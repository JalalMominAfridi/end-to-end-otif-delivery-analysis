
-- OTIF order-level transformation
-- Only delivered orders are included.

CREATE VIEW IF NOT EXISTS otif_order_performance AS

WITH delivery_summary AS (
    SELECT
        d.order_id,
        MAX(d.actual_delivery_date) AS final_delivery_date
    FROM deliveries d
    GROUP BY d.order_id
),

ordered_quantities AS (
    SELECT
        order_id,
        product_id,
        SUM(ordered_quantity) AS ordered_quantity
    FROM order_items
    GROUP BY order_id, product_id
),

delivered_quantities AS (
    SELECT
        d.order_id,
        di.product_id,
        SUM(di.delivered_quantity) AS delivered_quantity
    FROM deliveries d
    JOIN delivery_items di
        ON d.delivery_id = di.delivery_id
    GROUP BY d.order_id, di.product_id
),

full_delivery AS (
    SELECT
        o.order_id,
        CASE
            WHEN SUM(
                CASE
                    WHEN COALESCE(dq.delivered_quantity, 0)
                         < oq.ordered_quantity
                    THEN 1 ELSE 0
                END
            ) = 0
            THEN 1
            ELSE 0
        END AS in_full
    FROM orders o
    JOIN ordered_quantities oq
        ON o.order_id = oq.order_id
    LEFT JOIN delivered_quantities dq
        ON oq.order_id = dq.order_id
        AND oq.product_id = dq.product_id
    GROUP BY o.order_id
)

SELECT
    o.order_id,
    o.promised_date,
    ds.final_delivery_date,

    CASE
        WHEN DATE(ds.final_delivery_date) <= DATE(o.promised_date)
        THEN 1 ELSE 0
    END AS on_time,

    fd.in_full,

    CASE
        WHEN DATE(ds.final_delivery_date) <= DATE(o.promised_date)
             AND fd.in_full = 1
        THEN 1 ELSE 0
    END AS otif

FROM orders o
JOIN delivery_summary ds
    ON o.order_id = ds.order_id
JOIN full_delivery fd
    ON o.order_id = fd.order_id
WHERE LOWER(o.order_status) = 'delivered';

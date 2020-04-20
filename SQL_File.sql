SELECT
  t1.num AS 订单统计量,
  t2.num AS 国内出票量,
  t3.num AS 国际出票量,
  t4.num AS 保险销售量,
  t5.num AS 行李销售量
FROM
  (
    SELECT '{0}' AS currentDate,
    COUNT(1) AS num
  FROM
    (
      SELECT DISTINCT ord.order_no
    FROM
      table_1 ord
    WHERE
      ord.BOOKING_TIME >= TO_DATE('{0} 00:00:00', 'yyyy-MM-dd HH24:mi:ss')
      AND ord.BOOKING_TIME <= TO_DATE('{0} 23:59:59', 'yyyy-MM-dd HH24:mi:ss'))) t1,
  (
    SELECT '{0}' AS currentDate,
    COUNT(1) AS num
  FROM
    (
      SELECT DISTINCT ord.ticket_no
    FROM
      table_1 ord
    WHERE
      ord.order_status = '3'
      AND ord.order_infosource = '国内'
      AND ord.iss_date >= TO_DATE('{0} 00:00:00', 'yyyy-MM-dd HH24:mi:ss')
      AND ord.iss_date <= TO_DATE('{0} 23:59:59', 'yyyy-MM-dd HH24:mi:ss')
    GROUP BY
      ord.ticket_no)) t2,
  (
    SELECT '{0}' AS currentDate,
    COUNT(1) AS num
  FROM
    (
      SELECT DISTINCT ord.ticket_no
    FROM
      table_1 ord
    WHERE
      ord.order_status = '3'
      AND ord.order_infosource = '国际'
      AND ord.iss_date >= TO_DATE('{0} 00:00:00', 'yyyy-MM-dd HH24:mi:ss')
      AND ord.iss_date <= TO_DATE('{0} 23:59:59', 'yyyy-MM-dd HH24:mi:ss')
    GROUP BY
      ord.ticket_no)) t3,
  (
    SELECT '{0}' AS currentDate,
    COUNT(1) AS num
  FROM
    table_2 ins
  WHERE
    ins.remark = '购票购保'
	and ins.INSURANCE_ORDER_NO is not null
    AND ins.booking_time >= TO_DATE('{0} 00:00:00', 'yyyy-MM-dd HH24:mi:ss')
    AND ins.booking_time <= TO_DATE('{0} 23:59:59', 'yyyy-MM-dd HH24:mi:ss')) t4,
  (
    SELECT '{0}' AS currentDate,
    COUNT(1) AS num
  FROM
    table_3 bag
  WHERE
    bag.status = '3'
    AND bag.iss_date >= TO_DATE('{0} 00:00:00', 'yyyy-MM-dd HH24:mi:ss')
    AND bag.iss_date <= TO_DATE('{0} 23:59:59', 'yyyy-MM-dd HH24:mi:ss')) t5
WHERE
  t1.currentDate = t2.currentDate
  AND t2.currentDate = t3.currentDate
  AND t3.currentDate = t4.currentDate
  AND t4.currentDate = t5.currentDate

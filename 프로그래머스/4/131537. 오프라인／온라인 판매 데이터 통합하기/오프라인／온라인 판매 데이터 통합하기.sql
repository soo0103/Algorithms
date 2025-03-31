SELECT DATE_Format(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE YEAR(SALES_DATE) = '2022' AND Month(SALES_DATE) = '3'
UNION
SELECT DATE_Format(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE YEAR(SALES_DATE) = '2022' AND Month(SALES_DATE) = '3'
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID
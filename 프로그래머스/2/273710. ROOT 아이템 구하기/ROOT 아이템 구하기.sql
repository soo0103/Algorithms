SELECT I.ITEM_ID AS ITEM_ID, I.ITEM_NAME AS ITEM_NAME
FROM ITEM_INFO I, ITEM_TREE T
WHERE I.ITEM_ID = T.ITEM_ID AND T.PARENT_ITEM_ID IS NULL
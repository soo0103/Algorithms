SELECT COUNT(A.ID) AS FISH_COUNT
FROM FISH_INFO A, FISH_NAME_INFO B
WHERE A.FISH_TYPE = B.FISH_TYPE AND B.FISH_NAME IN ('BASS', 'SNAPPER')
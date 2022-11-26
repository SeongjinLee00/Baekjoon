-- 코드를 입력하세요
# SELECT mcdp_cd as'진료과코드', count(*) as '5월예약건수' from appointment
# where month(apnt_ymd)=5 and year(apnt_ymd)=2022
# group by mcdp_cd
# order by '5월예약건수' ASC, '진료과코드' ASC;

SELECT MCDP_CD AS 진료과코드, COUNT(*) AS 5월예약건수
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY 5월예약건수 ASC,진료과코드 ASC
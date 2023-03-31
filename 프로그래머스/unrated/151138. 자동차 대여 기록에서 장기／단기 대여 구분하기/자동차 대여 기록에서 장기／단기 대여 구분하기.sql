-- 코드를 입력하세요
SELECT history_id, car_id, date_format(start_date,'%Y-%m-%d'), date_format(end_date,'%Y-%m-%d'), case when datediff(end_date,start_date)>=29 then '장기 대여' else '단기 대여' end
from car_rental_company_rental_history h
where month(start_date)=9 and year(start_date)=2022
order by history_id desc
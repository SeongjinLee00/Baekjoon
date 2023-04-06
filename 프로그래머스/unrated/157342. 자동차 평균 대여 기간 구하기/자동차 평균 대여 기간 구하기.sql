-- 코드를 입력하세요
select car_id, average_duration from (
SELECT car_id, round(avg(datediff(end_date,start_date)+1),1) as average_duration from car_rental_company_rental_history
group by car_id
order by 2 desc, 1 desc
    ) a
where average_duration>=6
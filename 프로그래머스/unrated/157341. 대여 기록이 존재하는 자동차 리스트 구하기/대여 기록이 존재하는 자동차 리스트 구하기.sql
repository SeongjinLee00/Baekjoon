-- 코드를 입력하세요
SELECT distinct l.car_id from car_rental_company_car l
left join car_rental_company_rental_history r on l.car_id=r.car_id
where car_type='세단' and substr(start_date,6,2)=10
order by l.car_id DESC
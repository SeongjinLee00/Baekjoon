-- 코드를 입력하세요 
SELECT a.product_id, a.product_name, sum(a.price*b.amount) s from food_product a
left join food_order b on a.product_id=b.product_id
where month(b.produce_date)=5 and year(b.produce_date)=2022
group by a.product_id
order by s DESC, a.product_id ASC
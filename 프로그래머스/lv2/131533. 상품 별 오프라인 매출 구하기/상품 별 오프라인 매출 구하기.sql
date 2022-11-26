-- 코드를 입력하세요
SELECT a.product_code, a.price*sum(b.sales_amount) as sales from product a
left join offline_sale b on a.product_id=b.product_id
group by a.product_id
order by sales DESC, product_code ASC
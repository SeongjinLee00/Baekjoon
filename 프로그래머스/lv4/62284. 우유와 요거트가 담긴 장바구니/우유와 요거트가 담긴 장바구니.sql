-- 코드를 입력하세요
SELECT a.cart_id from cart_products a
inner join (select cart_id from cart_products where name='Yogurt') b
on a.cart_id=b.cart_id
where a.name='Milk'
order by a.cart_id ASC
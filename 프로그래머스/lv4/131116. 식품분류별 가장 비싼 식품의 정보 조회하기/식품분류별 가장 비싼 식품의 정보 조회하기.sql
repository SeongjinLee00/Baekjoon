-- 코드를 입력하세요
select a.category, a.price, a.product_name from food_product a
join (select category, max(price) as MAX_PRICE from food_product group by category) b
on a.category=b.category and a.price=b.MAX_PRICE
having category in ('과자', '국', '김치', '식용유')
order by price DESC

# SELECT FP.CATEGORY, SQ.MAX_PRICE, FP.PRODUCT_NAME
# FROM FOOD_PRODUCT FP
#      JOIN 
#     (SELECT CATEGORY, MAX(PRICE) MAX_PRICE
#      FROM FOOD_PRODUCT
#      GROUP BY CATEGORY
#      HAVING CATEGORY IN ('과자', '국', '김치', '식용유')) SQ
#      ON FP.CATEGORY = SQ.CATEGORY AND FP.PRICE = SQ.MAX_PRICE 
# ORDER BY SQ.MAX_PRICE DESC;
-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) from first_half a
left join icecream_info b on a.flavor=b.flavor
group by ingredient_type
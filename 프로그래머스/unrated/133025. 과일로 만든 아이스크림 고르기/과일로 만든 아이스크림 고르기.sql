-- 코드를 입력하세요
SELECT first_half.flavor from first_half
left join icecream_info on first_half.flavor = icecream_info.flavor
where icecream_info.ingredient_type = 'fruit_based' and first_half.total_order>3000
order by total_order DESC
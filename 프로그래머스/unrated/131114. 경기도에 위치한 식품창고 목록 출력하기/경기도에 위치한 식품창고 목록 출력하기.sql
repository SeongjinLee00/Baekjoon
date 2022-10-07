-- 코드를 입력하세요
SELECT WAREHOUSE_ID, warehouse_name, address, ifnull(freezer_yn,'N') from food_warehouse 
where substr(address,1,2) = '경기'
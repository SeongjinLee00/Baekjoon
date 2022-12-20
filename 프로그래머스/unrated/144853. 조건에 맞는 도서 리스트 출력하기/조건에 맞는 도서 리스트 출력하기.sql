-- 코드를 입력하세요
SELECT book_id,substr(published_date,1,10) from book
where year(published_date)=2021 and category='인문'
order by published_date ASC
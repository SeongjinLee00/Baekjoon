-- 코드를 입력하세요
SELECT category,sum(sales) from book
left join book_sales on book.book_id=book_sales.book_id
where year(book_sales.sales_date)=2022 and month(book_sales.sales_date)=1
group by book.category
order by book.category ASC
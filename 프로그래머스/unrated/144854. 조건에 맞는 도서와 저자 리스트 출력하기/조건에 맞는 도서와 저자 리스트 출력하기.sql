-- 코드를 입력하세요
SELECT book_id, author_name, to_char(book.published_date,'yyyy-mm-dd') from book
left outer join author on author.author_id=book.author_id
where book.category='경제'
order by published_date ASC
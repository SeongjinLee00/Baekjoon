-- 코드를 입력하세요
SELECT title, a.board_id, reply_id, b.writer_id, b.contents, date_format(b.created_date,'%Y-%m-%d') from used_goods_board a
inner join used_goods_reply b on a.board_id=b.board_id
where month(a.created_date)=10 and year(a.created_date)=2022
order by b.created_date asc, 1 asc
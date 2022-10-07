-- 코드를 입력하세요
SELECT member_id, member_name, gender, date_of_birth from member_profile
where tlno is not null and substr(date_of_birth,6,2) = '03' and gender = 'W'
order by member_id asc
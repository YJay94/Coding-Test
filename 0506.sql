-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,'%Y-%m-%d') as 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


where다음에 orderby와야한다....




-- 코드를 입력하세요
SELECT name, count(animal_id)
FROM animal_ins
WHERE name is not null
group by name
having count(animal_id) > 1
order by name

having 잘사용핼... group by 다음에...



SELECT HOUR(DATETIME), COUNT(*)
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)
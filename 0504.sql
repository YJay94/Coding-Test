-- 코드를 입력하세요
SELECT animal_type, IFNULL(name,'No name') AS name, set_upon_intake
FROM animal_ins
ORDER BY animal_id asc



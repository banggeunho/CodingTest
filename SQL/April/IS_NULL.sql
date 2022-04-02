// NULL인 값을 WHERE 조건문에 넣어 출력한다.
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL

// NULL이 아니면 NOT NULL 사용
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL

// NULL 처리 (IFNULL 사용), CASE문도 사용 가능
SELECT ANIMAL_TYPE,
  IFNULL(NAME, "No name") as NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS


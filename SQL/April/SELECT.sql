// 정렬
SELECT * from ANIMAL_INS ORDER BY ANIMAL_ID;

// 역순 정렬
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC

// WHERE 조건문
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION='Sick'

// 조건문과 정렬
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID

// 정렬
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC

// 여러개의 조건으로 정렬
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC

// LIMIT을 이용한 상위 N개 출력
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1
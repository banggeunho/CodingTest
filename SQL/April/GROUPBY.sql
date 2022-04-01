// 특정 컬럼의 VALUE별 데이터의 갯수를 구하기 (GROUP BY 이용)
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE

// 특정 이름의 데이터 갯수가 2개 이상인 경우 출력
// GROUP BY로 NAME별로 묶고, HAVING으로 조건을 주어 2개 이상인 이름만 묶는다.
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME

// DATETIME 형식의 시간을 가져오기 위해선 HOUR()로 가져올 수 있음
// 시간이 9시부터 20시전까지인 데이터를 가져와 HOUR 별로 묶어 카운트 해줍니다. 
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) < 20 
GROUP BY HOUR
ORDER BY HOUR


// 변수는 SET @hour 이런식으로 선언 가능
// 반복문으로 설정하여 hour 변수를 1씩 더해가면서 그에 맞는 데이터를 불러와 카운트해서 출력해줍니다.
SET @hour = -1;
SELECT @hour := @hour + 1 AS HOUR,
    ( SELECT COUNT(DATETIME)
     FROM ANIMAL_OUTS
     WHERE HOUR(DATETIME) = @hour ) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
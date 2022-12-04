WITH Fibonacci ( PrevN,  N) AS
(
     SELECT CAST(0 AS BIGINT) , CAST(1 AS BIGINT)
     UNION ALL
     SELECT  CAST(N AS BIGINT)  , CAST(PrevN + N  AS BIGINT)  
     FROM Fibonacci    
)
SELECT top 90 PrevN as Fibo
     FROM Fibonacci   

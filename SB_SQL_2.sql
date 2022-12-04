with c as (
select name , value  , 
ROW_NUMBER() OVER(PARTITION BY name ORDER BY (SELECT NULL)) as rn
from  people
	cross apply string_split(name , ' ')
)
select [2] as ��� ,
				[1] as ������� , 
				[3] as ��������
from c pivot(max(value) for rn in([2] , [1] , [3]  ) ) as pv




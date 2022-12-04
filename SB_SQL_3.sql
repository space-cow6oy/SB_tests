select people.id  , name ,sale_count , rank() over (order by sale_count desc) as sale_rank
from
 (
select people_id   , count(sale)  as sale_count
from  sales 
group by people_id 
) as g join people on g.people_id = people.id

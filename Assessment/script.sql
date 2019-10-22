-- write your code in PostgreSQL 9.4
select place
from (select place
           , sum(score) as score 
      from (select place
                 , case when opinion = 'recommended' then 1
                   else -1 end as score
            from opinions) as foo
      group by place
      having sum(score) > 0) as bar
order by place;
     

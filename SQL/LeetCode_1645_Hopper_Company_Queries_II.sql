# Write your MySQL query statement below

WITH RECURSIVE seq AS (SELECT 1 AS value UNION ALL SELECT value + 1 FROM seq WHERE value < 12)

, cte_rides as 
(
        select 
            ride_id
        ,   extract(month from r.requested_at) "month"
        ,   extract(year from r.requested_at) "year"
        ,   extract(year_month from r.requested_at) "year_month" 
        from rides r)

, cte_drivers as (select driver_id, extract(year_month from d.join_date) join_date from drivers d)

select 
    seq.value "month"
,   coalesce(round((count(distinct a.driver_id)/count(distinct d.driver_id)) * 100,2),0) "working_percentage"
from      seq
left join cte_rides r on seq.value = r.month and r.year = 2020
left join acceptedrides a on a.ride_id = r.ride_id
left join cte_drivers d on r.year_month >= d.join_date
where 1=1  
group by seq.value

# Write your MySQL query statement below


with cte as 
(
    select 
        *
    ,   row_number() over (partition by username order by startdate desc) rn
    ,   count(startdate) over (partition by username order by username) cnt 
    from useractivity u
)

select 
    username
,   activity
,   startdate
,   enddate
from cte
where rn = 2 or cnt = 1




; with cte_details_1 as
(
    select 
        hall_id
    ,   start_day
    ,   end_day
    ,   min(start_day) over (partition by hall_id order by start_day, end_day rows between unbounded preceding and 1 preceding) min_start_day
    ,   max(end_day) over (partition by hall_id order by start_day, end_day rows between unbounded preceding and 1 preceding) max_end_day
    ,   case when start_day > max(end_day) over (partition by hall_id order by start_day, end_day rows between unbounded preceding and 1 preceding)
                  or
                  max(end_day) over (partition by hall_id order by start_day, end_day rows between unbounded preceding and 1 preceding) is null
             then 1 else 0 end as ind
    from hallevents
)

, cte_details_2 as 
(
    select 
        hall_id
    ,   start_day
    ,   end_day
    ,   sum(ind) over (partition by hall_id order by start_day, end_day) sum_ind
    from cte_details_1 
)

select 
    hall_id
,   min(start_day) as start_day
,   max(end_day) as end_day
from cte_details_2
group by hall_id, sum_ind
order by hall_id, start_day

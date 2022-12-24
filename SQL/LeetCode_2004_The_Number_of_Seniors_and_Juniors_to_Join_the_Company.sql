/* Write your T-SQL query statement below */

; with cte_cume as 
(
    select 
        c.experience
    ,   1 as dummy
    ,   sum(salary) over (partition by c.experience order by salary,employee_id) cume_sum
    from candidates c
)

, cte_senior as 
(
    select 
        experience
    ,   1 as dummy
    ,   max(case when experience = 'Senior' and cume_sum <= 70000 then cume_sum else 0 end) snr_max_salary
    ,   sum(case when experience = 'Senior' and cume_sum <= 70000 then 1 else 0 end) snr_accepted_candidates 
    from cte_cume
    where experience = 'Senior'
    group by experience, dummy
)

, cte_junior as 
(
    select 
        a1.experience
    ,   sum(case when snr_max_salary < 70000 then case when a1.experience = 'Junior' and cume_sum <= (70000 - snr_max_salary) then 1 else 0 end else 0 end) jnr_accepted_candidates
    from cte_cume a1
    join cte_senior a2 on a1.dummy = a2.dummy
    where a1.experience = 'Junior'
    group by a1.experience
)

select experience, jnr_accepted_candidates accepted_candidates from cte_junior
union
select experience, snr_accepted_candidates accepted_candidates from cte_senior


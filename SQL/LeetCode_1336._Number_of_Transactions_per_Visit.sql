# Write your MySQL query statement below

with recursive
  cte_join as 
(
    select 
        v.visit_date
    ,   v.user_id
    ,   case when c.user_id is null then 0 else count(c.user_id) end txn_count
    from visits v
    left join transactions c on v.user_id = c.user_id and v.visit_date = c.transaction_date
    group by v.visit_date,v.user_id
)


, cte_txn_cnt as 
(
    select 
        txn_count as transactions_count 
    ,   count(*) as visits_count 
    from cte_join
    group by txn_count
)

, cte_seq as 
(
    select min(transactions_count) as transactions_count, max(transactions_count) as max_transactions_count from cte_txn_cnt 
    union all
    select transactions_count + 1, max_transactions_count from cte_seq where transactions_count < max_transactions_count
    union
    select 0 as transactions_count, max_transactions_count as max_transactions_count from cte_seq
)

select 
    c4.transactions_count
,   case when c3.visits_count is null then 0 else c3.visits_count end as visits_count
from cte_seq c4
left join cte_txn_cnt c3 on c4.transactions_count = c3.transactions_count
order by 1

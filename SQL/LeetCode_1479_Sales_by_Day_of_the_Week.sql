/* Write your T-SQL query statement below */
; with cte as
    (
        select distinct
            item_category
        ,   datename(dw,order_date) dayOfWeek
        ,   sum(o.quantity) over (partition by datename(dw,order_date), item_category)  Quantity
        from      items i
        left join orders o on o.item_id = i.item_id
    )


select 
    item_category as Category
,   sum(case when dayOfWeek = 'Monday' then quantity else 0 end) as Monday
,   sum(case when dayOfWeek = 'Tuesday' then quantity else 0 end) as Tuesday
,   sum(case when dayOfWeek = 'Wednesday' then quantity else 0 end) as Wednesday
,   sum(case when dayOfWeek = 'Thursday' then quantity else 0 end) as Thursday
,   sum(case when dayOfWeek = 'Friday' then quantity else 0 end) as Friday
,   sum(case when dayOfWeek = 'Saturday' then quantity else 0 end) as Saturday
,   sum(case when dayOfWeek = 'Sunday' then quantity else 0 end) as Sunday
from cte
group by item_category
order by item_category
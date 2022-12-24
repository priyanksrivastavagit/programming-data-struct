/* Write your T-SQL query statement below */

; with cte_2nd_sold_brand as 
    (
        select 
            *
        from 
        (
            select
                u.user_id
            ,   i.item_brand
            ,   case when i.item_id is null then 'no' else 'yes' end as "2nd_item_fav_brand"
            ,   row_number() over (partition by o.seller_id order by o.order_date) rn
            from users u
            left join orders o on u.user_id = o.seller_id
            left join items i on o.item_id = i.item_id and u.favorite_brand = i.item_brand
        ) src
        where 1=1
        and   src.rn = 2
    )


    select 
        u.user_id as seller_id
    ,   case when cte.user_id is null then 'no' else [2nd_item_fav_brand] end as "2nd_item_fav_brand"
    from      users u
    left join cte_2nd_sold_brand cte on u.user_id = cte.user_id

    
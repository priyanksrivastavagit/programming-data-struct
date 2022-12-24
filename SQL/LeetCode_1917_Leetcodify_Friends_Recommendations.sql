/* Write your T-SQL query statement below */

    ; with cte_frnd as 
    (
        select user1_id id_1, user2_id id_2 from friendship
        union
        select user2_id id_1, user1_id id_2 from friendship
    )


    select distinct
        l1.user_id
    ,   l2.user_id recommended_id
    from      listens l1
    join      listens l2 on l1.day = l2.day and l1.song_id = l2.song_id and l1.user_id <> l2.user_id
    --left join cte_frnd frnd on frnd.id_1 = l1.user_id and frnd.id_2 = l2.user_id
    where 1=1
    and   not exists (select * from cte_frnd frnd where frnd.id_1 = l1.user_id and frnd.id_2 = l2.user_id)
    group by l1.user_id, l2.user_id, l1.day
    having count(distinct l1.song_id) >= 3;
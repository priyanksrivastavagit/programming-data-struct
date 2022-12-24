/* Write your T-SQL query statement below */

;with cte_comb as 
(
    select first_player player, sum(first_score) score from matches group by first_player
    union all
    select second_player player, sum(second_score) score from matches group by second_player
) 

, cte_player_score as
(
    select 
        p.group_id
    ,   cte.player
    ,   sum(score) score
    from cte_comb cte
    join players p on cte.player = p.player_id
    group by p.group_id, cte.player
)


select 
    group_id
,   player_id
from 
(
    select 
        group_id
    ,   player player_id
    ,   row_number() over(partition by group_id order by score desc, player) rn
    from cte_player_score
) src 
where src.rn = 1
order by group_id


select
d.id ,
d.name,
di.dish_id_ingredient,
din.name
from fit_dish d
join fit_dish_ingredient di on di.dish_id = d.id
join fit_dish din on di.dish_id_ingredient = din.id

where di.dish_id_ingredient is not null
order by din.name
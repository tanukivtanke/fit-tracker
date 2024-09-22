alter table fit_dish_ingredient rename column food_id to food_id_ingredient;
alter table fit_dish_ingredient add column dish_id_ingredient integer;


alter table fit_dish_ingredient rename column food_id_ingredient to food_id_ingredient_temp;
alter table fit_dish_ingredient add column food_id_ingredient integer;
update fit_dish_ingredient set food_id_ingredient = food_id_ingredient_temp;
alter table fit_dish_ingredient drop column food_id_ingredient_temp;


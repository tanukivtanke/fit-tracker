INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Egg', 12.8, 23.0, 34.1, 155);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Pasta', 12.0, 3.3, 67.0, 180);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Ketchup', 2.0, 1.0, 53.9, 100);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Хурма', 1.0, 2.0, 78.9, 127);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Свинина', 15.0, 35.0, 68.5, 280);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Баклажан', 1.0, 3.0, 24.8, 36);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Картофель', 6.0, 1.0, 86.2, 74.5);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Лук', 1.0, 1.0, 9, 12);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Морковь', 2.0, 2.0, 64.9, 68);

INSERT INTO dish (name, out_of_stock, recipe) VALUES ('Egged macaroni', False, 'Яйца смешать с макаронами и поджарить 10 минут.');
INSERT INTO dish (name, out_of_stock, recipe) VALUES ('Рагу овощное со свининой', True, 'Все овощи порезать и потушить 30 минут или более.');

INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (250, 1, 1);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (100, 2, 1);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (800, 5, 2);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (350, 6, 2);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (550, 7, 2);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (150, 8, 2);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (127, 9, 2);
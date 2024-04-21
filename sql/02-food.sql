CREATE TABLE food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    proteins REAL,
    fats REAL,
    carbs REAL,
    kcal REAL
);

CREATE TABLE dish (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    out_of_stock BOOLEAN
);

CREATE TABLE dish_ingredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_id INTEGER,
    food_id INTEGER,
    amount INTEGER
);

CREATE TABLE meal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_id INTEGER,
    food_id INTEGER,
    meal_group_id INTEGER,
    amount INTEGER
);

CREATE TABLE meal_group (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_name TEXT,
    user_id INTEGER,
    day DATE,
    meal_order_id INTEGER
);


CREATE TABLE meal_order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ordering INTEGER
);

INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Egg', 12.8, 23.0, 34.1, 155);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Pasta', 12.0, 3.3, 67.0, 180);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Ketchup', 2.0, 1.0, 53.9, 100);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Хурма', 1.0, 2.0, 78.9, 127);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Свинина', 15.0, 35.0, 68.5, 280);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Баклажан', 1.0, 3.0, 24.8, 36);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Картофель', 6.0, 1.0, 86.2, 74.5);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Лук', 1.0, 1.0, 9, 12);
INSERT INTO food (name, proteins, fats, carbs, kcal) VALUES ('Морковь', 2.0, 2.0, 64.9, 68);

INSERT INTO dish (name, out_of_stock) VALUES ('Egged macaroni', False);
INSERT INTO dish (name, out_of_stock) VALUES ('Рагу овощное со свининой', True);

INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (250, 1, 1);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (100, 2, 1);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (800, 5, 2);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (350, 6, 2);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (550, 7, 2);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (150, 8, 2);
INSERT INTO dish_ingredient (amount, food_id, dish_id) VALUES (127, 9, 2);

INSERT INTO meal (amount, dish_id, meal_group_id) VALUES (250, 1, 1);
INSERT INTO meal (amount, food_id, meal_group_id) VALUES (20, 3, 1);
INSERT INTO meal (amount, food_id, meal_group_id) VALUES (56, 1, 2);
INSERT INTO meal (amount, dish_id, meal_group_id) VALUES (280, 2, 2);
INSERT INTO meal (amount, food_id, meal_group_id) VALUES (80, 4, 3);


INSERT INTO meal_group (user_id, day, meal_order_id ) VALUES (1, DATE('now'), 1);
INSERT INTO meal_group (user_id, day, meal_order_id ) VALUES (1, DATE('now'), 2);
INSERT INTO meal_group (meal_name, user_id, day, meal_order_id ) VALUES ('Кушоц', 1, DATE('now'), 3);

INSERT INTO meal_order (name, ordering) VALUES ('Breakfast', 1);
INSERT INTO meal_order (name, ordering) VALUES ('Dinner', 10);
INSERT INTO meal_order (name, ordering) VALUES ('Supper', 20);

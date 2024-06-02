CREATE TABLE food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    proteins REAL NOT NULL ,
    fats REAL NOT NULL,
    carbs REAL NOT NULL,
    kcal REAL NOT NULL
);

CREATE TABLE dish (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL ,
    out_of_stock BOOLEAN NOT NULL,
    recipe TEXT NOT NULL
);

CREATE TABLE dish_ingredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_id INTEGER NOT NULL,
    food_id INTEGER NOT NULL,
    amount INTEGER NOT NULL
);

CREATE TABLE meal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_id INTEGER,
    food_id INTEGER,
    meal_group_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    calc_proteins REAL NOT NULL,
    calc_fats REAL NOT NULL,
    calc_carbs REAL NOT NULL,
    calc_kcal REAL NOT NULL
);

CREATE TABLE meal_group (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_name TEXT,
    user_id INTEGER NOT NULL,
    day DATE NOT NULL,
    meal_order_id INTEGER NOT NULL
);


CREATE TABLE meal_order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE ,
    ordering INTEGER NOT NULL
);



INSERT INTO meal_order (name, ordering) VALUES ('Завтрак', 1);
INSERT INTO meal_order (name, ordering) VALUES ('Второй завтрак', 5);
INSERT INTO meal_order (name, ordering) VALUES ('Обед', 10);
INSERT INTO meal_order (name, ordering) VALUES ('Полдник', 20);
INSERT INTO meal_order (name, ordering) VALUES ('Ужин', 30);
INSERT INTO meal_order (name, ordering) VALUES ('Последний ужин', 35);

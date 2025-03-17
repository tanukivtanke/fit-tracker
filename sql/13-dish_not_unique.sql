CREATE TABLE fit_dish_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL ,
    out_of_stock BOOLEAN NOT NULL,
    recipe TEXT NOT NULL,
    last_used DATE,
    for_dish INTEGER
);
INSERT INTO fit_dish_new select * from fit_dish;
DROP table fit_dish;
ALTER TABLE fit_dish_new rename to fit_dish;

CREATE TABLE gym_equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT UNIQUE NOT NULL);


CREATE TABLE gym_exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT UNIQUE NOT NULL,
    weights_quantity INTEGER,
    equipment_id INTEGER,
    FOREIGN KEY(equipment_id) REFERENCES gym_equipment(id));


CREATE TABLE gym_training_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT UNIQUE NOT NULL);


CREATE TABLE gym_training_plan_components (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    superset_id INTEGER,
    exercise_id INTEGER,
    training_plan_id INTEGER NOT NULL,
    FOREIGN KEY(training_plan_id) REFERENCES gym_training_plans(id));


CREATE TABLE gym_training_journal (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    training_plan_id INTEGER NOT NULL,
    date DATE,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id));


CREATE TABLE gym_training_details(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    training_journal_id INTEGER NOT NULL,
    set_num INTEGER NOT NULL,
    weight REAL NOT NULL,
    repetitions INTEGER NOT NULL,
    additional_info TEXT,
    training_plan_component_id INTEGER NOT NULL,
    FOREIGN KEY(training_plan_component_id) REFERENCES gym_training_plan_components(id));


CREATE TABLE gym_exercise_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT UNIQUE NOT NULL);

CREATE TABLE gym_grouping (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    exercise_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL,
    FOREIGN KEY(group_id) REFERENCES gym_exercise_groups(id));


CREATE TABLE gym_supersets (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    superset_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    FOREIGN KEY(exercise_id) REFERENCES gym_exercises(id));



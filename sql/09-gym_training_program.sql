create table gym_training_programs(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL
);

create table gym_training_program_components(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    training_plan_id INTEGER NOT NULL,
    training_program_id INTEGER NOT NULL
);

alter table gym_training_journal add column training_program_id INTEGER;
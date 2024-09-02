INSERT INTO gym_equipment (name) VALUES ('Dumbbell');
INSERT INTO gym_equipment (name) VALUES ('Barbell');
INSERT INTO gym_equipment (name) VALUES ('Machine');
INSERT INTO gym_equipment (name) VALUES ('Body');


INSERT INTO gym_exercises (name, equipment_id) VALUES ('Glute kickbacks', 3);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Back squat', 1);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Goblet sumo squats', 1);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Bentover rows', 2);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Tricep dips', 3);
INSERT INTO gym_exercises (name, equipment_id, weights_quantity) VALUES ('Leg raises', 4, 0);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Bench press', 2);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Tricep pushdown', 3);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Bicep curl(single-arm cable version)', 3);

INSERT INTO gym_exercises (name, equipment_id) VALUES ('Hack squat', 3);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Ovehead press', 2);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Leg extension', 3);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Hip thrust', 3);
INSERT INTO gym_exercises (name, equipment_id, weights_quantity) VALUES ('Bulgarian split squat', 1, 2);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Pull up', 3);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Chest flies(single-arm, from down to up)', 3);
INSERT INTO gym_exercises (name, equipment_id, weights_quantity) VALUES ('Sumo squats', 4, 0);
INSERT INTO gym_exercises (name, equipment_id) VALUES ('Chest flies(single-arm, from up to down)', 3);


INSERT INTO gym_training_plans (name) VALUES ('Compound day(full body)');
INSERT INTO gym_training_plans (name) VALUES ('Arm strength day(full body)');
INSERT INTO gym_training_plans (name) VALUES ('Leg focused day(full body)');


INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (1, 1);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (1, 2);
INSERT INTO gym_training_plan_components (training_plan_id, superset_id) VALUES (1, 2);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (1, 4);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (1, 5);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (1, 6);

INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (2, 7);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (2, 8);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (2, 9);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (2, 4);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (2, 10);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (2, 11);

INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (3, 2);
INSERT INTO gym_training_plan_components (training_plan_id, superset_id) VALUES (3, 1);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (3, 13);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (3, 14);
INSERT INTO gym_training_plan_components (training_plan_id, exercise_id) VALUES (3, 15);
INSERT INTO gym_training_plan_components (training_plan_id, superset_id) VALUES (3, 3);


INSERT INTO gym_exercise_groups (name) VALUES ('Leg exercises');
INSERT INTO gym_exercise_groups (name) VALUES ('Butt exercises');
INSERT INTO gym_exercise_groups (name) VALUES ('Quad exercises');
INSERT INTO gym_exercise_groups (name) VALUES ('Back exercises');
INSERT INTO gym_exercise_groups (name) VALUES ('Tricep exercises');
INSERT INTO gym_exercise_groups (name) VALUES ('Bicep exercises');
INSERT INTO gym_exercise_groups (name) VALUES ('Abs exercises');
INSERT INTO gym_exercise_groups (name) VALUES ('Shoulders exercises');
INSERT INTO gym_exercise_groups (name) VALUES ('Chest exercises');


INSERT INTO gym_grouping (group_id, exercise_id) VALUES (1, 1);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (1, 2);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (1, 3);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (1, 10);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (1, 12);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (1, 13);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (1, 14);

INSERT INTO gym_grouping (group_id, exercise_id) VALUES (2, 1);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (2, 3);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (2, 13);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (2, 14);

INSERT INTO gym_grouping (group_id, exercise_id) VALUES (3, 2);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (3, 10);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (3, 12);

INSERT INTO gym_grouping (group_id, exercise_id) VALUES (4, 4);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (4, 15);

INSERT INTO gym_grouping (group_id, exercise_id) VALUES (5, 5);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (5, 7);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (5, 8);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (5, 16);

INSERT INTO gym_grouping (group_id, exercise_id) VALUES (6, 9);

INSERT INTO gym_grouping (group_id, exercise_id) VALUES (7, 6);

INSERT INTO gym_grouping (group_id, exercise_id) VALUES (8, 5);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (8, 7);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (8, 11);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (8, 15);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (8, 16);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (9, 5);
INSERT INTO gym_grouping (group_id, exercise_id) VALUES (9, 16);

INSERT INTO gym_training_journal (user_id, training_plan_id, date) VALUES (1, 1, DATE('2024-08-17'));
INSERT INTO gym_training_journal (user_id, training_plan_id, date) VALUES (1, 3, DATE('2024-08-02'));
INSERT INTO gym_training_journal (user_id, training_plan_id, date) VALUES (1, 1, DATE('2024-08-30'));


INSERT INTO gym_supersets (superset_id, exercise_id) VALUES (1, 13);
INSERT INTO gym_supersets (superset_id, exercise_id) VALUES (1, 12);
INSERT INTO gym_supersets (superset_id, exercise_id) VALUES (2, 3);
INSERT INTO gym_supersets (superset_id, exercise_id) VALUES (2, 17);
INSERT INTO gym_supersets (superset_id, exercise_id) VALUES (3, 18);
INSERT INTO gym_supersets (superset_id, exercise_id) VALUES (3, 19);


INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 1, 5, 20, null, 1);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 2, 5, 20, null, 1);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 3, 5, 18, null, 1);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 4, 5, 35, null, 1);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 1, 10, 10, 'quality_deep', 2);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 2, 10, 12, 'quality', 2);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 3, 15, 11, 'quality', 2);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 4, 17.5, 7, 'quality', 2);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 1, 7, 8, null, 3);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 2, 7, 7, null, 3);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 4, 8, 6, null, 3);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 3, 7, 10, null, 3);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 5, 0, 13, null, 3);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 1, 0, 17, 'quality', 4);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 2, 0, 15, null, 4);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 3, 2.5, 15, null, 4);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 4, 0, 14, null, 4);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 1, -30, 10, null, 5);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 2, -30, 9, 'deep', 5);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 3, -35, 14, null, 5);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 4, -30, 8, null, 5);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 1, 0, 20, null, 6);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 2, 0, 18, null, 6);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 3, 0, 15, null, 6);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (1, 4, 0, 14, null, 6);


INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 1, 10, 12, null, 13);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 2, 12.5, 10, 'quality', 13);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 3, 12.5, 8, 'quality', 13);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 4, 12.5, 8, 'quality', 13);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 1, 5, 20, null, 14);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 2, 5, 20, null, 14);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 3, 5, 18, null, 14);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 4, 5, 35, null, 14);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 1, 5, 18, null, 15);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 2, 5, 17, null, 15);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 3, 7.5, 16, null, 15);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 4, 5, 17, null, 15);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 1, 6, 20, null, 16);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 2, 8, 18, null, 16);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 3, 8, 17, null, 16);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 4, 9, 15, null, 16);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 1, -30, 10, null, 17);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 2, -35, 13, null, 17);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 3, -35, 11, null, 17);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 4, -35, 13, null, 17);

INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 1, 2.5, 20, null, 18);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 2, 2.5, 18, null, 18);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 3, 2.5, 16, null, 18);
INSERT INTO gym_training_details(training_journal_id, set_num, weight, repetitions, additional_info, training_plan_component_id) VALUES (2, 4, 5, 25, null, 18);
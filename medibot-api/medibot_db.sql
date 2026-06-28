-- Create MediBot database
CREATE DATABASE IF NOT EXISTS medibot_db;
USE medibot_db;
CREATE TABLE IF NOT EXISTS symptoms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    disease VARCHAR(255) NOT NULL,
    fever TINYINT(1),
    headache TINYINT(1),
    cough TINYINT(1),
    fatigue TINYINT(1),
    stomach_pain TINYINT(1),
    nausea TINYINT(1),
    chest_pain TINYINT(1),
    dizziness TINYINT(1),
    sore_throat TINYINT(1),
    diarrhea TINYINT(1),
    rash TINYINT(1),
    shortness_of_breath TINYINT(1),
    joint_pain TINYINT(1)
);
CREATE TABLE IF NOT EXISTS disease_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    disease VARCHAR(255) NOT NULL,
    precautions TEXT,
    recommended_medicine VARCHAR(255),
    recommended_tests VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS medicine_book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medicine_name VARCHAR(255),
    uses TEXT,
    recommended_dose VARCHAR(255),
    side_effects TEXT
);
INSERT INTO medicine_book (medicine_name, uses, recommended_dose, side_effects)
VALUES
('Paracetamol','Fever, Pain','500mg every 6hrs','Liver toxicity in overdose'),
('Ibuprofen','Pain, Inflammation','400mg every 8hrs','Stomach upset'),
('Omeprazole','Stomach issues','20mg daily','Headache, nausea'),
('Amoxicillin','Bacterial infection','500mg every 8hrs','Nausea, diarrhea'),
('Ceftriaxone','Severe bacterial infection','1g daily','Diarrhea, rash'),
('Metformin','Diabetes','500mg twice daily','Nausea, diarrhea'),
('Amlodipine','Hypertension','5mg daily','Dizziness, swelling'),
('Antihistamine','Allergy','10mg daily','Drowsiness, dry mouth');
INSERT INTO disease_info (disease, precautions, recommended_medicine, recommended_tests)
VALUES
('Flu','Rest, fluids','Paracetamol','CBC, Temperature'),
('Migraine','Dark room, hydrate','Ibuprofen','MRI Head, Eye Exam'),
('Gastritis','Avoid spicy food, hydrate','Omeprazole','Endoscopy, Ultrasound'),
('Common Cold','Rest, hydrate','Antihistamine','Temperature Check, CBC'),
('Diabetes','Healthy diet, exercise','Metformin','Fasting Glucose, HbA1c'),
('Hypertension','Reduce salt, exercise','Amlodipine','Blood Pressure, ECG'),
('Strep Throat','Rest, hydrate','Amoxicillin','Throat Culture, CBC'),
('Pneumonia','Hospital care','Ceftriaxone','Chest X-ray, CBC'),
('Allergy','Avoid allergens','Antihistamine','Allergy Test, CBC'),
('Arthritis','Exercise, physiotherapy','Ibuprofen','X-ray, MRI Joint');
INSERT INTO symptoms (disease, fever, headache, cough, fatigue, stomach_pain, nausea, chest_pain, dizziness, sore_throat, diarrhea, rash, shortness_of_breath, joint_pain)
VALUES
('Flu',1,1,1,1,0,0,0,0,1,0,0,0,0),
('Migraine',0,1,0,1,0,0,0,0,0,0,0,0,0),
('Gastritis',0,0,0,1,1,1,0,0,0,1,0,0,0),
('Common Cold',0,1,1,0,0,0,0,0,1,0,0,0,0),
('Diabetes',0,0,0,1,0,0,0,0,0,0,0,0,0),
('Hypertension',0,0,0,1,0,0,1,0,0,0,0,0,0),
('Strep Throat',0,0,0,1,0,0,0,0,1,0,0,0,0),
('Pneumonia',1,1,1,1,0,0,1,0,1,0,0,1,0),
('Allergy',0,0,0,0,0,0,0,0,1,0,1,0,0),
('Arthritis',0,0,0,1,0,0,0,0,0,0,0,0,1);

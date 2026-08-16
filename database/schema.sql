CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

CREATE TABLE Patient (
    Patient_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT,
    Gender VARCHAR(10),
    Phone VARCHAR(15),
    Blood_Grp VARCHAR(5),
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password_Hash VARCHAR(255) NOT NULL
);

CREATE TABLE Admin (
    Admin_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password_Hash VARCHAR(255) NOT NULL
);

CREATE TABLE Doctor (
    Doctor_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Qualification VARCHAR(100),
    Specialization VARCHAR(100),
    Fee DECIMAL(10,2),
    Phone VARCHAR(15),
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password_Hash VARCHAR(255) NOT NULL,
    is_approved BOOLEAN DEFAULT FALSE
);

CREATE TABLE Appointment (
    Appointment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Patient_ID INT,
    Doctor_ID INT,
    Date DATE,
    Time TIME,
    Token_No INT,
    Status VARCHAR(50) DEFAULT 'Pending',
    Problem TEXT,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID) ON DELETE CASCADE,
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID) ON DELETE CASCADE
);

CREATE TABLE Prescription (
    Prescription_ID INT AUTO_INCREMENT PRIMARY KEY,
    Appointment_ID INT,
    Diagnosis TEXT,
    Medicine TEXT,
    Dosage TEXT,
    FOREIGN KEY (Appointment_ID) REFERENCES Appointment(Appointment_ID) ON DELETE CASCADE
);

CREATE TABLE Bill (
    Bill_ID INT AUTO_INCREMENT PRIMARY KEY,
    Appointment_ID INT,
    Bill_Date DATE,
    Amount DECIMAL(10,2),
    Payment_Mode VARCHAR(50),
    Payment_Status VARCHAR(50) DEFAULT 'Unpaid',
    FOREIGN KEY (Appointment_ID) REFERENCES Appointment(Appointment_ID) ON DELETE CASCADE
);

-- Insert Default Admin (Password: admin123)
-- Uses bcrypt hash for passlib
INSERT INTO Admin (Name, Email, Password_Hash) 
VALUES ('Super Admin', 'admin@hospital.com', '$2b$12$Kixb1a.s2Y/R2/K2k0bUq.hXfMAsM8ySInF6hS9xGE/Z0Qk9oJkS6');

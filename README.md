Flask API Project
This is a Flask application that implements a simple API with database interaction.

Table of Contents
Getting Started
Prerequisites
Installation
Database Schema
Sample Data
Dependencies
Git Workflow
Getting Started
Prerequisites
Before running the Flask application, ensure you have the following installed:

Python 3.x
Flask
MySQL Server
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/flask-api-project.git
cd flask-api-project
Install the required Python dependencies:
bash
Copy code
pip install -r requirements.txt
Set up the MySQL database with the following schema:
sql
Copy code
CREATE DATABASE users;

USE users;

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    role VARCHAR(255)
);
Database Schema
The database schema consists of a single table named "users" with the following columns:

id (int, primary key)
name (varchar)
email (varchar)
role (varchar)
Sample Data
You can populate the "users" table with sample data by running the following SQL queries:

sql
Copy code
INSERT INTO users (id, name, email, role)
VALUES
    (1, 'John Doe', 'john.doe@example.com', 'Admin'),
    (2, 'Jane Smith', 'jane.smith@example.com', 'User'),
    (3, 'Michael Johnson', 'michael.johnson@example.com', 'User'),
    (4, 'Emily Brown', 'emily.brown@example.com', 'Admin');
Dependencies
The application requires the following dependencies, which are listed in the requirements.txt file:

Flask==2.1.0
mysql-connector-python==8.0.26
You can install these dependencies using the pip install -r requirements.txt command.

Git Workflow
Our Git workflow follows the "feature branch workflow." To contribute to the project, follow these steps:

Fork the repository on GitHub.
Clone your forked repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/flask-api-project.git
cd flask-api-project
Create a new branch for your feature:
bash
Copy code
git checkout -b feature/new-feature
Make necessary changes and commit your work:
bash
Copy code
git add .
git commit -m "Implemented new feature"
Push your branch to your forked repository:
bash
Copy code
git push origin feature/new-feature
Create a pull request from your branch to the main branch on GitHub.

Your changes will be reviewed, and upon approval, they will be merged into the main branch.

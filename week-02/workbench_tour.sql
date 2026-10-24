/*
Ex1C - Workbench Readiness Check
Name: Idasha Lee   Date: 10/20/2026
Q1: Root is the user and the host name and portnumber is localhost:3306
Q2: You would select the plus + icon to create a brand new connection
Q3: 1.Navigator 2. Information 3. Query Editor 4. Output 5. SQL Additions 6. We will not be using SQL Additions.
Q4: Login User: root, Port: 3306, MySQL Version: 8.0.46
Q5: 2 Tools under MANAGMENT: Status and System Variables, Data Import/Restore
Q6: actor_id is a primary code data type. The PK stands for primary key and AI stands for auto increment.
Q7: film_actor has 3 colunms which includes actor_id, film_id, and last_update.It has a total of 2 foreign keys. The tables they point to is the actor_id and the film_id tables
Q8: A new query pulled up for film_actor result grid.
Q9: In the action output section it says that 200 rows were returned.
Q10: 1000 rows of sakila.film returned; however there was an error code 1146 stating that the table sakila.actr doesn't exist.
Q11: The vertical output looks more like a notepade or receipt format which can be useful when you just need to see the plain text and all identifiers grouped together. Compared to the normal result grid which just aligns it by the primary key and go down like columns. 
Q12: The last name to appear at the top is AKROYD, CHRISTIAN. 
Q13: There are 3 actor records under the last name DAVIS. 
Q14: first_name is a variable character data type with the maximum length/ display size of 45 characters. 
*/
USE sakila;
SELECT * FROM actor;
SELECT * FROM sakila.film;
SELECT * FROM actor;


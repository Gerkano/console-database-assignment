# console-database-assignment
Console program, which generates random employee list with names, surnames, age, salary and etc.
<!-- # console-database-assignment

# Create Console program :
# which would ask to:
# - create database ++++++++++++
# - create table (column names: name, surname. age, salary) ++++
# - populate table with 50 elements (name, surname auto generated, age from 18 to 99, salary from 50 000 to 250000 (with a step size of 25000))
# - print the names of people who earn more than entered value (in a prompt)
# - print all users (names and surnames)  +++++
# - delete user by surname ++++
# OOP, application should be runned a module .

# - extend database to 300 - 500 records.
# - get the average salaries in different age groups (ex. 20-29 , 30-39 etc. )
# - find 3 biggest age groups by number of people, get the names/surnames of 
# - the most/least and closest to average earning.

# - get all people wjo names start with name 'a' and surnames contains letter 'w'.
# - get all people who's salalry is lower than 150 000 or are older than 50 years old.
# - get all people and their salaries , where age varies from 38y. to 72y. 
# - get number of people and average salary of people who's age between 19 and 43.

    # ALTER TABLE
# Add column:
'ALTER TABLE <table_name> ADD COLUMN <column_name> INTEGER'
# Rename:
'ALTER TABLE <table_name> RENAME COLUMN <existing_column_name> TO <new_column_name>'
# Rename Table:
'ALTER TABLE <table_name> RENAME TO <new_table_name>' 
# Drop Column:
'ALTER TABLE <table_name> DROP COLUMN <column_name>'
# Note: The DROP COLUMN syntax is used to remove an existing column from a table. The DROP COLUMN command removes the named column from the table, and rewrites its content to purge the data associated with that column. The DROP COLUMN command only works if the column is not referenced by any other parts of the schema and is not a PRIMARY KEY and does not have a UNIQUE constraint.
'''
Tasks:
Update current code base with these 4 new methods. 
Test it.
First, lower the number of the possible entry to 100 the db -> table. (possible increase by 1000's)
Update current task that instead of creating 1 table,  it would create 2 : 
New table name = 'personalInfo' consist (name, surname, dob ('YYYY-MM-DD' format, year should be calculated from the age value, and other two values auto generates) (date of birth), email: (name.surname@gmail.com), phone(+3706******* , * - random numbers), sex (male, female, unicorn))
During the creation of the second table , it should use the same class object.
!! Important - names and surnames should be the same in both database tables by the same order. 
'''
Getting data from several tables: 
- Using WHERE statements:
SELECT <column> FROM <table1>, <table2> WHERE <statement> AND <statement>;
# table names: person, car
SELECT person.first_name, person.last_name, car.plate
FROM person, car
WHERE person.car_id = car.id
From 3 tables:
SELECT last_name, make, name
from person, car, company
WHERE person.car_id = car.id AND person.company_id = company.id
ORDER BY name
Example with extra statement:
SELECT last_name, make, name
from person, car, company
WHERE person.car_id = car.id 
AND person.company_id = company.id
AND make = "Ford"
ORDER BY name DESC;
'''
################################################################################################################################
#  - Update current implementation where the second table have different randomly generated names and surenames (generate dob randomly). 
#  - Count all the letter what makes all names and surnames in both tables: which table wins and by what margin?
# - Get all names and surnames from both tables where the age is more than 40y and less than 66.
# - Get all users (from both tables) whos names starts with letter 'B' and is male (sex).
# What is the most popular letter (and the 2nd and the 3rd) the names and surnames starts in both tables. 
# Create  a pie chart to see the distribution by sex. (Use matplotlib library - example: https://www.w3schools.com/python/matplotlib_pie_charts.asp)
########################################################################################################################
# Python tasks
'''
1st - Create a function which would take a sentence (a string. Can't be less than 25 characters - if so - report error!) and would print/return the number of the characters , and sort them out (You can use a list for that). 
'As tu' = ['a','s', 't', 'u'] 
2nd - Create a class and two methods which would do the same things as previuos task. All PEP requirements shoud be met.
''' -->

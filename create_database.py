from app import SqlDatabase
import names
from random import random, randint, randrange, choice
from sqlite3 import OperationalError as e
from datetime import date, timedelta




class DataInput:

    def __init__(self, database_name: str, table_name: str, how_many:str) -> None:
        self.database = SqlDatabase(database_name)
        self.table_name = table_name
        self.how_many = how_many
        self.create_data()

    def create_data(self) -> None:
        self.database.create_table(table_name=self.table_name, 
        columns="first_name TEXT NOT NULL, last_name TEXT NOT NULL, age INTEGER, salary INTEGER")
        self.database.create_table(table_name='personalInfo', 
        columns="first_name TEXT NOT NULL, last_name TEXT NOT NULL, date_of_birth TEXT NOT NULL, email TEXT NOT NULL, phone INTEGER, gender TEXT NOT NULL")
        self.database.create_table(table_name=f'{self.table_name}2nd', 
        columns="first_name TEXT NOT NULL, last_name TEXT NOT NULL, age INTEGER, salary INTEGER")
        for i in range(0, int(self.how_many)):
            gender_list = ['male', 'female']
            gender = choice(gender_list)
            name = names.get_first_name(gender=gender)
            surname = names.get_last_name()
            age = randint(18, 89)
            end_date = date.today()
            date_of_birth = end_date - timedelta(days=age*randint(365, 370))
            self.database.write(table_name=self.table_name, 
            entry_values=(f" '{name}', '{surname}', '{age}', '{randrange(50000, 250000, 25000)}' "))
            self.database.write(table_name='personalInfo', 
            entry_values=(f" '{name}', '{surname}', '{date_of_birth}', '{name}.{surname}@gmail.com', '3{randint(7060000000, 7069999999)}', '{gender}'"))
            self.database.write(table_name=f'{self.table_name}2nd', 
            entry_values=(f" '{names.get_first_name()}', '{names.get_last_name()}', '{randint(18, 89)}', '{randrange(50000, 250000, 25000)}' "))

    def show_all_employees(self) -> list:
        return self.database.read_all(
            
            columns="*", 
            table_name=self.table_name
        
        )
    
    def show_all_employees_info(self) -> list:
        return self.database.read_all(
            
            columns="*", 
            table_name='personalInfo'
        
        )
    def salary_above_input(self, user_input: int) -> list:
        return self.database.read(
            
            columns="first_name, last_name", 
            table_name=self.table_name, 
            where_clause=f"salary > {user_input}", 
            order_by="first_name"
            
        )

    def delete_employee(self, user_input: str) -> None:
        self.database.delete(

            table_name=self.table_name, 
            where_clause=f"last_name = '{user_input}'"

        )

    def find_employee(self, user_input: str) -> None:
        return self.database.read(
            
            columns= "*",
            table_name=self.table_name, 
            where_clause=f"last_name = '{user_input}'",
            order_by="last_name"

        )

    def filter_by_age(self, tablename, age_from: int, age_to: int, order_by: str, column_entrie: str) -> list:
        return self.database.read(
            
            columns=column_entrie, 
            table_name=tablename, 
            order_by=order_by,
            where_clause=f"age > {age_from} AND age < {age_to}" 
            
        
        )     


    def specific_filter(self) -> list:
        return self.database.read(

            columns="first_name, last_name", 
            table_name=self.table_name, 
            where_clause=f"age > 25 AND age < 50 AND salary > 100000 AND salary < 200000 GROUP BY first_name, last_name", 
            order_by="salary DESC"

        )

    def age_group(self) -> list:
        groups = [(18, 19), (20, 29), (30, 39), (40, 49), (50, 59), (60, 69), (70, 79), (80, 89)]
        all_group_employees = []
        for i in range(0, len(groups)):
            all_group_employees.append(self.database.read(

                columns="*", 
                table_name=self.table_name, 
                where_clause=f"age BETWEEN {groups[i][0]} AND {groups[i][1]}", 
                order_by="salary"

                )    
            )
        return all_group_employees

    def age_group_avg_salary(self) -> list:
        groups = [(18, 19), (20, 29), (30, 39), (40, 49), (50, 59), (60, 69), (70, 79), (80, 89)]
        all_group_salary = []
        for i in range(0, len(groups)): 
            all_group_salary.append(self.database.read(

                columns="ROUND(AVG(salary)), COUNT(*)", 
                table_name=self.table_name, 
                where_clause=f"age BETWEEN {groups[i][0]} AND {groups[i][1]}", 
                order_by="salary"
                
                )
            )
        return all_group_salary
            

    def names_aw(self) -> list:
        return self.database.read(

            columns="*", 
            table_name=self.table_name, 
            where_clause="first_name LIKE 'A%' AND last_name LIKE 'W%'", 
            order_by="salary"
            
        )

    def salary_and_age_filter(self) -> list:
        return self.database.read(
            
            columns="*",
            table_name=self.table_name,
            where_clause="salary < 150000 OR age > 50",
            order_by="first_name"

        )

    
    def age_filter(self) -> list:
        return self.database.read(

            columns="first_name, last_name, salary", 
            table_name=self.table_name, 
            where_clause=f"age > 38 AND age < 72", 
            order_by="salary DESC"

        )


    def age_salary_avarage(self) -> list:
        return self.database.read(

            columns="ROUND(AVG(salary), 2), COUNT(*)", 
            table_name=self.table_name, 
            where_clause=f"age > 19 AND age < 43", 
            order_by="salary DESC"

        )

    def name_lenght(self) -> list:
        return self.database.read_all(
            
            columns="first_name", 
            table_name=f"{self.table_name}, {self.table_name}2nd"
        
        )

    def add_column(self, column_name) -> None:
        self.database.add_column(

            table_name=self.table_name,
            where_clause=column_name
        )



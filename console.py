import curses
from curses import wrapper
from re import T
from create_database import DataInput
import time

class Console:

    def __init__(self) -> None:
        self.stdscr = curses.initscr()
        self.stdscr.clear()
        self.echo = curses.echo()
        self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
        self.stdscr.addstr(3, 0, "Enter the name of the database you want to ceate/access:", curses.A_STANDOUT)
        self.database = self.stdscr.getstr(3, 60, 15).decode("utf-8")
        self.stdscr.addstr(4, 0, "Enter the name of the table you want to ceate/access:", curses.A_STANDOUT)
        self.tablename = self.stdscr.getstr(4, 60, 15).decode("utf-8")
        self.how_many = self.how_many_check()
        self.data_init = DataInput(database_name=self.database, table_name=self.tablename, how_many=self.how_many)
        self.main(self.tablename, self.data_init.show_all_employees(), "All employees")
        self.menu()
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.getch()

    def how_many_check(self) -> int:
        while True:
            try:
                self.stdscr.addstr(5, 0, "Enter the number of entries you want to be ceated/added:", curses.A_STANDOUT)
                how_many = self.stdscr.getstr(5, 60, 4).decode("utf-8")
                return int(how_many)
            except:
                self.stdscr.addstr(5, 65, 4, "Please enter a number")

    def menu(self) -> None:
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
        self.stdscr.addstr(3, 0, "Menu(page 1):", curses.A_STANDOUT)
        for i in range(0, 10):
            self.stdscr.addstr(i+5, 0, '{}.'.format(i), curses.A_STANDOUT)
        self.stdscr.addstr(5, 3, "Show employees personal info")
        self.stdscr.addstr(6, 3, "Enter a salary to check who earns more")
        self.stdscr.addstr(7, 3, "Delete employee by surname")
        self.stdscr.addstr(8, 3, "Filter by age (enter two integers)")
        self.stdscr.addstr(9, 3, "Specific filter (age(25-50) AND salary(100k-200k))")
        self.stdscr.addstr(10, 3, "Age group average salary")
        self.stdscr.addstr(11, 3, "Employees initials which match A.W.")
        self.stdscr.addstr(12, 3, "Salary and age filter (salary < 150000 OR age > 50)")
        self.stdscr.addstr(13, 3, "Age filter (age > 38 AND age < 72)")
        self.stdscr.addstr(14, 3, "More options")
        self.stdscr.addstr(16, 0, "Choose by entering a number from the list: ", curses.A_STANDOUT)
        while True:
            try:
                choice_menu = int(self.stdscr.getkey())
                break
            except ValueError:
                self.stdscr.addstr(17, 43, "Please enter a number")
                time.sleep(1)
                self.stdscr.clear()
                self.stdscr.refresh()
                self.menu()

        if choice_menu >= 0 and choice_menu <= 9:
            if choice_menu == 0:
                info_list = self.data_init.show_all_employees_info()
                if len(info_list) == 0:
                    self.stdscr.addstr(5, 50, "Empty")
                    self.stdscr.refresh()
                    time.sleep(2)
                    self.menu()
                self.main(tablename="personalInfo", all_employees=info_list, procedure="All employees personal info:")
                self.stdscr.refresh()
                time.sleep(2)
                self.menu()
            if choice_menu == 1:
                self.stdscr.clear()
                self.stdscr.refresh()
                self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
                self.stdscr.addstr(6, 3, "Enter a salary to check who earns more:")
                while True:
                    try:
                        salary_entrie = int(self.stdscr.getstr(6, 45, 15).decode("utf-8"))
                        employees_earn_more=self.data_init.salary_above_input(salary_entrie)
                        if len(employees_earn_more) == 0:
                            self.stdscr.addstr(10, 50, "Empty")
                            self.stdscr.refresh()
                            time.sleep(2)
                        self.main(tablename=self.tablename, all_employees=employees_earn_more, procedure="Salary above input")
                        # self.stdscr.clear()
                        # self.stdscr.refresh()
                        # self.menu()
                        break
                    except:
                        self.stdscr.clear()
                        self.stdscr.refresh()
                        self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
                        self.stdscr.addstr(6, 3, "Please enter a number:")
            if choice_menu == 2:
                self.stdscr.clear()
                self.stdscr.refresh()
                self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
                self.stdscr.addstr(6, 3, "Enter the last name of an employee, to delete it from the data base:")
                surname_entrie = self.stdscr.getstr(6, 72, 15).decode("utf-8")
                if len(self.data_init.find_employee(surname_entrie)) == 0:
                    self.stdscr.addstr(10, 50, "Not found")
                    self.stdscr.refresh()
                    time.sleep(2)
                    self.menu()
                elif len(self.data_init.find_employee(surname_entrie)) == 1:
                    self.main(tablename=self.tablename, all_employees=self.data_init.find_employee(surname_entrie), procedure="Delete employee")
                    self.data_init.delete_employee(surname_entrie)
                    self.stdscr.addstr(10, 50, "Deleted")
                    time.sleep(2)
                    self.menu()
                else:
                    self.stdscr.addstr(10, 50, "Error")
                    self.stdscr.refresh()
                    time.sleep(2)
                    self.menu()

            if choice_menu == 3:
                self.stdscr.clear()
                self.stdscr.refresh()
                self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
                self.stdscr.addstr(6, 3, "Enter age range. From:   ")
                self.stdscr.addstr(7, 3, "Enter age range.   To:   ")
                while True:
                    try:
                        age1 = int(self.stdscr.getstr(6, 26, 3).decode("utf-8"))
                        age2 = int(self.stdscr.getstr(7, 26, 3).decode("utf-8"))
                        age_group = self.data_init.filter_by_age(tablename=self.tablename, age_from=age1, age_to=age2, order_by="last_name", column_entrie= "*")
                        self.main(tablename=self.tablename, all_employees=age_group, procedure="Filter by age")
                        if len(age_group) == 0:
                            self.stdscr.addstr(10, 50, "Empty")
                        self.stdscr.refresh()
                        time.sleep(4)
                        self.menu()
                        break
                    except: 
                        self.stdscr.addstr(10, 50, "Error")
                        self.stdscr.refresh()
                        time.sleep(2)
                        self.menu()
                        break
                self.stdscr.clear()
                self.stdscr.refresh()
                self.menu()

            if choice_menu == 4:
                self.main(tablename=self.tablename, all_employees=self.data_init.specific_filter(), procedure="Specific filter")
                self.stdscr.refresh()
                time.sleep(2)
                self.menu()

            if choice_menu == 5:
                groups = [(18, 19), (20, 29), (30, 39), (40, 49), (50, 59), (60, 69), (70, 79), (80, 89)]
                for i in range(len(self.data_init.age_group())):
                    self.main(tablename=self.tablename, all_employees=self.data_init.age_group()[i], procedure=f"Age group {groups[i]}")
                    self.stdscr.refresh()
                    time.sleep(2)
                    self.main(tablename=self.tablename, all_employees=self.data_init.age_group_avg_salary()[i], procedure=f"Average salary and people count in the group {groups[i]}")
                    self.stdscr.refresh()
                    time.sleep(2)
                self.stdscr.refresh()
                time.sleep(2)
                self.menu()

            if choice_menu == 6:
                self.main(tablename=self.tablename, all_employees=self.data_init.names_aw(), procedure="All employees whos intials are A.W. :")
                self.stdscr.refresh()
                time.sleep(2)
                self.menu()

            if choice_menu == 7:
                self.main(tablename=self.tablename, all_employees=self.data_init.salary_and_age_filter(), procedure="Salary and age filter (salary < 150000 OR age > 50): ")
                self.stdscr.refresh()
                time.sleep(2)
                self.menu()

            if choice_menu == 8:
                self.main(tablename=self.tablename, all_employees=self.data_init.age_filter(), procedure="Age filter (age > 38 AND age < 72): ")
                self.stdscr.refresh()
                time.sleep(2)
                self.menu()

            if choice_menu == 9:
                self.menu2()

        else:
            self.stdscr.clear()
            self.stdscr.refresh()
            self.menu()

    def menu2(self) -> None:
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
        self.stdscr.addstr(3, 0, "Menu(page 2):", curses.A_STANDOUT)
        for i in range(0, 10):
            self.stdscr.addstr(i+5, 0, '{}.'.format(i), curses.A_STANDOUT)
        self.stdscr.addstr(5, 3, "Age group average salary (age > 19 AND age < 43)")
        self.stdscr.addstr(6, 3, "Add column")
        self.stdscr.addstr(7, 3, "Rename column")
        self.stdscr.addstr(8, 3, "Rename table")
        self.stdscr.addstr(9, 3, "Drop column")
        self.stdscr.addstr(10, 3, "Name and surname length in letters comparison of two randomly created tables")
        self.stdscr.addstr(11, 3, "")
        self.stdscr.addstr(12, 3, "")
        self.stdscr.addstr(13, 3, "Back to menu page 1")
        self.stdscr.addstr(14, 3, "Exit")
        self.stdscr.addstr(16, 0, "Choose by entering a number from the list: ", curses.A_STANDOUT)
        while True:
            try:
                choice_menu = int(self.stdscr.getkey())
                break
            except ValueError:
                self.stdscr.addstr(17, 43, "Please enter a number")
                time.sleep(1)
                self.stdscr.clear()
                self.stdscr.refresh()
                self.menu2()

        if choice_menu >= 0 and choice_menu <= 9:
            if choice_menu == 0:
                self.main(tablename=self.tablename, all_employees=self.data_init.age_salary_avarage(), procedure="Age group average salary and people count (age > 19 AND age < 43): ")
                self.stdscr.refresh()
                time.sleep(2)
                self.menu2()

            if choice_menu == 1:
                self.stdscr.clear()
                self.stdscr.refresh()
                self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
                self.stdscr.addstr(6, 3, "Enter a column name you want to add to accessed/creted table: ")
                column_name = self.stdscr.getstr(7, 60, 15).decode("utf-8")
                self.data_init.add_column(column_name=column_name)
                self.stdscr.addstr(8, 45, '{} - column added.'.format(column_name), curses.A_STANDOUT)
                self.stdscr.refresh()
                time.sleep(2)
                self.menu2()

            if choice_menu == 2:
                self.stdscr.refresh()
                time.sleep(2)
                self.menu2()

            if choice_menu == 3:
                self.stdscr.refresh()
                time.sleep(2)
                self.menu2()

        
            if choice_menu == 4:
                self.stdscr.refresh()
                time.sleep(2)
                self.menu2()

        
            if choice_menu == 5:
                self.main(tablename=self.tablename, all_employees=self.data_init.name_lenght(), procedure="Name surname length comparison")
                self.stdscr.refresh()
                time.sleep(2)
                self.menu2()
        
            
            if choice_menu == 6:
                self.stdscr.refresh()
                time.sleep(2)
                self.menu2()

        
            if choice_menu == 7:
                self.stdscr.refresh()
                time.sleep(2)
                self.menu2()

            if choice_menu == 8:
                self.menu()

            if choice_menu == 9:
                self.curses = curses()
                self.curses.endwin()
                        
    def main(self, tablename: str, all_employees: list, procedure: str) -> None:
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
        self.stdscr.addstr(4, 0, 'Created/Accessed database table: {}, Proceedure: {}'.format(tablename, procedure), curses.A_STANDOUT)
        next_line = 5
        next_word = 0
        for i in all_employees:
            self.stdscr.addstr(next_line, next_word, str(i))
            next_word=next_word + len(str(i))
            if next_word > 70:
                next_word = 0
                next_line = next_line + 1
            if next_line > 15:
                self.stdscr.addstr(next_line, 0, 'Show more?: (y/n) ', curses.A_STANDOUT)
                key = self.stdscr.getkey()
                if key == "y":
                    self.stdscr.clear()
                    self.stdscr.refresh()
                    self.stdscr.addstr(0, 75, "Hello, this will generate a random employee list in created/accessed database", curses.A_UNDERLINE)
                    self.stdscr.addstr(4, 0, 'Created/Accessed database table: {}, Proceedure: {}'.format(tablename, procedure), curses.A_STANDOUT)
                    next_line = 5
                    next_word = 0
                    continue
                elif key == "n":
                    self.stdscr.clear()
                    self.stdscr.refresh()
                    self.menu()
                    break
                else:
                    self.stdscr.clear()
                    self.stdscr.refresh()
                    self.menu()
                    break

if __name__ == ("__main__"):    
    console = Console()
    wrapper(console)
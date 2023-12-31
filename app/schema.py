import graphene
import sqlite3

class EmployeeType(graphene.ObjectType):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    department = graphene.String()
    position = graphene.String()
    salary = graphene.Float()

class ProjectType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    start_date = graphene.String()
    end_date = graphene.String()
    manager_id = graphene.Int()

class Query(graphene.ObjectType):
    employees = graphene.List(EmployeeType)
    projects = graphene.List(ProjectType)

    def resolve_employees(self, info):
         with sqlite3.connect('C:\sqlite_database\personal') as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM employees"

            # # Execute the query
            cursor.execute(query)

            # Fetch and print the results
            data = cursor.fetchall()

            employees_data=[]
            for row in data:
                id, first_name, last_name, email, department, position, salary = row
                employees_data.append(EmployeeType(
                id=id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                department=department,
                position=position,
                salary=salary))
            return employees_data
   
        

    def resolve_projects(self, info):
        with sqlite3.connect('C:\sqlite_database\personal') as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM projects"

            # # Execute the query
            cursor.execute(query)

            # Fetch and print the results
            data = cursor.fetchall()

            projects_data = []
            for row in data:
                id, name, start_date, end_date, manager_id = row
                projects_data.append(ProjectType(
                    id=id,
                    name=name,
                    start_date=start_date,
                    end_date=end_date,
                    manager_id=manager_id
                ))
            return projects_data

# Define EmployeeType and ProjectType as you've done before

class CreateEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        department = graphene.String()
        position = graphene.String()
        salary = graphene.Float()

    employee = graphene.Field(EmployeeType)

    def mutate(self, info, first_name, last_name, email, department, position, salary):
        # Connect to the database
        with sqlite3.connect('C:\sqlite_database\personal') as conn:
            cursor = conn.cursor()

            # Insert a new employee into the database
            query = """
                INSERT INTO employees (first_name, last_name, email, department, position, salary)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (first_name, last_name, email, department, position, salary))
            conn.commit()

            new_employee_id = cursor.lastrowid

            # Return the newly created employee
            return CreateEmployee(employee=EmployeeType(
                id=new_employee_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                department=department,
                position=position,
                salary=salary
            ))
class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()


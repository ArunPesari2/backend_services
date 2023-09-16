import graphene
from flask import Flask
from flask_graphql import GraphQLView
from .schema import Query

app = Flask(__name__)

# Define the GraphQL schema
schemas = graphene.Schema(query=Query)

# Add GraphQL route
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schemas, graphiql=True)
)

print("app object has been created")


# import sqlite3
# from flask import Flask, jsonify, render_template
# import graphene
# from flask_graphql import GraphQLView
# # from graphql.execution.base import GraphQLResolveInfo  # Correct import


# class EmployeeType(graphene.ObjectType):
#     id = graphene.Int()
#     first_name = graphene.String()
#     last_name = graphene.String()
#     email = graphene.String()
#     department = graphene.String()
#     position = graphene.String()
#     salary = graphene.Float()

# class ProjectType(graphene.ObjectType):
#     id = graphene.Int()
#     name = graphene.String()
#     start_date = graphene.String()
#     end_date = graphene.String()
#     manager_id = graphene.Int()

# class Query(graphene.ObjectType):
#     employees = graphene.List(EmployeeType)
#     projects = graphene.List(ProjectType)

#     def resolve_employees(self, info):
#          with sqlite3.connect('C:\sqlite_database\personal') as conn:
#             cursor = conn.cursor()
#             query = "SELECT * FROM employees"

#             # # Execute the query
#             cursor.execute(query)

#             # Fetch and print the results
#             data = cursor.fetchall()

#             employees_data=[]
#             for row in data:
#                 id, first_name, last_name, email, department, position, salary = row
#                 employees_data.append(EmployeeType(
#                 id=id,
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 department=department,
#                 position=position,
#                 salary=salary))
#             return employees_data
   
        

#     def resolve_projects(self, info):
#         with sqlite3.connect('C:\sqlite_database\personal') as conn:
#             cursor = conn.cursor()
#             query = "SELECT * FROM projects"

#             # # Execute the query
#             cursor.execute(query)

#             # Fetch and print the results
#             data = cursor.fetchall()

#             projects_data = []
#             for row in data:
#                 id, name, start_date, end_date, manager_id = row
#                 projects_data.append(ProjectType(
#                     id=id,
#                     name=name,
#                     start_date=start_date,
#                     end_date=end_date,
#                     manager_id=manager_id
#                 ))
#             return projects_data

# schema = graphene.Schema(query=Query)

# app = Flask('graphql')
# app.add_url_rule(
#     '/graphql',
#     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
# )

# if __name__ == '__main__':
#     app.run()
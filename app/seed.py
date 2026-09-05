from models.department import Department
from models.employee import Employee
from models.__init__ import CURSOR
from faker import Faker 
import random


fake=Faker()
# Employee.drop_table()
# Department.drop_table()
# Department.create_table()
# Employee.create_table()



# departments=[]
# for i in range(20):
#     department=Department.create(
#         name=fake.unique.name(),
#         location=fake.unique.address()
#     )
#     departments.append(department)
# employees=[]
# for department in departments:
#     for i in range(random.randint(1,3)):
#         employee=Employee.create(
#             name=fake.unique.name(),
#             job_title=fake.word(),
#             department_id=department.id
#         )
#         employees.append(employee)


# print(Department.get_all())
# print(".................")
# print(Department.find_by_id(2))
# print(Department.find_by_name("Dakota Bell"))
# sql="SELECT * FROM departments WHERE id=?;"
# dep1=CURSOR.execute(sql,(1,)).fetchone()
# print(dep1)
# print(dep1.employees())
dep1=Department.find_by_id(1)
print(dep1)
print(dep1.employees())
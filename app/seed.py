from models.department import Department
from models.__init__ import CURSOR
from faker import Faker 


# fake=Faker()
# Department.drop_table()
# Department.create_table()

# departments=[]
# for i in range(20):
#     department=Department.create(
#         name=fake.unique.name(),
#         location=fake.unique.address()
#     )
#     departments.append(department)

print(Department.get_all())
print(".................")
print(Department.find_by_id(2))
print(Department.find_by_name("Dakota Bell"))
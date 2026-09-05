from .__init__ import CURSOR,CONN 
from .department import Department
class Employee:
    all={}
    def __init__(self,name,job_title,department_id,id=None):
        self.id=id
        self.name=name
        self.job_title=job_title
        self.department_id=department_id
    def __repr__(self):
        return(
            f"<Employee {self.id}: {self.name}, {self.job_title}, "+
            f"Department ID {self.department_id}>"
        )
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value):
            self._name=value
        else:
            raise ValueError("Name must be a non empty string")
    @property
    def job_title(self):
        return self._job_title
    @job_title.setter
    def job_title(self,value):
        if isinstance(value,str) and len(value):
            self._job_title=value
        else:
            raise ValueError("Job title must be a non empty string")
    @property
    def department_id(self):
        return self._department_id
    @department_id.setter
    def department_id(self,value):
        if type(value) is int and Department.find_by_id(value):
            self._department_id=value
        else:
            raise ValueError("department_id must reference a deprtment in database")
    @classmethod
    def create_table(cls):
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        job_title TEXT,
        department_id INTEGER,
        FOREIGN KEY(department_id) REFERENCES departments(id)
        );
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql="DROP TABLE IF EXISTS employees;"
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql="""
        INSERT INTO employees(name,job_title,department_id)
        VALUES(?,?,?);
        """
        CURSOR.execute(sql,(self.name,self.job_title,self.department_id))
        CONN.commit()
        self.id=CURSOR.lastrowid
        type(self).all[self.id]=self
    @classmethod
    def create(cls,name,job_title,department_id):
        employee=cls(name,job_title,department_id)
        employee.save()
        return employee
    def update(self):
        sql="""
        UPDATE employees 
        SET name=?,job_title=?,department_id=?
        WHERE id=?;
        """
        CURSOR.execute(sql,(self.name,self.job_title,self.department_id,self.id))
        CONN.commit()
    def delete(self):
        sql="DELETE FROM employees WHERE id=?;"
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id=None



    @classmethod
    def instance_from_db(cls,row):
        employee=cls.all.get(row[0])
        if employee:
            employee.name=row[1]
            employee.job_title=row[2]
            employee.department_id=row[3]
        else:
            employee=cls(row[1],row[2],row[3])
            employee.id=row[0]
            cls.all[employee.id]=employee
        return employee
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM employees;"
        rows=CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    @classmethod
    def find_by_id(cls,id):
        sql="SELECT * FROM employees WHERE id=?;"
        row=CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_name(cls,name):
        sql="SELECT * FROM employees WHERE name is?;"
        row=CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None































# Employee.drop_table()
# Employee.create_table()

# john=Employee.create("John","Manager",1)
# doe=Employee("Doe","IT Consuultant",2)
# doe.save()
# doe.job_title="IT Consultant"
# doe.update()
# kaniaru=Employee.create("Kaniaru","Technician",1)
# kaniaru.delete()
# guido=Employee.create("Guido","Creator",1)
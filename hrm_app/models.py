from django.db import models
from user_auth.models import User

# Create your models here.
class Department (models.Model) :
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_dept', null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='department_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='department_updated_by', null=True,blank=True)

class Rank(models.Model):
    title = models.CharField(max_length=50, unique=True)  # e.g., "Junior", "Senior"
    level = models.PositiveIntegerField()  # e.g., 1 = lowest, 5 = highest
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rank', null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='rank_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rank_updated_by', null=True,blank=True)

    def __str__(self):
        return self.title
    
class Manager(models.Model):
    office_number = models.CharField(max_length=20, blank=True, null=True)
    appointed_date = models.DateField()
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_manager', null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='manager_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_updated_by', null=True,blank=True)

    def __str__(self):
        return f"Manager: {self.employee.first_name} {self.employee.last_name}" 
    
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees',null =True, blank=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, related_name='ranks',null =True, blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='managers',null =True, blank=True)
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_employee', null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='employee_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_updated_by', null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    
       
    
class Salary(models.Model):
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    effective_from = models.DateField()
    effective_to = models.DateField(blank=True, null=True)  # null = still active
    is_active = models.BooleanField(default=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_salary', null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='salary_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salary_updated_by', null=True,blank=True)


    def __str__(self):
        return f"{self.employee} - {self.base_salary}"
    


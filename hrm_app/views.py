from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from permissions.decorator import permission_required
from utils.base_authentication import JWTAuthentication
from .hrm_controller import DepartmentController, EmployeeController, ManagerController, RankController, SalaryController



department_controller = DepartmentController()
rank_controller =RankController()
manager_controller =ManagerController()
employee_controller= EmployeeController()
salary_controller=SalaryController()



class DepartmentViews(ModelViewSet):
     authentication_classes = [JWTAuthentication]

     @permission_required(['create_department'])
      
     def post_department(self,request):
       return department_controller.create(request)
     
     @permission_required(['read_department'])
     
     
     def get_department(self,request):
       return department_controller.get_department(request)
     
     @permission_required(['update_department'])
     
     
     def update_department(self,request):

        return department_controller.update_department(request)
     @permission_required(['delete_department'])
     
     
     def delete_department(self,request):
        return department_controller.delete_department(request)
     



class RankViews(ModelViewSet):
     authentication_classes = [JWTAuthentication]


     def post_rank(self,request):
       return rank_controller.create(request)
     
     def get_rank(self,request):
       return rank_controller.get_rank(request)
     
     def update_rank(self,request):
        return rank_controller.update_rank(request)
     
     def delete_rank(self,request):
        return rank_controller.delete_rank(request)    
      
     


class ManagerViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]
  

    def post_manager(self, request):
        return manager_controller.create(request)

    def get_manager(self, request):
        return manager_controller.get_manager(request)

    def update_manager(self, request):
        return manager_controller.update_manager(request)

    def delete_manager(self, request):
        return manager_controller.delete_manager(request)
    


class EmployeeViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    
    @permission_required(['create_employee'])
    def create(self, request):
        return employee_controller.create(request)
    @permission_required(['read_employee'])
    def list(self, request):
        return employee_controller.get_employee(request)
    @permission_required(['update_employee'])
    def update(self, request):
        return employee_controller.update_employee(request)
    @permission_required(['delete_employee'])
    def destroy(self, request):
        return employee_controller.delete_employee(request)    
    


class SalaryViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    

    def post_salary(self, request):
        return salary_controller.create(request)

    def get_salary(self, request):
        return salary_controller.get_salary(request)

    def update_salary(self, request):
        return salary_controller.update_salary(request)

    def delete_salary(self, request):
        return salary_controller.delete_salary(request)
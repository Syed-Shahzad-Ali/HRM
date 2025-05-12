from django.shortcuts import render
from .models import Make , Vehicle
from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import MakeSerializer,VehicleSerializer
from utils.base_authentication import JWTAuthentication

from .controller import MakeController, VehicleController



department = DepartmentController()
rank =RankController()
manager =ManagerDepartmentController()
employee= EmployeeController()
salary=SalaryController()



class DepartmentViews(ModelViewSet):
     authentication_classes = [JWTAuthentication]


     def post_department(self,request):
       return department_controller.created(request)
     
     def get_department(self,request):
       return department_controller.get_department(request)
     
     def update_department(self,request):

        return department_controller.update_department(request)
     
     def delete_department(self,request):
        return department_controller.delete_department(request)
     



class RankViews(ModelViewSet):
     authentication_classes = [JWTAuthentication]


     def post_rank(self,request):
       return rank_controller.created(request)
     
     def get_rank(self,request):
       return rank_controller.get_rank(request)
     
     def update_rank(self,request):
        return rank_controller.update_rank(request)
     
     def delete_rank(self,request):
        return rank_controller.delete_rank(request)    
      
     


class ManagerViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]
  

    def post_manager(self, request):
        return manager_controller.created(request)

    def get_manager(self, request):
        return manager_controller.get_manager(request)

    def update_manager(self, request):
        return manager_controller.update_manager(request)

    def delete_manager(self, request):
        return manager_controller.delete_manager(request)
    


class EmployeeViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    

    def post_employee(self, request):
        return employee_controller.created(request)

    def get_employee(self, request):
        return employee_controller.get_employee(request)

    def update_employee(self, request):
        return employee_controller.update_employee(request)

    def delete_employee(self, request):
        return employee_controller.delete_employee(request)    
    


class SalaryViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    

    def post_salary(self, request):
        return salary_controller.created(request)

    def get_salary(self, request):
        return salary_controller.get_salary(request)

    def update_salary(self, request):
        return salary_controller.update_salary(request)

    def delete_salary(self, request):
        return salary_controller.delete_salary(request)
from django import forms
from django_filters import DateFilter, CharFilter, FilterSet
from .models import *


class EmployeeFilter(FilterSet):
    id=CharFilter(field_name='id')
    name=CharFilter(field_name='name', Lookup_expr='icontains')
    position=CharFilter(field_name='position', Lookup_expr='icontains')
    salary=CharFilter(field_name='salary')
    date_from=DateFilter(field_name='created_at', Lookup_expr='gte')
    date_to=DateFilter(field_name='created_at', Lookup_expr='lte')


    class Meta:
        model = Employee
        fields  = '__all__'

   

class DepartmentFilter(FilterSet):
    id = CharFilter(field_name='id')
    date_from=DateFilter(field_name='created_at', Lookup_expr='gte')
    date_to=DateFilter(field_name='created_at', Lookup_expr='lte')
    dept_name=CharFilter(field_name='dept_name', Lookup_expr='icontains')
    dept_location=CharFilter(field_name='dept_location', Lookup_expr='icontains')
    
    class Meta:
        model = Employee
        fields  = '__all__'
    

class SalaryFilter(FilterSet):

    id = CharFilter(field_name='id')
    date_from=DateFilter(field_name='created_at', Lookup_expr='gte')
    date_to=DateFilter(field_name='created_at', Lookup_expr='lte')
    net_salary= CharFilter(field_name='net_salary')
    allowances= CharFilter(field_name='allowances')
    class Meta:
        model = Employee
        fields  = '__all__'



class RankFilter(FilterSet):

    id = CharFilter(field_name='id')
    date_from=DateFilter(field_name='created_at', Lookup_expr='gte')
    date_to=DateFilter(field_name='created_at', Lookup_expr='lte')
    rank_title=CharFilter(field_name='rank_title', Lookup_expr='icontains')
    class Meta:
        model = Employee
        fields  = '__all__'     




class ManagerFilter(FilterSet):

    id = CharFilter(field_name='id')
    date_from=DateFilter(field_name='created_at', Lookup_expr='gte')
    date_to=DateFilter(field_name='created_at', Lookup_expr='lte')
    status=CharFilter(field_name='status', Lookup_expr='icontains')
    class Meta:
        model = Employee
        fields  = '__all__'                   



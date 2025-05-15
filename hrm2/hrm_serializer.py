from rest_framework import serializers
from hrm_app.models import Manager, Department, Employee, Rank, Salary
from user_auth.user_serializer import UserListingSerializer



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Employee
        fields= '__all__'


    def to_representation(self, instance):
     data = super().to_representation(instance)

     data.pop('department',None)

     data['department_name']=isinstance.department.name if instance.department else None
     
     data['created_by']=UserListingSerializer(instance.created_by).data if instance.created_by else None
     data['updated_by']=UserListingSerializer(instance.updated_by).data if instance.updated_by else None

     return data
     
     
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Department
        fields= '__all__'


    def to_representation(self, instance):
     data = super().to_representation(instance) 
     data['created_by']=UserListingSerializer(instance.created_by).data if instance.created_by else None
     data['updated_by']=UserListingSerializer(instance.updated_by).data if instance.updated_by else None

     return data     
    

     
class SalarySerializer(serializers.ModelSerializer):
    class Meta :
        model = Salary
        fields= '__all__'


    def to_representation(self, instance):
     data = super().to_representation(instance) 
     data['created_by']=UserListingSerializer(instance.created_by).data if instance.created_by else None
     data['updated_by']=UserListingSerializer(instance.updated_by).data if instance.updated_by else None

     return data         
    



class RankSerializer(serializers.ModelSerializer):
    class Meta :
        model = Rank
        fields= '__all__'


    def to_representation(self, instance):
     data = super().to_representation(instance) 
     data['created_by']=UserListingSerializer(instance.created_by).data if instance.created_by else None
     data['updated_by']=UserListingSerializer(instance.updated_by).data if instance.updated_by else None

     return data             
    



class ManagerSerializer(serializers.ModelSerializer):
    class Meta :
        model =Manager
        fields= '__all__'


    def to_representation(self, instance):
     data = super().to_representation(instance) 
     data['created_by']=UserListingSerializer(instance.created_by).data if instance.created_by else None
     data['updated_by']=UserListingSerializer(instance.updated_by).data if instance.updated_by else None

     return data                 
    



class RankSerializerlisting(serializers.ModelSerializer):
   class Meta:
      model = Rank
      fields = ['id','rank_title']
          
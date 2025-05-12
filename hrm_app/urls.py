from django.urls import path
from . views import DepartmentViews, RankViews, ManagerViews, EmployeeViews, SalaryViews

urlpatterns=[
        path('department', DepartmentViews.as_view({"get":"get_department",
                                        "post":"post_department",
                                        "patch":"update_department",
                                        "delete":"delete_department"})),
    

        path('rank', RankViews.as_view({"get":"get_rank",
                                                "post":"post_rank",
                                                "patch":"update_rank",
                                                "delete":"delete_rank" })),


        path('manager', ManagerViews.as_view({"get":"get_manager",
                                                "post":"post_manager",
                                                "patch":"update_manager",
                                                "delete":"delete_manager" })),
        

        path('employee', EmployeeViews.as_view({"get":"get_employee",
                                                "post":"post_employee",
                                                "patch":"update_employee",
                                                "delete":"delete_employee" })),

        path('salary', SalaryViews.as_view({"get":"get_salary",
                                                "post":"post_salary",
                                                "patch":"update_salary",
                                                "delete":"delete_salary" }))
]
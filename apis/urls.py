from django.urls import path
from . import views

urlpatterns = [
    path('<str:n>/<str:p>/',views.Login.as_view()),
    path('ems/',views.EmployeeList.as_view()),
    path('ems/<int:pk>',views.EmployeeDetail.as_view()),
    # path('ems/manager/<int:pk>',views.ManagerDetail.as_view()),
    path('ems/attendance/<int:pk>/',views.AttendanceDetail.as_view()),
    path('/ems/leave/',views.LeaveList.as_view()),
    path('ems/leave/<int:pk>/',views.LeaveDetail.as_view()),
    path('ems/leave/request/<int:pk>/',views.LeavePutDelete.as_view()),
]

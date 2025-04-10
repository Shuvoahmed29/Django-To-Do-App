from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),

    path('',views.home,name='home'),
    path('create/',views.task_create,name='create'),
    path('task/<int:task_id>/',views.task_detail,name='task_details'),
    path('delete/<int:task_id>/',views.task_delete,name='delete'),

    path('logout/',views.user_logout,name='logout'),
    path('update/<int:task_id>/',views.task_update,name='update'),
]

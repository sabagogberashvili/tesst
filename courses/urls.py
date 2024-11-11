from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/update/<int:id>/', views.course_update, name='course_update'),
    path('course/delete/<int:id>/', views.course_delete, name='course_delete'),
]

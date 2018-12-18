from django.urls import path
#from .views import CourseDetailView, CourseCreateView
from . import views

urlpatterns = [
    path('', views.home, name='course-home'),
    path('about/', views.about, name='course-about'),
    path('search/', views.search, name='course-search'),
    path('calculate/', views.calculate, name='course-calculate'),
    path('addCourse/', views.addCourse, name='course-add'),
    #path('course/new/', CourseDetailView.as_view(), name='course-add'),
    #path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail')
]
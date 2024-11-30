"""
URL configuration for dbms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('userreg/', views.userreg, name='userreg'),
    path('insertevent/', views.insertevent, name='insertevent'),
    path('viewusers/', views.viewusers, name='viewusers'),
    path('deleteprofile/<str:id>', views.deleteprofile,name='deleteprofile'),
    path('editprofile/<str:id>', views.editprofile, name='editprofile'),
    path('updateprofile/<str:id>', views.updateprofile, name='updateprofile'),
    path('viewdept/', views.viewdept, name='viewdept'),
    path('deletedept/<int:id>', views.deletedept,name='deletedept'),
    path('viewvenue/', views.viewvenue, name='viewvenue'),
    path('register/', views.register, name='register'),
    path('update_register/<int:pk>/', views.update_register, name='update_register'),
    path('ajax/load-contests/', views.load_contests, name='ajax_load_contests'), # AJAX
    path('view_participants/', views.view_participants, name='view_participants'),
    path('sponser_registration/', views.sponser_registration, name='sponser_registration'),
    path('view_sponsers/', views.view_sponsers, name='view_sponsers'),
    path('update_sponsers/<int:pk>/', views.update_sponsers, name='update_sponsers'),
    path('delete_participants/<int:id>', views.delete_participants, name='delete_participants'),
    path('delete_sponsers/<int:id>', views.delete_sponsers, name='delete_sponsers'),
    path('volunteer_registration/', views.volunteer_registration, name='volunteer_registration'),
    path('view_volunteers/', views.view_volunteers, name='view_volunteers'),
    path('update_volunteer/<int:pk>/', views.update_volunteer, name='update_volunteer'),
    path('delete_volunteers/<int:id>', views.delete_volunteers, name='delete_volunteers'),
    path('contests_view', views.contests_view,name='contests_view')
    #path('update_participant/<str:id>', views.updateprofile, name='update_participant'),
    #path('edit_participant/<str:id>', views.edit_participant, name='edit_participant')
]



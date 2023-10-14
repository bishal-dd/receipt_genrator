from django.urls import path
from . import views


app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('save_data/', views.save_data, name="save_data")
]

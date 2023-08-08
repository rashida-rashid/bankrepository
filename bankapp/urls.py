from bankapp import views
from django.urls import path

app_name='bank'
urlpatterns=[
    path('',views.display,name='display'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('form_view',views.form_view,name='form_view'),

]
from django.urls import path

from . import views

app_name = 'PoC'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('sysserialno/<str:sysserialno>/', views.serial_detail, name='serial_detail'),
    path('line_detail/<str:line>/<str:stage>/<int:inSLA>', views.line_detail, name='line_detail'),

]
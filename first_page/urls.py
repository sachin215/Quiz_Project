from django.urls import path
from . import views
app_name = 'first_page'
urlpatterns = [
    
   path('select/', views.select_Category, name='select_category'),
    path('quiz/<str:category>/', views.quiz_view, name='Quiz'),
    path('Welcome_Page/',views.welcome_page,name='welcome'),
   
]
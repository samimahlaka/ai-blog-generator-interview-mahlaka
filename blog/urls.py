from blog import views
from django.urls import path

urlpatterns = [
   path('generate_blog/', views.generate_blog),
]




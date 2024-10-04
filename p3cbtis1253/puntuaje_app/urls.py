from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name= 'index'),
    path("valentina/",views.valentina, name = "valentina"),
    path("quincy/",views.quincy, name = "quincy")
]

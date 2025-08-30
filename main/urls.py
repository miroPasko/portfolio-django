from django.urls import path
from .views import indexPageView, mlExamplePageView
 
urlpatterns = [
	path("", indexPageView, name="index"),
    path("ml-example", mlExamplePageView, name="ml-example")
] 

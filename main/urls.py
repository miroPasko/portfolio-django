from django.urls import path
from .views import indexPageView, mlExamplePageView, linearRegressionView
 
urlpatterns = [
	path("", indexPageView, name="index"),
    path("ml-example", mlExamplePageView, name="ml-example"),
    path("ml-example/linear-regression", linearRegressionView, name="ml-linear-regression")
] 

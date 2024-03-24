from django.urls import path

from . import views

urlpatterns = [

	path('', views.social, name="social"),
	path('page/', views.page, name="page"),

]
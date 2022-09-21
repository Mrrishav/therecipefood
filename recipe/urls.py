from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path("post/<int:id>/",views.post,name="post"),
    path('detail/', views.search, name='search'),
    path('add/', views.create_item, name='create_item'),
    path('about/', views.about, name='about'),
    path("update/<int:id>/",views.update,name="update"),
    path("delete/<int:id>/",views.delete,name="delete")
]
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("sum/", views.sum),
    path("add/", views.add),
    # path("show_items/<int:id>", views.show_items),
    path("show_items/<int:id>/", views.show_items),
    path("add_entry/", views.addEntry),
    path("create/", views.create_list),
    path("view/", views.view_list)
]



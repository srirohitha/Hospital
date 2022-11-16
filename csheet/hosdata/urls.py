from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('pd/',views.patient_list),
    path('pd/<int:pat_id>',views.patient_list_id),
    path('ai/',views.admission_list),
    path('ai/<int:id>',views.admission_list_id),
    path('count/<int:n>',views.patcount)
]

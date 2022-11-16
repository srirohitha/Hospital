from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home),
    path('pi/',views.casesheet_list),
    path('pi/<int:id>',views.cs_detail),
    path('fpi/',views.finalcasesheet_list),
    path('fpi/<int:id>',views.finalcs_detail)
]

from django.contrib import admin
from django.urls import path
from companies.views import CompanyInfo, CompanyDetail

urlpatterns = [
    path('company-info/', CompanyInfo.as_view(), name='company-info'),
    path('company-detail/<int:pk>/', CompanyDetail.as_view(), name='company-detail')
]
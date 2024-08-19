from django.contrib import admin
from django.urls import path
from assets.views import AssetInfo, AssetDetail

urlpatterns = [
    path('asset-info/', AssetInfo.as_view(), name='asset-info'),
    path('asset-detail/<int:pk>/', AssetDetail.as_view(), name='asset-detail'),
]

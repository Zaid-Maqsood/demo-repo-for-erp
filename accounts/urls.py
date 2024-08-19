from django.urls import path, include
from accounts.views import UserInfo, UserDetail

urlpatterns = [
    path('user-info/', UserInfo.as_view(), name='user-info'),
    path('user-detail/<int:pk>', UserDetail.as_view(), name='user-detail')
]
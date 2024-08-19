from django.urls import path
from teams.views import TeamInfo, TeamDetail

urlpatterns = [
    path('team-info/', TeamInfo.as_view(), name='team-info'),
    path('team-detail/<int:pk>/', TeamDetail.as_view(), name='team-detail')
]


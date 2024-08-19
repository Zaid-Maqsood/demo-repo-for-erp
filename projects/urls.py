from django.urls import path
from projects.views import ProjectInfo, ProjectDetail

urlpatterns = [
    path('project-info/', ProjectInfo.as_view(), name='project-info'),
    path('project-detail/<int:pk>/', ProjectDetail.as_view(), name='project-detail')
]


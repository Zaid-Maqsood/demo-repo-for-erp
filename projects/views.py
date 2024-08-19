from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectInfo(APIView):
    def get(self, request):
        data = Project.objects.all()
        serializer = ProjectSerializer(data, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = ProjectSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProjectDetail(APIView):
    def get(self, request, pk):
        data = Project.objects.filter(id=pk).first()
        serializer = ProjectSerializer(data)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        data = Project.objects.filter(id=pk).first()
        serializer = ProjectSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        data  = Project.objects.filter(id=pk).first()
        serializer = ProjectSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        data = Project.objects.filter(id=pk).first()
        if data:
            data.delete()
            return Response(status=204)
        return Response(data="could not delete", status=400)





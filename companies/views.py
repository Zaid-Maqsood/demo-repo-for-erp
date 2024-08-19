from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyInfo(APIView):
    def get(self, request):
        data = Company.objects.all()
        serializer = CompanySerializer(data, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CompanyDetail(APIView):
    def get(self, request, pk):
        data = Company.objects.filter(id=pk).first()
        serializer = CompanySerializer(data)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        data = Company.objects.filter(id=pk).first()
        serializer = CompanySerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        data = Company.objects.filter(id=pk).first()
        serializer = CompanySerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        data = Company.objects.filter(id=pk).first()
        if data:
            data.delete()
            return Response(status=204)
        return Response(data="data not found", status=400)


















#
# @api_view(['GET', 'POST'])
# def company_info(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['PUT', 'PATCH', 'DELETE', 'GET'])
# def company_detail(request, pk):
#     try:
#         company = Company.objects.get(id=pk)
#     except Company.DoesNotExist:
#         return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CompanySerializer(company)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = CompanySerializer(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'PATCH':
#         serializer = CompanySerializer(company, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         company.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







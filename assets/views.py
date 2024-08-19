from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from assets.models import Asset
from assets.serializers import AssetSerializer


class AssetInfo(APIView):
    def get(self, request):
        data = Asset.objects.all()
        serializer = AssetSerializer(data, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = AssetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)


class AssetDetail(APIView):
    def get(self, request, pk):
        data = Asset.objects.get(id=pk)
        serializer = AssetSerializer(data)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        data = Asset.objects.get(id=pk)
        serializer = AssetSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        data = Asset.objects.get(id=pk)
        serializer = AssetSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        data = Asset.objects.delete(id=pk)
        data.delete()
        return Response(status=204)




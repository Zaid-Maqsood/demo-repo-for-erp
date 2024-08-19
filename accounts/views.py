from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import UserSerializer


class UserInfo(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class UserDetail(APIView):
    def get(self, request, pk):
        data = User.objects.filter(id=pk).first()
        serializer = UserSerializer(data)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        data = User.objects.filter(id=pk).first()
        serializer = UserSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        data = User.objects.filter(id=pk).first()
        serializer = UserSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        data = User.objects.filter(id=pk).first()
        if data:
            data.delete()
            return Response(status=204)
        return Response(data="could not delete", status=400)






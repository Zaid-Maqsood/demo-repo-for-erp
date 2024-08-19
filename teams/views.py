from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from teams.models import Team
from companies.models import Company
from .serializers import TeamSerializer


class TeamInfo(APIView):
    def get(self, request):
        data = Team.objects.all()
        serializer = TeamSerializer(data, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = TeamSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TeamDetail(APIView):
    def get(self, request, pk):
        data = Team.objects.filter(id=pk).first()
        serializer = TeamSerializer(data)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        data = Team.objects.filter(id=pk).first()
        serializer = TeamSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        data = Team.objects.filter(id=pk).first()
        serializer = TeamSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        data = Team.objects.filter(id=pk).first()
        if data:
            data.delete()
            return Response(status=204)
        return Response(data="could not delete", status=400)
























# class TeamInfo(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Team.objects.all()
#         serializer = TeamSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         team = Team.objects.filter(pk=pk).first()
#         if team:
#             serializer = TeamSerializer(team)
#             return Response(serializer.data)
#         else:
#             return Response(data="No data found", status=status.HTTP_404_NOT_FOUND)
#
#     def create(self, request):
#         # company_id = request.data.get("company")
#         # if company_id:
#         #     company = Company.objects.filter(id=company_id).first()
#         #     if company:
#         #         team =  Team.objects.create(team_name=request.data.get("team_name"), company=company)
#         #
#         #         data = {
#         #             "team_name": request.data.get("team_name"),
#         #             "company": company_id
#         #         }
#             serializer = TeamSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def update(self, request, pk=None):
#         data = Team.objects.filter(pk=pk).first()
#         serializer = TeamSerializer(data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         data = Team.objects.filter(pk=pk).first()
#         if data:
#             data.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(data="Action cannot be performed", status=400)


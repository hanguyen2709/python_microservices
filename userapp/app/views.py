
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import CoreUsers
from .serializers import CoreUsersSerializer


class UserViewSet(viewsets.ViewSet):

    def list(self, request): #/api/employee
        employees = CoreUsers.objects.all()
        serializer = CoreUsersSerializer(employees, many = True)
        return Response(serializer.data)

    def create(self, request): #/api/employee
        serializer = CoreUsersSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #/api/employee/<str:id>
        employee = CoreUsers.objects.get(id = pk)
        serializer = CoreUsersSerializer(employee)
        return Response(serializer.data)

    def update(self, request, pk = None):
        employee = CoreUsers.objects.get(id=pk)
        serializer = CoreUsersSerializer(instance = employee, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk = None):
        employee = CoreUsers.objects.get(id = pk)
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)





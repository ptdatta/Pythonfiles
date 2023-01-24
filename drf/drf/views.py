from urllib import response
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import StudentSeriallizers
from drfapp.models import Student

class TesView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request,*args,**kwargs):
       qs=Student.objects.all()
       student1=qs.first()
       serializer=StudentSeriallizers(student1)
       return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=StudentSeriallizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
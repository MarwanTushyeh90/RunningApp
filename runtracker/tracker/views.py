from django.contrib.auth import get_user_model
from rest_framework.views import exception_handler
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.shortcuts import render
from .RunningSessionManager import RunningSessionManager
from rest_framework import authentication, permissions, viewsets
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route

from rest_framework import viewsets

from .models import RunningSession
from .serializers import RunSessionSerializer,UserSerializer
User = get_user_model()


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""
    
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,    
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
 


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    
 


class RunSessionViewSet(viewsets.ModelViewSet):

    """API endpoint for listing and creating sprints."""
    queryset = RunningSession.objects.order_by('createdDate')
    serializer_class = RunSessionSerializer
    
    def list(self, request):
        try:
            queryset = RunningSession.objects.filter(name=request.user)
            serializer = serializer_class = RunSessionSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('An Error Has Occured...Please Try Again Later', status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    def retrieve(self, request, pk=None):
        try:
            queryset = RunningSession.objects.filter(name=request.user)
            serializer = serializer_class = RunSessionSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('An Error Has Occured...Please Try Again Later', status = status.HTTP_500_INTERNAL_SERVER_ERROR)        
    @detail_route(methods=['get'])
    def Distance(self, request, pk=None):
        try: 
            print(request.user)     
            return Response({'Distance' : RunningSessionManager.GetSessionDistance(request.user.id,pk)}, status = status.HTTP_200_OK)
        except:
            return Response('An Error Has Occured...Please Try Again Later', status = status.HTTP_500_INTERNAL_SERVER_ERROR)    
            
    @detail_route(methods=['get'])
    def Speed(self, request, pk=None):
        try:       
            return Response({'Speed' : RunningSessionManager.GetSessionSpeed(request.user.id,pk)}, status = status.HTTP_200_OK)
        except:
            return Response('An Error Has Occured...Please Try Again Later', status = status.HTTP_500_INTERNAL_SERVER_ERROR)    
                    
    @list_route(methods=['get'])
    def TotalSpeed(self, request):
        try:
            return Response({'Speed' :  RunningSessionManager.GetTotalSpeed(request.user.id)}, status = status.HTTP_200_OK)
        except:
            return Response('An Error Has Occured...Please Try Again Later', status = status.HTTP_500_INTERNAL_SERVER_ERROR) 
    @list_route(methods=['get'])
    def TotalDistance(self, request):
        try:
            return Response({'Distance' : RunningSessionManager.GetTotalDistance(request.user.id) }, status = status.HTTP_200_OK)
        except:
            return Response('An Error Has Occured...Please Try Again Later', status = status.HTTP_500_INTERNAL_SERVER_ERROR)        


        
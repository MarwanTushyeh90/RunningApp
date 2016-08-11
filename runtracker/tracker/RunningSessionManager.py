from rest_framework.views import exception_handler
from django.db.models import Sum

from rest_framework import viewsets

from .models import RunningSession

class RunningSessionManager():
    """API endpoint for listing and creating sprints."""
    
    def GetSessionDistance( user,pk=None):
        distance = RunningSession.objects.filter(name=user).filter(id =pk).aggregate(Sum('miles'))
        return distance.get('miles__sum')
        
    def GetSessionSpeed(user,pk=None):
         try:
             distance = RunningSession.objects.filter(name=user).filter(id =pk).aggregate(Sum('miles'))
             duration = RunningSession.objects.filter(name=user).filter(id =pk).aggregate(Sum('duration')) 
             return  distance.get('miles__sum')/duration.get('duration__sum')
         except ZeroDivisionError:    
             return 0

    def GetTotalSpeed(user):
       try:
            distance = RunningSession.objects.filter(name=user).aggregate(Sum('miles'))
            duration = RunningSession.objects.filter(name=user).aggregate(Sum('duration')) 
            return distance.get('miles__sum')/duration.get('duration__sum')
       except ZeroDivisionError:    
               return 0
    def GetTotalDistance(user):
        return RunningSession.objects.filter(name=user).aggregate(Sum('miles'))
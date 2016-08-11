from django.test import TestCase
from .models import RunningSession
from django.conf import settings
from django.contrib.auth.models import User
from .RunningSessionManager import RunningSessionManager

class SessiontCase(TestCase):
    def setUp(self):  
        user =User()
        user.name="TestRun"
        user.id=1
        user.save()
        RunningSession.objects.create(id="0", name=user, miles=12, duration =3)
        RunningSession.objects.create(id="1", name=user, miles=8, duration =6)
        RunningSession.objects.create(id="2", name=user, miles=4, duration =9)
        RunningSession.objects.create(id="3", name=user, miles=2.5, duration =2.8)
        RunningSession.objects.create(id="4", name=user, miles=8, duration =0)

    def test_Session_calculatingTotalSessionSpeed(self):
        self.assertEqual(RunningSessionManager.GetTotalSpeed(1),1.658653846153846)

    def test_Session_calculatingSessionSpeed(self):
        self.assertEqual(RunningSessionManager.GetSessionSpeed(1,0), 4)
        
    def test_Sesssson_TestingDevideByZero(self):
        self.assertEqual(RunningSessionManager.GetSessionSpeed(1,4), 0)
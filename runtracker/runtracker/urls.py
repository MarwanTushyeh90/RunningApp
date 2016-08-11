from tracker import views
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from django.conf.urls import include, url


router = DefaultRouter()
router.register(r'sessions', views.RunSessionViewSet)
router.register(r'users', views.UserViewSet)
urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),

]

from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    url(r'tasks/', include('api.tasks.routers')),
]

urlpatterns += router.urls
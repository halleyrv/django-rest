from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.tasks.views import PeopleTasksViewSet, TaskDetailView

urlpatterns = [
    path('<int:pk>/', TaskDetailView.as_view()),
    path('people', PeopleTasksViewSet.as_view({'get': 'list'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)

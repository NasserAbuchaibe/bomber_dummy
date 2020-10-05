from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api_bomber/', views.ParentView.as_view()),
]

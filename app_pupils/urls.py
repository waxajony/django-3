from django.urls import path

from .views import all_pupils, pupil

urlpatterns = [
    path('pupils/', all_pupils),
    path('pupil/<int:id>/',pupil)
]
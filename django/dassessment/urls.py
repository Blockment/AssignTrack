from django.urls import path
from .views import *

urlpatterns = []

prefix = 'person'
urlpatterns.extend([
    path(prefix + '/create/', PersonCreate.as_view(), name='create-' + prefix),
    path(prefix + '/', PersonList.as_view()),
    path(prefix + '/<str:pk>/', PersonDetail.as_view(), name='retrieve-' + prefix),
    path(prefix + '/update/<str:pk>/', PersonUpdate.as_view(), name='update-' + prefix),
    path(prefix + '/delete/<str:pk>/', PersonDelete.as_view(), name='delete-' + prefix),
])

prefix = 'assignment'
urlpatterns.extend([
    path(prefix + '/create/', AssignmentCreate.as_view(), name='create-' + prefix),
    path(prefix + '/', AssignmentList.as_view()),
    path(prefix + '/<str:pk>/', AssignmentDetail.as_view(), name='retrieve-' + prefix),
    path(prefix + '/update/<str:pk>/', AssignmentUpdate.as_view(), name='update-' + prefix),
    path(prefix + '/delete/<str:pk>/', AssignmentDelete.as_view(), name='delete-' + prefix),
])

prefix = 'submission'
urlpatterns.extend([
    path(prefix + '/create/', SubmissionCreate.as_view(), name='create-' + prefix),
    path(prefix + '/', SubmissionList.as_view()),
    path(prefix + '/<str:pk>/', SubmissionDetail.as_view(), name='retrieve-' + prefix),
    path(prefix + '/update/<str:pk>/', SubmissionUpdate.as_view(), name='update-' + prefix),
    path(prefix + '/delete/<str:pk>/', SubmissionDelete.as_view(), name='delete-' + prefix),
])

prefix = 'assessment'
urlpatterns.extend([
    path(prefix + '/create/', AssessmentCreate.as_view(), name='create-' + prefix),
    path(prefix + '/', AssessmentList.as_view()),
    path(prefix + '/<str:pk>/', AssessmentDetail.as_view(), name='retrieve-' + prefix),
    path(prefix + '/update/<str:pk>/', AssessmentUpdate.as_view(), name='update-' + prefix),
    path(prefix + '/delete/<str:pk>/', AssessmentDelete.as_view(), name='delete-' + prefix),
])
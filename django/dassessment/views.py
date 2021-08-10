from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import *
from .models import *

API_PERSMISSION = [permissions.AllowAny] #[permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class PersonCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Person
    queryset = Person.objects.all(),
    serializer_class = PersonSerializer
    permission_classes = API_PERSMISSION

class PersonList(generics.ListAPIView):
    # API endpoint that allows Person to be viewed.
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = API_PERSMISSION

class PersonDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Person by pk.
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = API_PERSMISSION

class PersonUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Person record to be updated.
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = API_PERSMISSION

class PersonDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Person record to be deleted.
    pass
    # queryset = Person.objects.all()
    # serializer_class = PersonSerializer
    permission_classes = API_PERSMISSION


class AssignmentCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Assignment
    queryset = Assignment.objects.all(),
    serializer_class = AssignmentSerializer
    permission_classes = API_PERSMISSION

class AssignmentList(generics.ListAPIView):
    # API endpoint that allows Assignment to be viewed.
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = API_PERSMISSION

class AssignmentDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Assignment by pk.
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = API_PERSMISSION

class AssignmentUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Assignment record to be updated.
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = API_PERSMISSION

class AssignmentDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Assignment record to be deleted.
    pass
    # queryset = Assignment.objects.all()
    # serializer_class = AssignmentSerializer
    permission_classes = API_PERSMISSION


class SubmissionCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Submission
    queryset = Submission.objects.all(),
    serializer_class = SubmissionSerializer
    permission_classes = API_PERSMISSION

class SubmissionList(generics.ListAPIView):
    # API endpoint that allows Submission to be viewed.
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = API_PERSMISSION

class SubmissionDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Submission by pk.
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = API_PERSMISSION

class SubmissionUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Submission record to be updated.
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = API_PERSMISSION

class SubmissionDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Submission record to be deleted.
    pass
    # queryset = Submission.objects.all()
    # serializer_class = SubmissionSerializer
    permission_classes = API_PERSMISSION


class AssessmentCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Assessment
    queryset = Assessment.objects.all(),
    serializer_class = AssessmentSerializer
    permission_classes = API_PERSMISSION

class AssessmentList(generics.ListAPIView):
    # API endpoint that allows Assessment to be viewed.
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = API_PERSMISSION

class AssessmentDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Assessment by pk.
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = API_PERSMISSION

class AssessmentUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Assessment record to be updated.
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = API_PERSMISSION

class AssessmentDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Assessment record to be deleted.
    pass
    # queryset = Assessment.objects.all()
    # serializer_class = AssessmentSerializer
    permission_classes = API_PERSMISSION
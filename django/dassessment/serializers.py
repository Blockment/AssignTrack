from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "username", "first_name", "last_name"]

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ["id", "date", "due_date", "name", "description", "file_address", "max_score"]

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["id", "assignment_id", "date", "file_address"]

    def create(self, validated_data):
        submission = Submission.objects.create(
            username=self.context['request'].user,
            assignment_id=validated_data['assignment_id'],
            date=validated_data['date'],
            file_address=validated_data['file_address'],
        )
        submission.save()

        return submission

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ["id", "submission_id", "date", "score"]

    def create(self, validated_data):
        assessment = Assessment.objects.create(
            username=self.context['request'].user,
            submission_id=validated_data['submission_id'],
            date=validated_data['date'],
            score=validated_data['score'],
        )
        assessment.save()

        return assessment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
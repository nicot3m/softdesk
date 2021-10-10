from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id', 'contributors']
        read_only_fields = ['author_user_id']

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)

        # Get user id
        project.author_user_id = self.context['request'].user

        # Add user to contributor
        Contributor.objects.create(user_id=project.author_user_id, project_id=project, permission="All",
                                   role="Author")
        project.save()
        return project


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user_id', 'project_id', 'permission', 'role']
        read_only_fields = ['project_id']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'project_id', 'status', 'author_user_id',
                  'assignee_user_id', 'created_time']
        read_only_fields = ['project_id', 'author_user_id', 'created_time']

    def create(self, validated_data):
        issue = Issue.objects.create(**validated_data)

        # Get user id
        issue.author_user_id = self.context['request'].user

        issue = self.check_assignee_user(issue)
        return issue

    def update(self, instance, validated_data):

        # Get user id
        instance.author_user_id = validated_data.get('author_user_id', instance.author_user_id)
        instance.assignee_user_id = validated_data.get('assignee_user_id', instance.assignee_user_id)

        instance = self.check_assignee_user(instance)
        return instance

    @staticmethod
    def check_assignee_user(issue):
        # Get project id
        project = Project.objects.get(pk=issue.project_id.id)
        project_contributors = project.contributors.all()

        # If assignee_user_id is filled, check user_id is contributors
        if issue.assignee_user_id is not None:
            if issue.assignee_user_id not in project_contributors:
                issue.assignee_user_id = issue.author_user_id

        # If assignee_user_id is not filled, set author_user_id by default
        else:
            issue.assignee_user_id = issue.author_user_id

        issue.save()
        return issue


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user_id', 'issue_id', 'created_time']
        read_only_fields = ['author_user_id', 'issue_id', 'created_time']

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)

        # Get user id
        comment.author_user_id = self.context.get('request').user
        comment.save()
        return comment

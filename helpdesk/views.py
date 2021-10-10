from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError

from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from .models import Project, Contributor, Issue, Comment
from .permissions import IsAuthorOrReadOnly, IsProjectContributor, IsProjectAuthor


# Create your views here.
class ProjectViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete a project
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly, IsProjectContributor]

    def get_queryset(self):
        return Project.objects.filter(contributors=self.request.user)


class ContributorViewSet(ModelViewSet):
    """
    API endpoints to create, view or edit a contributor
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly, IsProjectContributor]

    def get_permissions(self):
        if self.action == 'create' or self.request.method == 'DELETE':
            permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]
        else:
            permission_classes = [permissions.IsAuthenticated, IsProjectContributor]
        return [permission() for permission in permission_classes]

    def get_queryset(self, *args, **kwargs):
        # project_pk is the primary key of project
        return Contributor.objects.filter(project_id=self.kwargs.get('project_pk'))

    def perform_create(self, serializer, *args, **kwargs):
        project_id = Project.objects.get(pk=self.kwargs.get('project_pk'))

        # Check if the user is is already contributor
        user_list = [user.user_id.id for user in Contributor.objects.filter(project_id=project_id)]
        if self.request.data.get('user_id') in user_list:
            raise ValidationError("this user is already contributor")
        else:
            serializer.save(project_id=project_id)


class IssueViewSet(ModelViewSet):
    """
    API endpoints to create, view or edit an issue
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_permissions(self):
        if self.action == 'create' or self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated, IsProjectContributor]
        else:
            permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self, *args, **kwargs):
        # project_pk is the primary key of project
        return Issue.objects.filter(project_id=self.kwargs.get('project_pk'))

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(project_id=Project.objects.get(pk=self.kwargs.get('project_pk')))

    def perform_update(self, serializer, *args, **kwargs):
        serializer.save(project_id=Project.objects.get(pk=self.kwargs.get('project_pk')))


class CommentViewSet(ModelViewSet):
    """
    API endpoints to create, view or edit a comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create' or self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated, IsProjectContributor]
        else:
            permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self, *args, **kwargs):
        # issue_pk is the primary key of issue
        return Comment.objects.filter(issue_id=self.kwargs.get('issue_pk'))

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(issue_id=Issue.objects.get(pk=self.kwargs.get('issue_pk')), author_user_id=self.request.user)

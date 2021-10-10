from rest_framework import permissions
from .models import Project


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # SAFE_METHODS are GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of an object (project, issue or comment)
        return obj.author_user_id == request.user


class IsProjectContributor(permissions.BasePermission):
    # Custom permission for project contributor
    def has_permission(self, request, view):
        if 'project_pk' in view.kwargs:
            this_project = view.kwargs.get('project_pk')
            print("this is it", this_project)
        elif 'pk' in view.kwargs:
            this_project = view.kwargs.get('pk')
            print("this is another one", this_project)
        else:
            return True
        project = Project.objects.get(pk=this_project)
        project_contributors = project.contributors.all()
        if request.user in project_contributors:
            return True
        else:
            return False


class IsProjectAuthor(permissions.BasePermission):
    # Custom permission for project author
    def has_permission(self, request, view):
        if 'project_pk' in view.kwargs:
            this_project = view.kwargs.get('project_pk')
            print("this is it", this_project)
        elif 'pk' in view.kwargs:
            this_project = view.kwargs.get('pk')
            print("this is another one", this_project)
        project = Project.objects.get(pk=this_project)
        if project.author_user_id == request.user:
            return True
        else:
            return False

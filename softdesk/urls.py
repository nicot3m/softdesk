from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from account.views import AccountViewSet
from helpdesk.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet


account_router = DefaultRouter()
account_router.register(r'signup', AccountViewSet)

project_router = routers.SimpleRouter()
project_router.register(r'projects', ProjectViewSet, basename='project')

project_router_nested = routers.NestedSimpleRouter(project_router, r'projects', lookup='project')
project_router_nested.register(r'users', ContributorViewSet, basename='user')
project_router_nested.register(r'issues', IssueViewSet, basename='issue')

issue_router_nested = routers.NestedSimpleRouter(project_router_nested, r'issues', lookup='issue')
issue_router_nested.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(account_router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(project_router.urls)),
    path('', include(project_router_nested.urls), name='project'),
    path('', include(issue_router_nested.urls), name='issue'),
]

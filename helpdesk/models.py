from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    TYPE_CHOICES = [("backend", "backend"), ("frontend", "frontend"), ("Android", "Android"), ("iOS", "iOS")]
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default="backend")
    author_user_id = models.ForeignKey(to=User, related_name="author_user_id_project", on_delete=models.CASCADE,
                                       blank=True, null=True)
    contributors = models.ManyToManyField(to=User, through="Contributor", related_name="contributors")

    def __str__(self):
        return "Project:" + self.title


class Contributor(models.Model):
    PERMISSION_CHOICES = [("Read", "Read"), ("All", "All")]
    ROLE_CHOICES = [("Author", "Author"), ("Manager", "Manager"), ("Creator", "Creator")]
    user_id = models.ForeignKey(to=User, related_name="user_id_contributor", on_delete=models.CASCADE,
                                blank=True, null=True)
    project_id = models.ForeignKey(to=Project, related_name="project_id_contributor", on_delete=models.CASCADE,
                                   blank=True, null=True)
    permission = models.CharField(max_length=4, choices=PERMISSION_CHOICES, default="All")
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default="Author")

    def __str__(self):
        return "Contributor:" + str(self.user_id)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    TAG_CHOICES = [("Bug", "Bug"), ("Task", "Task"), ("Upgrade", "Upgrade")]
    tag = models.CharField(max_length=7, choices=TAG_CHOICES, default='Bug')
    PRIORITY_CHOICES = [("Low", "Low"), ("Medium", "Medium"), ("High", "High")]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default="Low")
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, blank=True, null=True)
    STATUS_CHOICES = [("Pending", "Pending"), ("Open", "Open"), ("Closed", "Closed")]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default="Pending")
    author_user_id = models.ForeignKey(to=User, related_name="author_user_id_issue", on_delete=models.CASCADE,
                                       blank=True, null=True)
    assignee_user_id = models.ForeignKey(to=User, related_name="assignee_user_id_issue", on_delete=models.CASCADE,
                                         blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Issue: ' + self.title


class Comment(models.Model):
    description = models.CharField(max_length=2048, blank=True)
    author_user_id = models.ForeignKey(to=User, related_name="author_user_id_comment", on_delete=models.CASCADE,
                                       blank=True, null=True)
    issue_id = models.ForeignKey(to=Issue, related_name="issue_id_comment", on_delete=models.CASCADE,
                                 blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment: ' + self.description

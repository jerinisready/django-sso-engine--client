from django.db import models


class LeaveRequest(models.Model):
    reason = models.CharField(max_length=300)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

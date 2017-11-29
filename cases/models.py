from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from clients.models import Account
from contacts.models import Contact
from common.models import User, Team
from common.utils import CASE_TYPE, PRIORITY_CHOICE, STATUS_CHOICE, INDCHOICES




class Case(models.Model):
    name = models.CharField(
        pgettext_lazy("Name of the case", "Name"),
        max_length=64)
    status = models.CharField(choices=STATUS_CHOICE, max_length=64)
    priority = models.CharField(choices=PRIORITY_CHOICE, max_length=64)
    case_type = models.CharField(choices=INDCHOICES, max_length=255, blank=True, null=True, default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    contacts = models.ManyToManyField(Contact)

    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(User, related_name='case_assigned_users')
    teams = models.ManyToManyField(Team)
    created_by = models.ForeignKey(User, related_name='case_created_by', on_delete=models.CASCADE)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_meetings(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Meeting", status="Planned")

    def get_completed_meetings(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Meeting").exclude(status="Planned")

    def get_tasks(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(content_type=content_type, object_id=self.id, event_type="Task", status="Planned")

    def get_completed_tasks(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Task").exclude(status="Planned")

    def get_calls(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(content_type=content_type, object_id=self.id, event_type="Call", status="Planned")

    def get_completed_calls(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Call").exclude(status="Planned")

    def get_assigned_user(self):
        return User.objects.get(id=self.assigned_to.id)


def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return '{0}/{1}'.format(Case.objects.get(id=3), filename)


class UploadFile(models.Model):

    # name = models.CharField(
    #     pgettext_lazy("Name of the case", "Case Name"),
    #     max_length=64)

    name = models.ForeignKey(Case)

    # case = models.ForeignKey(Case)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    # document = models.FileField(upload_to='user_directory_path')
    uploaded_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Lead(models.Model):
    ''' lead information '''
    first_name = models.CharField(max_length=30, blank=False, default='')
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=250, blank=False)
    is_contacted = models.BooleanField(null=False)
    notes = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Form(models.Model):
    class Education(models.TextChoices):
        BACHELOR = 'Bachelor', _('Bachelor')
        MASTER = 'Master', _('Master')
        PH_D = 'PH.D', _('PH.D')
        
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    education_degree = models.CharField(
        choices=Education,
        help_text=_('Please select one of the options'),
        blank=True,
        null=True,
        max_length=8
    )

    
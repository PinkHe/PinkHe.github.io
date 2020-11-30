from django.contrib import admin

from .models import TrainCompany
from .models import WorkPosition
# Register your models here.

admin.site.register(TrainCompany)
admin.site.register(WorkPosition)
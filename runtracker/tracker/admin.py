from django.contrib import admin
from tracker.models import RunningSession

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(RunningSession)
# Register your models here.

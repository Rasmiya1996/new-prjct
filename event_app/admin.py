from django.contrib import admin

from event_app import models
admin.site.register(models.Login)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Club)
admin.site.register(models.Feedback)
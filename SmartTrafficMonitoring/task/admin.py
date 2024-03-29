from django.contrib import admin
from .models import *

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'loop', 'input_vdo', 'output_vdo', 'status_id', 'note', 'preset', 'created_by', 'created_at', 'updated_at', 'report']

class UploadFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'video_file', 'loop_txt_file']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['detail', 'task', 'already_read', 'created_by', 'created_at']

admin.site.register(Status, StatusAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Notification, NotificationAdmin)
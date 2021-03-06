from django.contrib import admin
from .models import Profile, Skill, Message

admin.site.register(Profile)
admin.site.register(Skill)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'is_read', 'created']
    search_fields = ['message']
    list_filter = ['is_read']
    


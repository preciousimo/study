from django.contrib import admin

# Register your models here.

from .models import User, Topic, Room, Message

class UserAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'username',
        'email',
        'bio'
    ]

    list_filter = [
        'name',
        'username',
        'email',
    ]

class TopicAdmin(admin.ModelAdmin):
    
    list_display = [
        'name'
    ]

    list_filter = [
        'name'
    ]

class RoomAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'topic',
        'description',
        'host',
    ]

    list_filter = [
        'name',
        'topic',
        'description'
    ]

class MessageAdmin(admin.ModelAdmin):
    
    list_display = [
        'user',
        'room',
        'body'
    ]

    list_filter = [
        'user'
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
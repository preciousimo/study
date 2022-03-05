from django.contrib import admin

# Register your models here.

from .models import User, Topic, Room, Message


class UserAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'username',
        'email',
        'bio'
    )

    list_filter = (
        'name',
        'username',
        'email',
    )

class TopicAdmin(admin.ModelAdmin):
    
    list_display = (
        'name'
    )

    list_filter = (
        'name'
    )

class RoomAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'topic',
        'description',
        'host',
        'participants'
    )

    list_filter = (
        'name',
        'topic',
        'description',
    )

class MessageAdmin(admin.ModelAdmin):
    
    list_display = (
        'user',
        'room,
        'body'
    )

    list_filter = (
        'user'
    )

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)
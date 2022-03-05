from django.contrib import admin

# Register your models here.

from .models import User, Topic, Room, Message


class UserAdmin(admin.ModelAdmin):
    
    list_display = (

    )

    list_filter = (

    )

class TopicAdmin(admin.ModelAdmin):
    
    list_display = (

    )

    list_filter = (

    )
class RoomAdmin(admin.ModelAdmin):
    
    list_display = (

    )

    list_filter = (

    )

class MessageAdmin(admin.ModelAdmin):
    
    list_display = (

    )

    list_filter = (

    )
admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)
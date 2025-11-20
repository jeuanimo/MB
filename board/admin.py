from django.contrib import admin
from .models import Message

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for Message model
    """
    list_display = ('title', 'author', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Message Information', {
            'fields': ('title', 'content', 'author')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

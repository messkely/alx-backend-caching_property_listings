from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'price', 'created_at']
    list_filter = ['location', 'created_at']
    search_fields = ['title', 'description', 'location']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description')
        }),
        ('Details', {
            'fields': ('price', 'location')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )
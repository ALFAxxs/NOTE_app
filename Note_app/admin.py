from django.contrib import admin

from .models import Note, User
@admin.register(Note, User)

class UserDataAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name' ]
    

class NoteDataAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', ]
    list_filter = ['created', 'updated']
    list_display = [ 'title', 'description']
    list_display_links = ['title']
    list_editable = ['description']
    list_per_page = 10
    ordering = ['-created']
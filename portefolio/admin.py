from django.contrib import admin

from .models import Project, Technologie, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "date",)
    list_filter = ("date",)

@admin.register(Technologie)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date",)
    list_filter = ("date",)

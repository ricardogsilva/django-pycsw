from django.contrib import admin

from . import models


class CollaboratorInline(admin.StackedInline):
    model = models.Collaborator
    extra = 1


@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("identifier", "title",)


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [CollaboratorInline,]


@admin.register(models.PycswConfig)
class PycswConfigAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

from django.contrib import admin

from sneak.admin import SneakAdmin

from query import FileSystemQuerySet
from models import FileSystemElement


class FileSystemAdmin(SneakAdmin):
    QuerySet = FileSystemQuerySet

    list_display = ('path', )
admin.site.register([FileSystemElement], FileSystemAdmin)

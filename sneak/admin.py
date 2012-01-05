from django.contrib import admin

from forms import DummyForm


class SneakAdmin(admin.ModelAdmin):
    """Inherit this class and define ``QuerySet`` attribute to sneak into
    the admin"""
    form = DummyForm

    def queryset(self, request):
        return self.QuerySet()

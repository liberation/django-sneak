from django.contrib import admin

from forms import DummyForm


class SneakAdmin(admin.ModelAdmin):
    """Inherits this class and define ``QuerySet``. ``self.QuerySet.filter``
    should Result``"""
    form = DummyForm
    actions = None

    def queryset(self, request):
        return self.QuerySet()

from django.contrib import admin

from forms import DummyForm


class SneakAdmin(admin.ModelAdmin):
    """Inherits this class and define ``QuerySet``. ``self.QuerySet.filter``
    should return a class inheriting ``sneak.query.ListQueryResult``"""
    form = DummyForm

    def queryset(self, request):
        return self.QuerySet()

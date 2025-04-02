"""
Damit die Models in der Admin sichtbar sind,
müssen sie hier registriert werden.
"""
from django.contrib import admin
from .models import Category, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author"]
    search_fields = ["name"]  # eine Suchbox, die im name-Feld sucht

    def get_queryset(self, request):
        q = request.GET.get("q") or ""
        return super().get_queryset(request).filter(name__contains=q)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sub_title", "number_events"]  # Die Felder, die in der Übersicht angezeigt werden
    actions = ["print_to_console"]

    @admin.display(description="Auf Konsole ausdrucken")
    def print_to_console(self, request, queryset):
        for q in queryset:
            print(q)

    def number_events(self, category):
        # obj => jede Kategorie 
        return category.events.count()
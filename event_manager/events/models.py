from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()  # aktuelle User-Model


class Category(models.Model):
    """Ein erstes Model."""

    name = models.CharField(max_length=100) # obligatorisch
    # null => darf in DB null sein, blank => darf im Formular leer sein
    sub_title = models.CharField(max_length=100, null=True, blank=True)  # optional
    description = models.TextField(null=True, blank=True) # optional

    # objects = models.Manager() DefaultManager
    class Meta:
        ordering = ["-name"]  # Default Sortierung ist absteigend name
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def __str__(self):
        # String-Repräsentation eines Kategorie-Objekts
        return self.name


class Event(models.Model):

    class Group(models.IntegerChoices):
        SMALL = 5, "kleine Gruppe"
        BIG = 10, "große Gruppe"

    name = models.CharField(max_length=100)
    group_size = models.PositiveIntegerField(choices=Group.choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")  # sport.events.all()
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="events")   # bob.events.all()
    
    def __str__(self):
        return self.name
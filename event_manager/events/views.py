from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # für die klassenbasierten Views
from django.contrib.auth.decorators import login_required   # für die funktionsbasierte Views
from django.http import HttpResponse
from .models import Category, Event
from .forms import EventForm, EmailForm


class IsAdminUser(UserPassesTestMixin):
    """ 
    Ein Mixin, dass prüft, ob ein User ein Admin-User ist
    """
    def test_func(self):
        return self.request.user.is_superuser


class EventDeleteView(IsAdminUser, DeleteView):
    """ 
    muss Adminuser sein, um den Event zu löschen

    events/delete/3
    generische Templatename ist: event_confirm_delete.html 
    """
    model = Event
    success_url = reverse_lazy("events:event_list")


class EventUpdateView(IsAdminUser, UpdateView):
    """ 
    muss Adminuser sein, um den Event zu löschen

    events/update/3
    """
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("events:event_list")


class EventCreateView(LoginRequiredMixin, CreateView):
    """
    Muss eingeloggt sein!

    generische Klassenbasierte View zum Anlegen eines Objekts
    benötigt Formular und Template   
    generische Templatename ist: event_form.html 

    events/create
    """
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("events:event_list")  #=> events/
    


class EventListView(ListView):
    """ 
    generische klassenbasierte List-View
    template_name = event_list.html
    generische Name der Eventliste: object_list

    127.0.0.1:8000/events
    """
    model = Event
    # queryset = Event.objects.all()
    # Inner Join auf Category und User-Table
    queryset = Event.objects.select_related("category", "author").all()


@login_required
def category_detail(request, pk):
    """View zum Anzeigen der Detailseite einer Kategorie.
    
    127.0.0.1:8000/events/category/3
    """
    # category = Category.objects.get(pk=pk)
    # Verhindern, dass ein 500-Server-Error ausgelöst wird, wenn ein Objekt nicht gefunden wird
    # holt das Objekt aus DB oder löst 404-Fehler aus
    category = get_object_or_404(Category, pk=pk) 
    # try:
    #     category = Category.objects.get(pk=pk)
    # except Category.DoesNotExist:
    #     return redirect("/events/categories")

    context = {
        "category": category,
    }
    return render(request, "events/category_detail.html", context)


def send_mail(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            print("Name aus Form: ", form.cleaned_data["name"])
        return redirect("events:event_list")
    else:
        form = EmailForm()
    
    return render(request, "events/email_form.html", {"form": form})


def category_list(request):
    """View zum Auflisten der Kategorien.

    127.0.0.1:8000/events/categories
    """
    categories = Category.objects.all()
    context = {
        "dummy": "Das ist ein Dummytext",
        "categories": categories
    }
    return render(request, "events/categories.html", context)


def hello_world(request):
    """Eine erste View.
    
    127.0.0.1:8000/events/hello
    """
    # das wird auf der Konsole im Webserver ausgegeben
    print("Hello World auf Console")

    # eine HTTP-Response als content-type text
    return HttpResponse("Hello World")

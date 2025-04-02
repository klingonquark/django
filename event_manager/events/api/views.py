from rest_framework import generics, permissions, authentication
from .serializers import CategorySerializer
from events.models import Category



class CategoryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    """ 
    View zum Holen, Löschen und Updaten eines Kategorie-Objekts
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    View zum Anlegen eines Objekts und Auslesen von vielen 
    Objekte. 
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
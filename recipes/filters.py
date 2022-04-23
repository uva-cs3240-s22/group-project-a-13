from typing import OrderedDict
import django_filters
from .models import *

class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = []
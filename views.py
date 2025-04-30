import random
from django.shortcuts import render
from .models import Quote

def random_quote(request):
    quotes = Quote.objects.all()
    quote = random.choice(quotes) if quotes else None
    return render(request, 'quotes/index.html', {'quote': quote})

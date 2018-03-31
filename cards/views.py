from django.shortcuts import render

from django.http import Http404

from .models import Card

def index(request, card_id):
    try:
        card = Card.objects.get(pk=card_id)
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    
    path = 'training_data/' + str(card_id) + '.png'
    return render(request, 'cards/card.html',
     {'path': path, 'card_id': card_id})

    

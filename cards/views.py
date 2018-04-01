from django.shortcuts import render, redirect

from django.http import Http404, HttpResponse

from .models import Card
from .helpers import fetch_unidentified

import json

def index(request):
    next = fetch_unidentified()
    if next:
        return redirect('card', card_num=next)
    else:
        return redirect('done')

def done(request):
    cards = Card.objects.all()
    list = [(card.id, card.color, card.rank) for card in cards]
    return HttpResponse(json.dumps(list))

def card(request, card_num):
    if request.method == 'GET':
        try:
            card = Card.objects.get(pk=card_num)
        except Card.DoesNotExist:
            raise Http404("Card does not exist")
        
        image_path = 'training_data/' + str(card_num) + '.png'

        if card.color != '':            
            return render(request, 'cards/card_done.html', 
            {'identified_card': str(card), 'path': image_path })  

        
        return render(request, 'cards/card.html',
        {'path': image_path, 'card_num': card_num})
    elif request.method == 'POST':
        try:
            card = Card.objects.get(num=card_num)

            trash = request.POST.get('trash', None)
            color = request.POST.get('color', None)
            rank = request.POST.get('rank', None)
            if trash == 'true':
                card.color = 'not_card'
                card.rank = 'not_card'        
                card.save()
            elif color and rank:
                card.color = color
                card.rank = rank
                card.save()                                    
        except Card.DoesNotExist:
            raise Http404("Card does not exist")                

        return redirect('index')


    

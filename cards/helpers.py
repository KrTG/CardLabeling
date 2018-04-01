from .models import Card

def fetch_unidentified():
    cards = Card.objects.filter(color='', rank='')
    if (cards):
        return cards[0].id
    else:
        return None


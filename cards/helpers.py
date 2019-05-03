from .models import Card

def fetch_unidentified():
    cards = Card.objects.filter(color='', rank='')
    if (cards):
        return cards[0].num
    else:
        return None

def populate_db():
    Card.objects.all().delete()
    for i in range(1, 1197):
        c = Card(num=i)
        c.save()

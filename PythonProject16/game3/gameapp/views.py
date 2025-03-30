from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html')

def game(request):
    return render(request, 'game.html')
def player(request):
    return render(request, 'player.html')
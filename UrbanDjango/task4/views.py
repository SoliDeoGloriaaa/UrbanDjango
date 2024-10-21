from django.shortcuts import render


def index(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    context = {
        'games': ["Atomic Heart", "Cyberpunk 2077", "Pay Day 2"]
    } 
    return render(request, 'fourth_task/shop.html', context)


def shop_cart(request):
    return render(request, 'fourth_task/shop_cart.html')
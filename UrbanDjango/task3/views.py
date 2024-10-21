from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    atomic_heard = 'Atomic Heard'
    cyberpunk_2077 = 'Cyberpunk 2077'
    pay_day_2 = 'Pay Day 2'
    context = {
        'atomic_heard': atomic_heard,
        'cyberpunk_2077': cyberpunk_2077,
        'pay_day_2': pay_day_2
    }
    return render(request, 'third_task/shop.html', context)


def shop_cart(request):
    return render(request, 'third_task/shop_cart.html')

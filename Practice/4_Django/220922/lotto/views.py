from django.shortcuts import render
import random

# Create your views here.
def getLotto(request):
    num_range = range(1, 46)
    lotto = list()

    for i in range(5):
        row = random.sample(num_range, 6)
        lotto.append(sorted(row))

    context = {
        'lotto': lotto,
    }
    
    return render(request, 'lotto.html', context)
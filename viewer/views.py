from django.shortcuts import render

def hello(request):
    # práce s databází
    adjectives = ['nice', 'cruel', 'blue', 'beautiful']
    name = 'Petr'
    context = {'adjectives': adjectives, 'name': name}
    return render(request, 'hello.html',
                  context=context)
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def all_pupils(request):
    pupils = [
        {'id': 1, 'full_name': 'Ruslan mamatanov', 'full_ball': 40},
        {'id': 2, 'full_name': 'Muhammadyusuf Abduvaliyev', 'full_ball': 36},
        {'id': 3, 'full_name': 'Zafarbek Olimbayev', 'full_ball': 39},
        {'id': 4, 'full_name': 'Samariddin Baxtiyorov', 'full_ball': 31},
        {'id': 5, 'full_name': 'Sunnatillo Sharipov', 'full_ball': 40},
        {'id': 6, 'full_name': 'Shoxrux Turdaliyev', 'full_ball': 00},

    ]
        
    return render(request, 'pupils.html', context={'pupils': pupils})
def pupil(request, id):
    pupils = [
        {'id': 1, 'full_name': 'Ruslan Mamatanov ', 'full_ball': 40},
        {'id': 2, 'full_name': 'Muhammadyusuf Abdullayev', 'full_ball': 36},
        {'id': 3, 'full_name': 'Zafarbek Olimbayev', 'full_ball': 39},
        {'id': 4, 'full_name': 'Samariddin Baxtiyorov', 'full_ball': 31},
        {'id': 5, 'full_name': 'Sunnatillo Sharipov', 'full_ball': 40},
        {'id': 6, 'full_name': 'Shohruxbek Turdaliyev', 'full_ball': 00},

    ]

    if id > len(pupils):
        return HttpResponse(f"guruhda{len(pupils)} ta oquvchi  bor")
    else:
        return render(request, 'pupil.html', context={'pupil': pupils[id-1]})
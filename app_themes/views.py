from django.shortcuts import render

# Create your views here.
def themes_list(request):
    list_les = []
    with open('templates/lesson.txt', 'r') as file:
        for f in file:
            list_les.append(f)

    return render(request, 'themes.html', context= {'list_les': list_les})


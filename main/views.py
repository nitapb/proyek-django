from django.shortcuts import render

def index(request):
    context = {
        'app_name': 'Football Shop',
        'student_name': 'Nita Pasaribu',     # ganti dengan nama aslimu
        'student_class': 'PBP A'    # ganti dengan kelasmu
    }
    return render(request, 'main.html', context)
from django.shortcuts import render

def index(request):
    context = {
        'app_name': 'Football Shop',
        'student_name': 'Nama Kamu',     # ganti dengan nama aslimu
        'student_class': 'Kelas Kamu'    # ganti dengan kelasmu
    }
    return render(request, 'main/main.html', context)
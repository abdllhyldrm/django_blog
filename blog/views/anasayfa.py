from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim': 'Abdullah Yıldırım'
    }
    return render(request, 'pages/anasayfa.html', context={})
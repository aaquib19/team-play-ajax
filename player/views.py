from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from .models import  Player

def create_player(request):
    print("Fasdfas")
    players = Player.objects.all()
    response_data={}
    print(request.method)
    print(request.POST)
    print(request.body)
    if request.POST.get('action') == 'post':
        print(request.POST,request.body)
        pname = request.POST.get('pname')
        hscore = request.POST.get('hscore')
        age = request.POST.get('age')
        response_data['pname'] = pname
        response_data['hscore'] = hscore
        response_data['age'] = age

        obj = Player.objects.create(
            pname=pname,
            hscore=hscore,
            age=age
        )
        print("id == ",obj.pk)
        return JsonResponse({"id":obj.pk})

    return render(request,'mytemplate.html',{"players":players})
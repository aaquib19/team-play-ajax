from django.shortcuts import render
# Create your views here.


def create_team(request):

    if request.POST:
        print(request.POST)
    else :
        return render(request,'add-team.html',{})

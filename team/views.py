from django.shortcuts import render
from .forms import TeamForm
# Create your views here.


def team(request):

    if request.POST:
        print(request.POST)
    else :
        form = TeamForm()
        return render(request,'add-team.html',{'form':form})

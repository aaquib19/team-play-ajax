from django.shortcuts import render
# Create your views here.
from .models import Team
from player.models import Player
def create_team(request):
    print("in create team")
    if request.POST:
        players  = request.POST.get("pids")
        plist = players.split(",")
        plist =plist[:-1]
        tname  = request.POST.get("tname")
        obj = Team.objects.create(
            tname=tname
        )
        for id in plist:
            player_obj = Player.objects.get(id=int(id))
            obj.player.add(player_obj)
        obj.save()
        print(tname,players.split(","))
        print(request.POST)

    return render(request,'add-team.html',{})

from django.shortcuts import render
# Create your views here.
from .models import Team
from player.models import Player
def create_team(request):
    print("in create team")
    if request.POST:
        tname  = request.POST.get("tname")
        print(tname)
        obj = Team.objects.create(
            tname=tname
        )
        player_ids =  request.POST.get('pids').split(",")
        for i in player_ids:
            print(i)
            pname = request.POST.get('pname['+str(i) +']')
            score = request.POST.get('score['+str(i) +']')
            age = request.POST.get('age['+str(i) +']')
            print(pname)
            player_obj = Player.objects.create(
                pname=pname,
                hscore=score,
                age=age
            )
            obj.player.add(player_obj)

        # players  = request.POST.get("pids")
        # plist = players.split(",")
        # plist =plist[:-1]
        # tname  = request.POST.get("tname")
        # obj = Team.objects.create(
        #     tname=tname
        # )
        # for id in plist:
        #     player_obj = Player.objects.get(id=int(id))
        #     obj.player.add(player_obj)
        # obj.save()
        # print(tname,players.split(","))
        print(request.POST)

        print(request.POST['pids'])
        # print(len(lll))
        # for i in lll:
        #     print(i)

    return render(request,'add-team.html',{})


def edit_team(request,pk):
    print("in create team")

    obj = Team.objects.get(pk=pk)

    print(request.POST)
    if request.POST:
        players  = request.POST.get("pids")
        plist = players.split(",")
        plist =plist[:-1]
        tname  = request.POST.get("tname")
        print(tname)
        obj.tname = tname
        obj.save()
        for id in plist:
            player_obj = Player.objects.get(id=int(id))
            obj.player.add(player_obj)
        print(request.POST)

    return render(request,'edit-team.html',{"id":pk,"obj":obj})


def delete_team(request,teamid,playerid):
    # print(teamid,playerid)
    print("fasdf")
    obj = Team.objects.filter(pk=teamid).first()
    player_obj  = Player.objects.filter(pk=playerid).first()
    print(player_obj,obj)
    obj.player.remove(player_obj)

    return  render(request,'edit-team.html',{"obj":obj})


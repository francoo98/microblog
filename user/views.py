from django.http import HttpResponse
from django.shortcuts import render
from user.models import User

def profile(request, id):
    current_user = request.user
    visited_user = User.objects.get(id = id)
    return render(request, 'user/index.html', {'current_user': current_user, 'visited_user': visited_user})

def seguidores(request, id):
    user = User.objects.get(id = id)
    seguidores = user.profile.profile_set.all()
    return render(request, 'user/seguidores.html', {'seguidores': seguidores, 'id': id})

def siguiendo(request, id):
    user = User.objects.get(id = id)
    siguiendo = user.profile.following.all()
    return render(request, 'user/siguiendo.html', {'siguiendo': siguiendo, 'id': id})

def seguir(request, id):
    follower = request.user
    followed = User.objects.get(id = id)
    if followed.id != follower.id:
        follower.profile.following.add(followed.profile)
        return render(request, 'user/seguido.html', {'follower': follower, 'followed': followed})
    return HttpResponse('Error! no podes seguirte a vos mismo')
    
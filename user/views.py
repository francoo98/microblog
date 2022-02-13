from django.http import HttpResponse
from django.shortcuts import render
from user.models import User

def profile(request, id = None):
    if id:
        user = User.objects.get(id = id)
    else:
        user = request.user
    return render(request, 'user/index.html', {'user': user})

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
    follower.profile.following.add(followed.profile)
    return HttpResponse("Seguido!") # hacer template
from django.urls import path
from user.views import profile, seguidores, seguir, siguiendo

urlpatterns = [
    path('', profile),
    path('user/<int:id>', profile),
    path('user/seguidores/<int:id>', seguidores, name = "seguidores"),
    path('user/siguiendo/<int:id>', siguiendo, name = "siguiendo"),
    path('user/seguir/<int:id>', seguir, name = "seguir")
]
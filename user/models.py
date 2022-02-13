from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    following = models.ManyToManyField("self", symmetrical = False)

    def __str__(self):
        return self.user.username + " profile"

    """class Meta:
        constraints = [
            CheckConstraint(check=Q(following = (F.Profile.following.from_Profile_id != F.Profile.following.to_profile_id)), name='following_df')
        ]"""

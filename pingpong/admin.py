from django.contrib import admin
from .models import Profile, Team, Player, Competition, Participation

# Register your models here.

admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Competition)
admin.site.register(Participation)
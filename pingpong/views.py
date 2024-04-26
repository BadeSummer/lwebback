from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Profile, Team, Player, Competition, Participation
from .serializers import ProfileSerializer, TeamSerializer, PlayerSerializer, CompetitionSerializer, ParticipationSerializer

# ViewSets 自动处理常见的 CRUD 操作
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer

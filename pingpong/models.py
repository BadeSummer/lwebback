from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
class Player(models.Model):
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
    
class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='profile', verbose_name="选手")
    blade = models.CharField(max_length=100, verbose_name="底板")
    forehand_rubber = models.CharField(max_length=100, verbose_name="正手胶皮")
    backhand_rubber = models.CharField(max_length=100, verbose_name="反手胶皮")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="性别")

    def __str__(self):
        return f"{self.blade} | {self.forehand_rubber} | {self.backhand_rubber} | {self.gender}"

class Competition(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name}"
    
class Participation(models.Model):
    RANK_CHOICES = (
        (1, '冠军'),
        (2, '亚军'),
        (3, '季军'),
        (4, '殿军'),
        (5, '第五名'),
        (9, '第九名'),
    )

    competition = models.ForeignKey(Competition, related_name='participations', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='participations', on_delete=models.CASCADE, null=True, blank=True)
    player = models.ForeignKey(Player, related_name='participations', on_delete=models.CASCADE, null=True, blank=True)
    rank = models.IntegerField(choices=RANK_CHOICES, help_text="选择名次，如：1（冠军）、2（亚军）等。")

    class Meta:
        unique_together = (('competition', 'team'), ('competition', 'player'))
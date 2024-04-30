from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100,
                                verbose_name='球队名称')
    
    def __str__(self):
        return f"{self.teamName}"
    
    class Meta:
        verbose_name = "球队"
        verbose_name_plural = "球队列表"
    
class Player(models.Model):
    team = models.ForeignKey(Team,
                             related_name='players',
                             on_delete=models.CASCADE,
                             verbose_name='所属球队')
    player_name = models.CharField(max_length=100,
                                  verbose_name='球员名称')
    points = models.PositiveSmallIntegerField(verbose_name='物天对战积分')

    def __str__(self):
        return f"{self.playerName}"
    
    class Meta:
        verbose_name = "球员"
        verbose_name_plural = "球员列表"
    
class Blade(models.Model):
    produce_name = models.CharField(max_length=100,
                                   verbose_name="底板型号")

    HOLDING_TYPE = (
        ('S', '直拍'),
        ('T', '横拍'),
        ('O', '其他')
    )
    holding_type = models.CharField(max_length=1,
                                   choices=HOLDING_TYPE,
                                   verbose_name="持握类型")

    def __str__(self):
        return f"{self.produceName} | {self.holdingType}"
    
    class Meta:
        verbose_name = "底板"
        verbose_name_plural = "底板列表"

class Rubber(models.Model):
    produce_name = models.CharField(max_length=100,
                                   verbose_name="胶皮型号")

    RUBBER_CHOICE = (
        ('I', '反胶'),
        ('O', '正胶'),
        ('S', '生胶'),
        ('L', '长胶')
    )
    category = models.CharField(choices=RUBBER_CHOICE,
                                verbose_name='胶皮类型')

    def __str__(self):
        return f"{self.produceName} | {self.category}"
    
    class Meta:
        verbose_name = "胶皮"
        verbose_name_plural = "胶皮列表"

class PingpongUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_player = models.BooleanField(default=False,
                                   verbose_name='是否为记录球员')
    connect_player = models.OneToOneField(Player,
                                         null=True,
                                         blank=True,
                                         verbose_name="用户关联的球员")
   
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | 是否关联球员：{self.isPlayer} | {self.connectPlayer}"
    
    class Meta:
        verbose_name = "乒乓用户"
        verbose_name_plural = "乒乓用户列表"

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    player = models.OneToOneField(Player,
                                  on_delete=models.CASCADE,
                                  related_name='profile',
                                  verbose_name="选手")
    blade = models.CharField(max_length=100,
                             verbose_name="底板",
                             null=True,
                             blank=True)
    forehand_rubber = models.CharField(max_length=100,
                                       verbose_name="正手胶皮",
                                       null=True,
                                       blank=True)
    backhand_rubber = models.CharField(max_length=100,
                                       verbose_name="反手胶皮",
                                       null=True,
                                       blank=True)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              verbose_name="性别")

    def __str__(self):
        return f"{self.player.playerName} | {self.blade} | {self.forehand_rubber} | {self.backhand_rubber} | {self.gender}"
    
    class Meta:
        verbose_name = "选手信息"
        verbose_name_plural = "选手信息列表"

class Competition(models.Model):
    competition_name = models.CharField(max_length=100,
                                       verbose_name='赛事名称')
    date = models.DateField(verbose_name='举办时间')

    def __str__(self):
        return f"{self.CompetitionName} on {self.date}"
    
    class Meta:
        verbose_name = "赛事"
        verbose_name_plural = "赛事列表"
    
class Participation(models.Model):
    RANK_CHOICES = (
        (1, '冠军'),
        (2, '亚军'),
        (3, '季军'),
        (4, '殿军'),
        (5, '第五名'),
        (9, '第九名'),
    )

    competition = models.ForeignKey(Competition,
                                    related_name='participations',
                                    on_delete=models.CASCADE,
                                    verbose_name='赛事')
    team = models.ForeignKey(Team,
                             related_name='participations',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             verbose_name='获奖队伍')
    player = models.ForeignKey(Player,
                               related_name='participations',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               verbose_name='获奖选手')
    rank = models.PositiveSmallIntegerField(choices=RANK_CHOICES,
                                            help_text="选择名次，如：1（冠军）、2（亚军）等。",
                                            verbose_name='获奖名次')

    def __str__(self):
        return f"{self.competition} | {self.team} {self.player} | {self.rank}"

    class Meta:
        verbose_name = "奖项"
        verbose_name_plural = "奖项"
        unique_together = (('competition', 'team'), ('competition', 'player'))
from django.db import models

class User(models.Model):
    u_id = models.IntegerField(primary_key=True)
    u_name = models.CharField(max_length = 108)
    t_id = models.IntegerField()
    t_name = models.CharField(max_length = 108)
    total_score = models.IntegerField(default=0)
    t_url = models.URLField()

class Matches(models.Model):
    m_id = models.IntegerField()
    team1 = models.IntegerField()
    team2 = models.IntegerField()
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    match_time = models.DateTimeField()

class Headtohead(models.Model):
    id = models.ForeignKey('User', primary_key=True)
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    h2h_score = models.IntegerField(default=0)


# http://stackoverflow.com/questions/4616787/django-making-a-custom-pk-auto-increment
# http://david.feinzeig.com/blog/2011/12/06/how-to-properly-set-a-default-value-for-a-datetimefield-in-django/
from django.db import models

# Create your models here.

class matchFixture(models.Model):
    match_id = models.IntegerField(default=0)
    round_number = models.IntegerField(default=0)
    match_time = models.DateTimeField()
    location = models.CharField(max_length=50)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    match_name = models.CharField(max_length=100)
    result = models.CharField(max_length=50)

    def __str__(self):
        return "%s" %(self.match_id)

#Add questions and options only
class FirstQuestion(models.Model):
    match_id = models.ForeignKey(matchFixture, on_delete=models.CASCADE)
    player = models.CharField(max_length=30, default='No Name') # delete player column
    question1 = models.TextField()
    q1_option_one = models.CharField(max_length=30)
    q1_option_two = models.CharField(max_length=30)

    question2 = models.TextField()
    q2_option_one = models.CharField(max_length=30)
    q2_option_two = models.CharField(max_length=30)
    q2_option_three = models.CharField(max_length=30)
    q2_option_four = models.CharField(max_length=30)

    question3 = models.TextField()
    q3_option_one = models.CharField(max_length=30)
    q3_option_two = models.CharField(max_length=30)
    q3_option_three = models.CharField(max_length=30)
    q3_option_four = models.CharField(max_length=30)

    def __str__(self):
        return "%s" %(self.match_id)

#take entries only
class FirstQuestion_entry(models.Model):
    submitted_on = models.DateTimeField()
    player = models.CharField(max_length=30)
    match_id = models.IntegerField(default=0)
    q1_select = models.CharField(max_length=30,default='NULL')
    q2_select = models.CharField(max_length=30,default='NULL')
    q3_select = models.CharField(max_length=30,default='NULL')
    q1_flag = models.BooleanField(default=0)
    q2_flag = models.BooleanField(default=0)
    q3_flag = models.BooleanField(default=0)
    q1_stake = models.FloatField(default=0)
    q2_stake = models.FloatField(default=0)
    q3_stake = models.FloatField(default=0)
    total_points = models.FloatField(default=0)
    pred_accuracy = models.FloatField(default=0)


    def __str__(self):
        return "%s" %(self.match_id)



class Results(models.Model):
    match_id = models.ForeignKey(matchFixture, on_delete=models.CASCADE)
    q1_answer = models.CharField(max_length=30)
    q2_answer = models.CharField(max_length=30)
    q3_answer = models.CharField(max_length=30)

    def __str__(self):
        return "%s" %(self.match_id)

# No need to activate
class MatchPoints(models.Model):
    match_id = models.ForeignKey(matchFixture, on_delete=models.CASCADE)
    player = models.ForeignKey(FirstQuestion_entry, on_delete=models.CASCADE)
    q1_points = models.FloatField()
    q2_points = models.FloatField()
    q3_points = models.FloatField()

    def __str__(self):
        return "%s" %(self.match_id)

# No need for this model 
class Leaderboard(models.Model):
    player = models.CharField(max_length=30)
    points = models.FloatField()
    pred_acc = models.FloatField()
    highest_stake = models.FloatField()
    total_attempt = models.FloatField()

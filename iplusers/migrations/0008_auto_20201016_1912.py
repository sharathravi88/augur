# Generated by Django 3.0.3 on 2020-10-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplusers', '0007_auto_20201016_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstquestion',
            name='q1_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q1_two_count',
            field=models.IntegerField(default=0),
        ),
    ]
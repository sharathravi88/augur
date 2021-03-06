# Generated by Django 3.0.3 on 2020-10-13 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='matchFixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField(default=0)),
                ('round_number', models.IntegerField(default=0)),
                ('match_time', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('home_team', models.CharField(max_length=50)),
                ('away_team', models.CharField(max_length=50)),
                ('match_name', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FirstQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=30)),
                ('question1', models.TextField()),
                ('q1_option_one', models.CharField(max_length=30)),
                ('q1_option_two', models.CharField(max_length=30)),
                ('q1_option_one_count', models.IntegerField(default=0)),
                ('q1_option_two_count', models.IntegerField(default=0)),
                ('q1_option_one_select', models.CharField(max_length=30)),
                ('q1_option_two_select', models.CharField(max_length=30)),
                ('q1_result', models.IntegerField(default=0)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iplusers.matchFixture')),
            ],
        ),
    ]

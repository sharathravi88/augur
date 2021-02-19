# Generated by Django 3.0.3 on 2020-10-18 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iplusers', '0010_auto_20201018_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1_points', models.FloatField()),
                ('q2_points', models.FloatField()),
                ('q3_points', models.FloatField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iplusers.matchFixture')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iplusers.FirstQuestion_entry')),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-10-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplusers', '0008_auto_20201016_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=30)),
                ('points', models.FloatField()),
                ('pred_acc', models.FloatField()),
                ('highest_stake', models.FloatField()),
                ('total_attempt', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='firstquestion',
            old_name='q1_result',
            new_name='q2_four_count',
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q2_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q2_option_four',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q2_option_one',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q2_option_three',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q2_option_two',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q2_three_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q2_two_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q3_four_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q3_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q3_option_four',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q3_option_one',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q3_option_three',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q3_option_two',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q3_three_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='q3_two_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='question2',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion',
            name='question3',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstquestion_entry',
            name='q2_select',
            field=models.CharField(default='NULL', max_length=30),
        ),
        migrations.AddField(
            model_name='firstquestion_entry',
            name='q3_select',
            field=models.CharField(default='NULL', max_length=30),
        ),
    ]
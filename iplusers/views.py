from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.views.generic import View
from django.views import generic
from datetime import datetime, timedelta, date
from django.utils import timezone
from .models import matchFixture, FirstQuestion, FirstQuestion_entry, Results, Leaderboard
import csv, io
from django.http import HttpResponse
from .forms import UpdateResultForm
from django.db.models import Avg, Count, Min, Sum, Max
from django.contrib.auth.decorators import permission_required

# Create your views here.

class indexView(generic.ListView):
    template_name = 'iplusers/index.html'
    context_object_name='all_matches'
    def get_queryset(self):
        return matchFixture.objects.filter(match_time__gte=timezone.now()).filter(match_time__day=date.today().day)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    form = UserCreationForm()
    context = {'form': form}

    return render(request,'registration/register.html', context)


#To upload raw

def fixture_upload(request):
    template = "iplusers/fixture_upload.html"
    date = matchFixture.objects.all()

    prompt ={
        'order':'order of the csv should be match_id, rounds, date, etc',
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file.')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = matchFixture.objects.update_or_create(
            match_id=column[0],
            round_number=column[1],
            match_time=column[2],
            location=column[3],
            home_team=column[4],
            away_team=column[5],
            match_name=column[6],
            result=column[7]
    )
    context = {}
    return render(request, template, context)

class AllMatchView(generic.ListView):
    template_name = 'iplusers/matches.html'
    context_object_name='matchlist'
    def get_queryset(self):
        return matchFixture.objects.all()

@login_required
def vote(request, match_id):
    try:
        q1 = FirstQuestion.objects.get(match_id=match_id)
    except FirstQuestion.DoesNotExist:
        q1 = ''
    print(q1)
    context = {
         'q1':q1
    }

    return render(request,'iplusers/vote.html',context)


# @permission_required("iplusers.vote")
# def restricted_view(request):
#     return HttpResponse("no no no")

@login_required
def submit_vote(request, match_id):

    q1 = FirstQuestion.objects.get(match_id=match_id)
    q2 = FirstQuestion_entry.objects.filter(match_id=match_id)
    player = request.user.username

    # For option one
    submitted_on = timezone.now()
    if q2.filter(player=player).exists():

        if request.method=='POST':
            selected_option = request.POST.get('poll')
            selected_option2 = request.POST.get('poll2')
            selected_option3 = request.POST.get('poll3')

            # Update Q1_Select
            if selected_option == 'option1':
                q1_select = q1.q1_option_one
                q1_entry = FirstQuestion_entry.objects.filter(player=player).update(q1_select=q1_select)
            elif selected_option == 'option2':
                q1_select = q1.q1_option_two
                q1_entry = FirstQuestion_entry.objects.filter(player=player).update(q1_select=q1_select)
            else:
                return HttpResponse(400, 'Contact Admin')

            # Update Q2_Select
            if selected_option2 == 'option1':
                q2_select = q1.q2_option_one
                q2_entry = FirstQuestion_entry.objects.filter(player=player).update(q2_select=q2_select)
            elif selected_option2 == 'option2':
                q2_select = q1.q2_option_two
                q2_entry = FirstQuestion_entry.objects.filter(player=player).update(q2_select=q2_select)
            elif selected_option2 == 'option3':
                q2_select = q1.q2_option_three
                q2_entry = FirstQuestion_entry.objects.filter(player=player).update(q2_select=q2_select)
            elif selected_option2 == 'option4':
                q2_select = q1.q2_option_four
                q2_entry = FirstQuestion_entry.objects.filter(player=player).update(q2_select=q2_select)
            else:
                return HttpResponse(400, 'Contact Admin')

            #Update q3_select

            if selected_option3 == 'option1':
                q3_select = q1.q3_option_one
                q3_entry = FirstQuestion_entry.objects.filter(player=player).update(q3_select=q3_select)
            elif selected_option3 == 'option2':
                q3_select = q1.q3_option_two
                q3_entry = FirstQuestion_entry.objects.filter(player=player).update(q3_select=q3_select)
            elif selected_option3 == 'option3':
                q3_select = q1.q3_option_three
                q3_entry = FirstQuestion_entry.objects.filter(player=player).update(q3_select=q3_select)
            elif selected_option3 == 'option4':
                q3_select = q1.q3_option_four
                q3_entry = FirstQuestion_entry.objects.filter(player=player).update(q3_select=q3_select)
            else:
                return HttpResponse(400, 'Contact Admin')

    else:
        if request.method=='POST':
            selected_option = request.POST.get('poll')
            selected_option2 = request.POST.get('poll2')
            selected_option3 = request.POST.get('poll3')
            if selected_option == 'option1':
                q1_select = q1.q1_option_one
                q1_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q1_select=q1_select)
            elif selected_option == 'option2':
                q1_select = q1.q1_option_two
                q1_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q1_select=q1_select)
            else:
                return HttpResponse(400, 'Contact Admin')
            q1_entry.save()


            #Create Q2_Select
            if selected_option2 == 'option1':
                q2_select = q1.q2_option_one
                q2_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q2_select=q2_select)
            elif selected_option2 == 'option2':
                q2_select = q1.q2_option_two
                q2_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q2_select=q2_select)
            elif selected_option2 == 'option3':
                q2_select = q1.q2_option_three
                q2_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q2_select=q2_select)
            elif selected_option2 == 'option4':
                q2_select = q1.q2_option_four
                q2_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q2_select=q2_select)
            else:
                return HttpResponse(400, 'Contact Admin')
            q2_entry.save()

            #Create Q3_Select

            if selected_option3 == 'option1':
                q3_select = q1.q3_option_one
                q3_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q3_select=q3_select)
            elif selected_option3 == 'option2':
                q3_select = q1.q3_option_two
                q3_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q3_select=q3_select)
            elif selected_option3 == 'option3':
                q3_select = q1.q3_option_three
                q3_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q3_select=q3_select)
            elif selected_option3 == 'option4':
                q3_select = q1.q3_option_four
                q3_entry = FirstQuestion_entry(submitted_on=submitted_on,player=player,match_id=match_id,q3_select=q3_select)
            else:
                return HttpResponse(400, 'Contact Admin')
            q3_entry.save()
    return render(request,'iplusers/submitted.html')



class CurrentMatchView(generic.ListView):
    template_name = 'iplusers/match_status.html'
    context_object_name='cm'
    matchFixture.objects.filter(match_time__lte=timezone.now()).filter(result='')
    def get_queryset(self):
        a = matchFixture.objects.filter(match_time__lte=timezone.now()).filter(result='')
        return a

def MatchStatusView(request,match_id):
    try:
        status = FirstQuestion_entry.objects.filter(match_id=match_id)
    except:
        status =''
    try:
        counter = FirstQuestion.objects.get(match_id=match_id)
    except:
        counter=''


    if status=='' or counter=='':
        return render(request,"iplusers/comingsoon.html")

    counter11 = FirstQuestion_entry.objects.filter(q1_select=counter.q1_option_one).filter(match_id=match_id).count()
    counter12 = FirstQuestion_entry.objects.filter(q1_select=counter.q1_option_two).filter(match_id=match_id).count()
    counter21 = FirstQuestion_entry.objects.filter(q2_select=counter.q2_option_one).filter(match_id=match_id).count()
    counter22 = FirstQuestion_entry.objects.filter(q2_select=counter.q2_option_two).filter(match_id=match_id).count()
    counter23 = FirstQuestion_entry.objects.filter(q2_select=counter.q2_option_three).filter(match_id=match_id).count()
    counter24 = FirstQuestion_entry.objects.filter(q2_select=counter.q2_option_four).filter(match_id=match_id).count()
    counter31 = FirstQuestion_entry.objects.filter(q3_select=counter.q3_option_one).filter(match_id=match_id).count()
    counter32 = FirstQuestion_entry.objects.filter(q3_select=counter.q3_option_two).filter(match_id=match_id).count()
    counter33 = FirstQuestion_entry.objects.filter(q3_select=counter.q3_option_three).filter(match_id=match_id).count()
    counter34 = FirstQuestion_entry.objects.filter(q3_select=counter.q3_option_four).filter(match_id=match_id).count()
    total = counter11+counter12
    template = 'iplusers/current_status.html'
    context ={
        'status':status,
        'counter': counter,
        'counter11': counter11,
        'counter12': counter12,
        'counter21': counter21,
        'counter22': counter22,
        'counter23': counter23,
        'counter24': counter24,
        'counter31': counter31,
        'counter32': counter32,
        'counter33': counter33,
        'counter34': counter34,
        'total':total
    }
    return render(request,template,context)

class MatchPointsView(generic.ListView):
    template_name = 'iplusers/match_status.html'
    context_object_name='cm'
    matchFixture.objects.filter(match_time__lte=timezone.now())
    def get_queryset(self):
        a = matchFixture.objects.filter(match_time__lte=timezone.now()).order_by('-match_id')
        return a

def UpdateResultsView(request):
    form_update = UpdateResultForm()

    if request.method=='POST':
        # print(request.POST)
        form_update = UpdateResultForm(request.POST)
        if form_update.is_valid():
            form_update.save()
            #update flags in FirstQuestion_entry
            #get match_id
            # print(request.POST['match_id'])
            match_id = request.POST['match_id']
            # print(match_id)
            # print(FirstQuestion_entry.objects.filter(match_id=match_id))
            instance = FirstQuestion_entry.objects.filter(match_id=match_id)
            total_entry = instance.count()
            ans1 = request.POST['q1_answer']
            ans2 = request.POST['q2_answer']
            ans3 = request.POST['q3_answer']
            for i in instance:
                # print(i.q1_select)
                if i.q1_select == ans1:
                    i.q1_flag = 1
                else:
                    i.q1_flag = 0
                if i.q2_select == ans2:
                    i.q2_flag = 1
                else:
                    i.q2_flag = 0
                if i.q3_select == ans3:
                    i.q3_flag = 1
                else:
                    i.q3_flag = 0
                i.save()
            flag_count1 = FirstQuestion_entry.objects.filter(q1_flag=1).count()
            flag_count2 = FirstQuestion_entry.objects.filter(q2_flag=1).count()
            flag_count3 = FirstQuestion_entry.objects.filter(q3_flag=1).count()

            losing_total_q1 = total_entry - flag_count1
            losing_total_q2 = total_entry - flag_count2
            losing_total_q3 = total_entry - flag_count3

            for i in instance:
                if i.q1_flag == 0:
                    if losing_total_q1 == total_entry:
                        i.q1_stake = 0
                    else:
                        i.q1_stake = -10

                else:
                    i.q1_stake = 10*(losing_total_q1/flag_count1)
                if i.q2_flag == 0:
                    if losing_total_q2 == total_entry:
                        i.q2_stake = 0
                    else:
                        i.q2_stake = -20
                else:
                    i.q2_stake = 20*(losing_total_q2/flag_count2)
                if i.q3_flag == 0:
                    if losing_total_q3 == total_entry:
                        i.q3_stake = 0
                    else:
                        i.q3_stake = -20
                else:
                    i.q3_stake = 20*(losing_total_q3/flag_count3)
                i.total_points = i.q1_stake + i.q2_stake + i.q3_stake
                i.pred_accuracy = (i.q1_flag + i.q2_flag + i.q3_flag)/3
                i.save()
            #update Leaderboard
    context ={
        'form_update':form_update
    }
    template = 'iplusers/update_result.html'
    return render(request, template, context)

def update_points(request):
    stake = FirstQuestion_entry.objects.values('player').annotate(Max('total_points'),Sum('total_points'),Avg('pred_accuracy'))
    print(stake)
    print(stake[1]['player'])
    print(len(stake))
    for i in range(0,len(stake)):
        print(stake[i]['player'])
        player_name = stake[i]['player']
        if Leaderboard.objects.filter(player=player_name).exists():
            update_instance = Leaderboard.objects.filter(player=player_name)
            update_instance.points=stake[i]['total_points__sum']
            update_instance.pred_acc=stake[i]['pred_accuracy__avg']
            update_instance.highest_stake=stake[i]['total_points__max']
            # update_instance.total_attempt=stake[i]['total_points__sum']
            print("Yes")

        else:
            new_entry = Leaderboard(player = stake[i]['player'], points=stake[i]['total_points__sum'], pred_acc=stake[i]['pred_accuracy__avg'],highest_stake=stake[i]['total_points__max'],total_attempt=0)
            new_entry.save()

    points = Leaderboard.objects.all()
    template_name = 'iplusers/leaderboard.html'
    context = {
        'stake': stake,
        'points':points,
    }

    return render(request, template_name, context)

def RulesView(request):
    template = 'iplusers/rules.html'
    return render(request,template)

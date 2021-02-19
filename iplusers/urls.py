from django.urls import path, re_path
from . import views

urlpatterns =[
    path('',views.indexView.as_view(), name='index'),
    path('register', views.register, name='register'),
    path('rules', views.RulesView, name ='rules'),
    path('upload', views.fixture_upload, name='upload'),
    path('matches', views.AllMatchView.as_view(), name='matches'),
    path('<match_id>/', views.vote, name='vote'),
    path('<match_id>/submit_vote', views.submit_vote, name='submitted'),
    path('match_status', views.CurrentMatchView.as_view(), name='match_status'),
    path('<match_id>/current_status', views.MatchStatusView, name='current_status'),
    path('match_points', views.MatchPointsView.as_view(), name='match_points'),
    path('update_result', views.UpdateResultsView, name='update_result'),
    path('leaderboard', views.update_points, name ='leaderboard'),



    # re_path(r'^(?P<match_id>[0-9]+)/$', views.vote, name = 'vote' ),

]

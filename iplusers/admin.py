from django.contrib import admin
from .models import matchFixture, FirstQuestion, FirstQuestion_entry, MatchPoints, Results, Leaderboard

# Register your models here.
admin.site.register(matchFixture)
admin.site.register(FirstQuestion)
admin.site.register(FirstQuestion_entry)
admin.site.register(MatchPoints)
admin.site.register(Results)
admin.site.register(Leaderboard)

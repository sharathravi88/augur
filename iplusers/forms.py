from django.forms import ModelForm
from iplusers.models import Results

class UpdateResultForm(ModelForm):
    class Meta:
        model = Results
        fields = ['match_id','q1_answer','q2_answer','q3_answer']

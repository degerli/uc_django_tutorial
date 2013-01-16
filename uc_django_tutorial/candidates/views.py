from django.views.generic import ListView

from uc_django_tutorial.candidates.models import Candidate

class CandidateListView(ListView):
    model = Candidate

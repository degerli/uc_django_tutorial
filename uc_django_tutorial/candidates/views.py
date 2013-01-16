from django.views.generic import ListView, UpdateView

from uc_django_tutorial.candidates.models import Candidate

class CandidateListView(ListView):
    model = Candidate

class CandidateUpdateView(UpdateView):
    model = Candidate
    success_url = '/'


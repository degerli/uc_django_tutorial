from django.conf.urls import patterns, include, url

from uc_django_tutorial.candidates.views import CandidateListView

urlpatterns = patterns('',
    url(r'^$', CandidateListView.as_view())
)

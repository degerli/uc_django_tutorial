from django.conf.urls import patterns, include, url

from uc_django_tutorial.candidates.views import (CandidateListView,
                                                 CandidateUpdateView)

urlpatterns = patterns('',
    url(r'^$', CandidateListView.as_view()),

    url(r'^candidate/(?P<pk>\d+)/$', CandidateUpdateView.as_view(),
            name='candidate-update')
)

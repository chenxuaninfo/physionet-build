from django.conf.urls import url
from django.urls import reverse_lazy

from . import views

urlpatterns = [
    url(r'^$', views.project_home, name='project_home'),
    url(r'^create/$', views.create_project, name='create_project'),

    url(r'^(?P<project_id>\d+)/$', views.edit_project, name='edit_project'),

    url(r'^(?P<project_id>\d+)/collaborators/$', views.project_collaborators, name='project_collaborators'),
    url(r'^(?P<project_id>\d+)/files/$', views.project_files, name='project_files'),
    url(r'^(?P<project_id>\d+)/metadata/$', views.project_metadata, name='project_metadata'),
]

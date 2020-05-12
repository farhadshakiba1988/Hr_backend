from django.urls import path

from api import views
from controller import RegisterController

proposal = [
    path('proposal-list/', views.proposallist, name='proposal-list'),
    path('proposal-update/<str:pk>', views.proposalupdate, name='proposal-update'),
    path('proposal-delete/<str:pk>', views.proposaldelete, name='proposal-delete'),
    path('proposal-create/', views.proposalcreate, name='proposal-ctreate'),
]


registerNamespace = 'register'
register = [
    path(registerNamespace+'/', RegisterController.index, name='register-index'),
    path(registerNamespace+'/jobs', RegisterController.jobs, name='register-jobs'),
    path(registerNamespace+'/ncode', RegisterController.ncode, name='register-ncode'),
    path(registerNamespace+'/upload', RegisterController.upload, name='register-upload'),
    path(registerNamespace+'/save', RegisterController.save, name='register-save'),
]

personnel = [
#     TO DO
]

urlpatterns = proposal + register + personnel

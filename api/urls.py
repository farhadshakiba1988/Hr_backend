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
    path(registerNamespace + '/', RegisterController.index, name='register-index'),
    path(registerNamespace + '/jobs', RegisterController.jobs, name='register-jobs'),
    path(registerNamespace + '/ncode', RegisterController.ncode, name='register-ncode'),
    path(registerNamespace + '/upload', RegisterController.upload, name='register-upload'),
    path(registerNamespace + '/save', RegisterController.save, name='register-save'),
]

registerNamespace = 'personnel'
personnel = [
    path(registerNamespace + '/list', RegisterController.jobs, name='personnel-list'),
    path(registerNamespace + '/delete', RegisterController.ncode, name='personnel-delete'),
    path(registerNamespace + '/upload', RegisterController.upload, name='personnel-upload'),
    path(registerNamespace + '/create', RegisterController.save, name='personnel-create'),
]

registerNamespace = 'proposalInterview'
proposalInterview = [
    path(registerNamespace + '/list', RegisterController.jobs, name='proposalInterview-list'),
    path(registerNamespace + '/delete', RegisterController.ncode, name='proposalInterview-delete'),
    path(registerNamespace + '/upload', RegisterController.upload, name='proposalInterview-upload'),
    path(registerNamespace + '/create', RegisterController.save, name='proposalInterview-create'),
]

registerNamespace = 'proposalFamily'
proposalFamily = [
    path(registerNamespace + '/list', RegisterController.jobs, name='proposalFamily-list'),
    path(registerNamespace + '/delete', RegisterController.ncode, name='proposalFamily-delete'),
    path(registerNamespace + '/upload', RegisterController.upload, name='proposalFamily-upload'),
    path(registerNamespace + '/create', RegisterController.save, name='proposalFamily-create'),
]

registerNamespace = 'proposalEducation'
proposalEducation = [
    path(registerNamespace + '/list', RegisterController.jobs, name='proposalEducation-list'),
    path(registerNamespace + '/delete', RegisterController.ncode, name='proposalEducation-delete'),
    path(registerNamespace + '/upload', RegisterController.upload, name='proposalEducation-upload'),
    path(registerNamespace + '/create', RegisterController.save, name='proposalEducation-create'),
]

registerNamespace = 'personnelEstimate'
personnelEstimate = [
    path(registerNamespace + '/list', RegisterController.jobs, name='personnelEstimate-list'),
    path(registerNamespace + '/delete', RegisterController.ncode, name='personnelEstimate-delete'),
    path(registerNamespace + '/upload', RegisterController.upload, name='personnelEstimate-upload'),
    path(registerNamespace + '/create', RegisterController.save, name='personnelEstimate-create'),
]

registerNamespace = 'personnelContract'
personnelContract = [
    path(registerNamespace + '/list', RegisterController.jobs, name='personnelContract-list'),
    path(registerNamespace + '/delete', RegisterController.ncode, name='personnelContract-delete'),
    path(registerNamespace + '/upload', RegisterController.upload, name='personnelContract-upload'),
    path(registerNamespace + '/create', RegisterController.save, name='personnelContract-create'),
]

urlpatterns = (proposal + register + personnel +
personnelContract + personnelEstimate + proposalEducation +
               proposalFamily + proposalInterview)

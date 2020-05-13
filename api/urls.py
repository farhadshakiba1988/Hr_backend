from django.urls import path

from api import views
from controller import *

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
    path(registerNamespace + '/update', RegisterController.upload, name='personnel-update'),
    path(registerNamespace + '/create', RegisterController.save, name='personnel-create'),
]

registerNamespace = 'proposalInterview'
proposalInterview = [
    path(registerNamespace + '/list', ProposalInterviewController.list, name='proposalInterview-list'),
    path(registerNamespace + '/delete', ProposalInterviewController.delete, name='proposalInterview-delete'),
    path(registerNamespace + '/update', ProposalInterviewController.update, name='proposalInterview-update'),
    path(registerNamespace + '/create', ProposalInterviewController.create, name='proposalInterview-create'),
]

registerNamespace = 'proposalFamily'
proposalFamily = [
    path(registerNamespace + '/list', ProposalFamilyController.list, name='proposalFamily-list'),
    path(registerNamespace + '/delete', ProposalFamilyController.delete, name='proposalFamily-delete'),
    path(registerNamespace + '/update', ProposalFamilyController.update, name='proposalFamily-update'),
    path(registerNamespace + '/create', ProposalFamilyController.create, name='proposalFamily-create'),
]

registerNamespace = 'proposalEducation'
proposalEducation = [
    path(registerNamespace + '/list', ProposalEducationController.list, name='proposalEducation-list'),
    path(registerNamespace + '/delete', ProposalEducationController.delete, name='proposalEducation-delete'),
    path(registerNamespace + '/update', ProposalEducationController.update, name='proposalEducation-update'),
    path(registerNamespace + '/create', ProposalEducationController.create, name='proposalEducation-create'),
]

registerNamespace = 'personnelEstimate'
personnelEstimate = [
    path(registerNamespace + '/list', PersonnelEstimateController.list, name='personnelEstimate-list'),
    path(registerNamespace + '/delete', PersonnelEstimateController.delete, name='personnelEstimate-delete'),
    path(registerNamespace + '/update', PersonnelEstimateController.update, name='personnelEstimate-update'),
    path(registerNamespace + '/create', PersonnelEstimateController.create, name='personnelEstimate-create'),
]

registerNamespace = 'personnelContract'
personnelContract = [
    path(registerNamespace + '/list', PersonnelContractController.list, name='personnelContract-list'),
    path(registerNamespace + '/delete', PersonnelContractController.delete, name='personnelContract-delete'),
    path(registerNamespace + '/update', PersonnelContractController.update, name='personnelContract-update'),
    path(registerNamespace + '/create', PersonnelContractController.create, name='personnelContract-create'),
]

urlpatterns = (proposal + register + personnel +
personnelContract + personnelEstimate + proposalEducation +
               proposalFamily + proposalInterview)

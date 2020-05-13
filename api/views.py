from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import *
from api.serializers import *


@api_view(['GET'])
def proposallist(request):
    try:
        proposal = Proposal.objects.all()
    except Proposal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProposalSerializers(proposal, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def proposalcreate(request):
    serializer = ProposalSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def proposalupdate(request, pk):
    proposal = Proposal.objects.get(id=pk)
    serializer = ProposalSerializers(instance=proposal, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def proposaldelete(request, pk):
    proposal = Proposal.objects.get(id=pk)
    proposal.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def personnellist(request):
    try:
        personnel = Personnel.objects.all()
    except Proposal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonnelSerializers(personnel, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def personnelcreate(request):
    serializer = PersonnelSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def personnelupdate(request, pk):
    personnel = Personnel.objects.get(id=pk)
    serializer = PersonnelSerializers(instance=personnel, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def personneldelete(request, pk):
    personnel = Personnel.objects.get(id=pk)
    personnel.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def proposalInterviewlist(request):
    try:
        proposalInterview = ProposalInterview.objects.all()
    except Proposal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProposalInterviewSerializers(proposalInterview, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def proposalInterviewcreate(request):
    serializer = ProposalInterviewSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def proposalInterviewupdate(request, pk):
    proposalInterview = ProposalInterview.objects.get(id=pk)
    serializer = ProposalInterviewSerializers(instance=proposalInterview, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def proposalInterviewdelete(request, pk):
    proposalInterview = ProposalInterview.objects.get(id=pk)
    proposalInterview.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def proposalFamilylist(request):
    try:
        proposalFamily = ProposalFamily.objects.all()
    except Proposal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProposalFamilySerializers(proposalFamily, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def proposalFamilycreate(request):
    serializer = ProposalFamilySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def proposalFamilyupdate(request, pk):
    proposalFamily = ProposalFamily.objects.get(id=pk)
    serializer = ProposalFamilySerializers(instance=proposalFamily, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def proposalFamilydelete(request, pk):
    proposalFamily = ProposalFamily.objects.get(id=pk)
    proposalFamily.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def proposalEducationlist(request):
    try:
        proposalEducation = ProposalEducation.objects.all()
    except Proposal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProposalEducationSerializers(proposalEducation, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def proposalEducationcreate(request):
    serializer = ProposalEducationSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def proposalEducationupdate(request, pk):
    proposalEducation = ProposalEducation.objects.get(id=pk)
    serializer = ProposalEducationSerializers(instance=proposalEducation, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def proposalEducationdelete(request, pk):
    proposalEducation = ProposalEducation.objects.get(id=pk)
    proposalEducation.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def personnelEstimatelist(request):
    try:
        personnelEstimate = PersonnelEstimate.objects.all()
    except Proposal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProposalEducationSerializers(personnelEstimate, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def personnelEstimatecreate(request):
    serializer = ProposalEducationSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def personnelEstimateupdate(request, pk):
    personnelEstimate = PersonnelEstimate.objects.get(id=pk)
    serializer = ProposalEducationSerializers(instance=personnelEstimate, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def personnelEstimatedelete(request, pk):
    personnelEstimate = PersonnelEstimate.objects.get(id=pk)
    personnelEstimate.delete()
    return Response('Item succsesfuly deleted')


# @api_view(['GET'])
# def personnelContractlist(request):
#     try:
#         personnelContract = PersonnelContract.objects.all()
#     except Proposal.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = PersonnelContractSerializers(personnelContract, many=True)
#         return Response(serializer.data)
@api_view(['GET'])
def personnelContractlist(request):
    personnelContract = PersonnelContract.objects.all()
    serializer = PersonnelContractSerializers(personnelContract, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def personnelContractcreate(request):
    serializer = PersonnelContractSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def personnelContractupdate(request, pk):
    personnelContract = PersonnelContract.objects.get(id=pk)
    serializer = PersonnelContractSerializers(instance=personnelContract, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def personnelContractdelete(request, pk):
    personnelContract = PersonnelContract.objects.get(id=pk)
    personnelContract.delete()
    return Response('Item succsesfuly deleted')

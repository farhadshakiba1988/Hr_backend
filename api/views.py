from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Proposal
from api.serializers import ProposalSerializers


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

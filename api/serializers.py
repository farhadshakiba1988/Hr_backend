from rest_framework import serializers

from api.models import *


class ProposalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'


class PersonnelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'


class ProposalInterviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProposalInterview
        fields = '__all__'


class ProposalFamilySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProposalFamily
        fields = '__all__'


class ProposalEducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProposalEducation
        fields = '__all__'


class PersonnelEstimateSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonnelEstimate
        fields = '__all__'


class PersonnelContractSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonnelContract
        fields = '__all__'


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

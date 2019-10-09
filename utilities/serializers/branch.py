from rest_framework import serializers

from utilities.models import Branch


class BranchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Branch
        field = '__all__'
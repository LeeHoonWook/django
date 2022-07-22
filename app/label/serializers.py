from rest_framework import serializers
from app.models import Labels


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Labels
        fields = "__all__"

    def create(self, data, commit=True):
        instance = Labels()
        instance.label = data.get("label")

        if commit:
            instance.save()

        return instance

    def update(self, data, pk, commit=True):
        instance = Labels.objects.get(pk=pk)
        instance.label = data.get("label")

        if commit:
            instance.save()

        return instance

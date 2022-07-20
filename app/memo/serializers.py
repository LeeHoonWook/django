from rest_framework import serializers
from app.models import Users, Memos, Labels


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ["username", "user_auth", "hint", "date_joined", "last_login"]


class MemoSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True)

    class Meta:
        model = Memos
        fields = "__all__"

    def create(self, request, data, commit=True):
        instance = Memos()
        instance.writer_id = request.user.id
        instance.title = data.get("title")
        instance.content = data.get("content")
        if request.FILES.get('img') != None:
            instance.img = request.FILES['img']
        labels = data.get('labels')
        if commit:
            try:
                instance.save()
            except Exception as e:
                print(e)
            else:
                if labels:
                    for i in labels:
                        instance.labels.add(Labels.objects.get(pk=i))

        return instance

    def update(self, request, data, pk, commit=True):
        instance = Memos.objects.get(pk=pk)
        instance.title = data.get('title')
        instance.content = data.get('content')

        if commit:
            if request.FILES.get('img') != None:
                instance.img = request.FILES['img']

            instance.save()

        return instance


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

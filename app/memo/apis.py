from app.models import Memos, Labels
from rest_framework import viewsets
from .serializers import MemoSerializer, LabelSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import renderer_classes, action
from rest_framework.renderers import JSONRenderer
from django.http.response import Http404
from app.utils import MsgOk


class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memos.objects.order_by("-created_at")
    serializer_class = MemoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        # POST METHOD
        serializer = MemoSerializer(data=request.data)

        if serializer.is_valid():
            rtn = serializer.create(request, serializer.data)

            return Response(MemoSerializer(rtn).data, status=status.HTTP_201_CREATED)
        else:
            return Response('필수 항목 : 제목 + 내용', status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        # PUT METHOD
        serializer = MemoSerializer(data=request.data)

        if serializer.is_valid():
            rtn = serializer.update(request, serializer.data, pk)

            return Response(MemoSerializer(rtn).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @renderer_classes([JSONRenderer])
    def destroy(self, request, pk=None):
        # DELETE METHOD
        queryset = self.get_queryset().filter(pk=pk)

        if not queryset.exists():

            raise Http404

        queryset.delete()

        return MsgOk()

    @action(detail=True, methods=["get", "post"])
    def add_click(self, request, pk=None):
        queryset = self.get_queryset().filter(pk=pk)

        if not queryset.exists():

            raise Http404

        rtn = queryset.first().clicked()
        serializer = MemoSerializer(rtn)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Labels.objects.order_by("-created_at")
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        # POST METHOD
        serializer = LabelSerializer(data=request.data)

        if serializer.is_valid():
            rtn = serializer.create(serializer.data)

            return Response(LabelSerializer(rtn).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        # PUT METHOD
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.update(request, serializer.data, pk)

            return Response(LabelSerializer(rtn).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @renderer_classes([JSONRenderer])
    def destroy(self, request, pk=None):
        # DELETE METHOD
        queryset = self.get_queryset().filter(pk=pk)

        if not queryset.exists():

            raise Http404

        queryset.delete()

        return MsgOk()

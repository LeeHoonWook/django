from app.models import Labels
from rest_framework import viewsets
from .serializers import LabelSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from django.http.response import Http404
from app.utils import MsgOk


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
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def update(self, request, pk=None):
        # PUT METHOD
        serializer = LabelSerializer(data=request.data)

        if serializer.is_valid():
            rtn = serializer.update(request, serializer.data, pk)

            return Response(LabelSerializer(rtn).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @renderer_classes([JSONRenderer])
    def destroy(self, request, pk=None):
        # DELETE METHOD
        queryset = self.get_queryset().filter(pk=pk)

        if not queryset.exists():

            raise Http404

        queryset.delete()

        return MsgOk()

    '''
    def list(self, request):
        # GET ALL
        queryset = self.get_queryset().all()
        serializer = LabelSerializer(queryset, many=True)

        # 참고 사항
        # content = JSONRenderer().render(serializer.data)
        # stream = io.BytesIO(content)
        # data = JSONParser().parse(stream)

        return Response(serializer.data)
        
    def retrieve(self, request, pk=None):
        # Detail GET
        queryset = self.get_queryset().filter(pk=pk).first()
        serializer = LabelSerializer(queryset)

        return Response(serializer.data)
    '''

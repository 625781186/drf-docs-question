# coding=utf-8
from django.http import JsonResponse

from rest_framework.decorators import action
from rest_framework import mixins, permissions, status
from rest_framework import viewsets

from .models import UWorksmain
from . import serializers as S
from .serializers import WorksmainBulkSerializer


class WorksMainViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated, permissions.IsAuthenticatedOrReadOnly)
    # authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = S.WorksmainSerializer

    ## ------------------------------
    from django_filters.rest_framework import DjangoFilterBackend
    from rest_framework import filters

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    search_fields = ['name']

    def get_queryset(self):

        return UWorksmain.objects.filter(pk_user_main = self.request.user)

    ## ------------------------------

    def get_serializer_class(self):
        if self.action == 'bulk_operation':
            serializer_class = WorksmainBulkSerializer
            return serializer_class
        else:
            return super(WorksMainViewSet, self).get_serializer_class()

    @action(methods = ['delete', 'patch'], detail = False)
    def bulk_operation(self, request, *args, **kwargs):
        """

        patch:
        bulk update worksmain.

        delete:
        bulk delete worksmain.
        """
        serializer = self.get_serializer(data = request.data)  # type: WorksmainBulkSerializer
        serializer.is_valid(raise_exception = True)
        if request.method == "DELETE":
            bulk_list = serializer.validated_data['bulk_list']
            self.get_queryset().filter(pk_works_main__in = bulk_list).delete()
            return JsonResponse(serializer.data, status = status.HTTP_204_NO_CONTENT)
        else:
            bulk_list = serializer.validated_data['bulk_list']
            pk_atlas_main = serializer.validated_data['atlas_id']
            self.get_queryset().filter(pk_works_main__in = bulk_list).update(pk_atlas_main = ...)
            return JsonResponse(serializer.data, status = status.HTTP_204_NO_CONTENT)

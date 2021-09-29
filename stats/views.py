from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from stats.models import Statictic
from stats.serializers import StatisticSerializer


class StaticticViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Statictic.objects.order_by('date')
    serializer_class = StatisticSerializer


    def get_queryset(self):
        _from = parse_date(self.request.query_params.get('from', ''))
        _to = parse_date(self.request.query_params.get('to', ''))
        
        if _from:
            self.queryset = self.queryset.filter(date__gte=_from)
        if _to:
            self.queryset = self.queryset.filter(date__lte=_to)
        return self.queryset


    @action(["DELETE"], detail=False)
    def delete(self, request):
        try:
            deleted, _ = Statictic.objects.all().delete()
            error = ''
        except Exception as e:
            deleted = 0
            error = str(e)

        return Response(
            {'error': error, 'deleted': deleted},
            status=status.HTTP_200_OK,
        )

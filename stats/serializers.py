from rest_framework import serializers
from stats.models import Statictic


class StatisticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statictic
        fields = ['date', 'views', 'clicks', 'cost', 'cpc', 'cpm']

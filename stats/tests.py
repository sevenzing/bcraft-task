from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from stats.models import Statictic


def now(delta_days=0):
    return (timezone.now() + timedelta(days=delta_days)).strftime('%Y-%m-%d')


class StatsTestCase(APITestCase):
    def test_create(self):
        res = self.client.post('/api/statistic/', {'date': now()})
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Statictic.objects.count(), 1)

        res = self.client.post('/api/statistic/', {'date': now(), 'views': 1, 'clicks': 1, 'cost': 1,})
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Statictic.objects.count(), 2)


    def test_get(self):
        self.client.post('/api/statistic/', {'date': '2000-01-01', 'views': 1, 'clicks': 1, 'cost': 1,})
        self.client.post('/api/statistic/', {'date': now(), 'views': 1, 'clicks': 1, 'cost': 1,})
        
        response = self.client.get(f'/api/statistic/?from={now()}')
        self.assertEqual(len(response.json()), 1)

        self.client.post('/api/statistic/', {'date': now(365), 'views': 1, 'clicks': 1, 'cost': 1,})

        response = self.client.get(f'/api/statistic/?from={now()}&to={now(10)}')        
        self.assertEqual(len(response.json()), 1)

    def test_delete(self):
        self.client.post('/api/statistic/', {'date': '2000-01-01', 'views': 1, 'clicks': 1, 'cost': 1,})
        self.client.post('/api/statistic/', {'date': now(), 'views': 1, 'clicks': 1, 'cost': 1,})
        self.client.post('/api/statistic/', {'date': now(365), 'views': 1, 'clicks': 1, 'cost': 1,})

        self.client.delete('/api/statistic/')


        response = self.client.get(f'/api/statistic/')        
        self.assertEqual(len(response.json()), 0)



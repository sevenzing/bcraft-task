from django.db import models
import typing


class Statictic(models.Model):
    date = models.DateField()
    views = models.IntegerField(null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    @property
    def cpc(self) -> typing.Optional[float]:
        if self.cost and self.clicks:
            if self.clicks == 0:
                return float('inf')
            else:
                return self.cost / self.clicks
    
    @property
    def cpm(self) -> typing.Optional[float]:
        if self.cost and self.views:
            if self.views == 0:
                return float('inf')
            else:
                return self.cost / self.views * 1000




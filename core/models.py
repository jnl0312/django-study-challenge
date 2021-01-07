from django.db import models


class TimeStampedModel(models.Model):
    """ Time Stamped Model Definition """

    """ model이 생성된 날짜 구하기 : auto_now_add
    model 업데이트 : auto_now """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

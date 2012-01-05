from django.db import models


class Model(models.Model):

    class meta:
        managed = False

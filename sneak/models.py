from django.db import models
from dardive.models import CommandConfig


class SneakModel(CommandConfig):

    class Meta:
        abstract = True

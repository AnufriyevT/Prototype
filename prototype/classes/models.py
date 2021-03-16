from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Entity(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        abstract = True


class Diagram(Entity):
    pass


class Domain(Entity):
    pass


class FeasibleDomain(Domain):
    pass


class StrategicDomain(FeasibleDomain):
    pass


class CurrentDomain(StrategicDomain):
    pass


class Vocabulary(models.Model):
    domain = models.OneToOneField(CurrentDomain, on_delete=models.SET_NULL, null=True)


class DomainSpecific(Vocabulary):
    pass


class NonDomainSpecific(Vocabulary):
    pass


class Product(models.Model):
    name = models.CharField(max_length=256)
    domain = models.ForeignKey(CurrentDomain, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self')
    users = models.ManyToManyField(User)


class API(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)


class Family(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)


class Suite(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)


class Standard(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)


class DataFormat(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)


class Producer(models.Model):
    name = models.CharField(max_length=256)
    competitors = models.ManyToManyField('self')


class Retail(User):
    pass


class StandardRetail(Retail):
    pass


class VolumeRetail(Retail):
    pass


class Academic(User):
    pass


class SingleAcademic(Academic):
    pass


class VolumeAcademic(Academic):
    pass

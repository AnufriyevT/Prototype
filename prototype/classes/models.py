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
    definition = models.TextField()


class Vocabulary(models.Model):
    domain = models.OneToOneField(CurrentDomain, on_delete=models.SET_NULL, null=True)


class DomainSpecific(Vocabulary):
    acronyms = models.CharField(max_length=512)
    symbols = models.CharField(max_length=512)
    terms = models.CharField(max_length=512)


class NonDomainSpecific(Vocabulary):
    acronyms = models.CharField(max_length=512)
    symbols = models.CharField(max_length=512)
    terms = models.CharField(max_length=512)


class Product(models.Model):
    name = models.CharField(max_length=256)
    domain = models.ForeignKey(CurrentDomain, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self')
    users = models.ManyToManyField(User)
    description = models.TextField()
    input_formats = models.ManyToManyField('DataFormat', related_name='inputs')
    output_formats = models.ManyToManyField('DataFormat', related_name='outputs')


class API(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)


class Family(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)
    description = models.TextField()


class Suite(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)


class Standard(models.Model):
    name = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)
    description = models.TextField()


class DataFormat(models.Model):
    type = models.CharField(max_length=256)
    read_write = models.BooleanField()


class Producer(models.Model):
    name = models.CharField(max_length=256)
    competitors = models.ManyToManyField('self')
    leader = models.BooleanField()


class MarketSegment(User):
    pass


class Retail(MarketSegment):
    pass


class StandardRetail(Retail):
    simple_cost = models.FloatField()
    upgrade_cost = models.FloatField()


class VolumeRetail(Retail):
    simple_cost = models.FloatField()
    upgrade_cost = models.FloatField()


class Academic(MarketSegment):
    pass


class SingleAcademic(Academic):
    simple_cost = models.FloatField()
    upgrade_cost = models.FloatField()


class VolumeAcademic(Academic):
    simple_cost = models.FloatField()
    upgrade_cost = models.FloatField()

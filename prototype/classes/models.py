from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Domain(models.Model):
    feasible = models.TextField()
    current = models.TextField()
    strategic = models.TextField()


class Vocabulary(models.Model):
    term = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return self.term


class Producer(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Value(models.Model):
    internal = models.TextField()
    external = models.TextField()


class StandardPrice(models.Model):
    cost = models.FloatField(blank=True, null=True)
    upgrade = models.FloatField(blank=True, null=True)


class VolumePrice(models.Model):
    cost = models.FloatField(blank=True, null=True)
    upgrade = models.FloatField(blank=True, null=True)


class Retail(models.Model):
    standard = models.ForeignKey(StandardPrice, on_delete=models.SET_NULL, null=True, blank=True)
    volume = models.ForeignKey(VolumePrice, on_delete=models.SET_NULL, null=True, blank=True)


class Academic(models.Model):
    standard = models.ForeignKey(StandardPrice, on_delete=models.SET_NULL, null=True, blank=True)
    volume = models.ForeignKey(VolumePrice, on_delete=models.SET_NULL, null=True, blank=True)


class Pricing(models.Model):
    retail = models.ForeignKey(Retail, on_delete=models.SET_NULL, null=True, blank=True)
    academic = models.ForeignKey(Academic, on_delete=models.SET_NULL, null=True, blank=True)


class Standard(models.Model):
    name = models.CharField(max_length=512, blank=False)

    def __str__(self):
        return self.name


class Input(models.Model):
    name = models.CharField(max_length=512, blank=False)

    def __str__(self):
        return self.name


class Output(models.Model):
    name = models.CharField(max_length=512, blank=False)

    def __str__(self):
        return self.name


class DataFormat(models.Model):
    input = models.ManyToManyField(Input)
    output = models.ManyToManyField(Output)


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Name", help_text="Enter name", null=False, blank=False)
    description = models.TextField("Description", help_text="Enter description")
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=False)
    leader = models.BooleanField()
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    standards = models.ManyToManyField(Standard)
    pricing = models.ForeignKey(Pricing, on_delete=models.SET_NULL, null=True)
    data_format = models.ForeignKey(DataFormat, on_delete=models.SET_NULL, null=True)
    complementary_products = models.ManyToManyField("self", null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=512)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    vocabulary = models.ManyToManyField(Vocabulary)
    product = models.ManyToManyField(Product)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

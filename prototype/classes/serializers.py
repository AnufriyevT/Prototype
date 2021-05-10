from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Project, Domain, Vocabulary, Product, Producer, Value, Standard, DataFormat, Pricing, Retail, \
    Academic, StandardPrice, VolumePrice, Input, Output


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = (
            '__all__'
        )


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = (
            '__all__'
        )


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = (
            '__all__'
        )


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = (
            '__all__'
        )


class StandardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = (
            '__all__'
        )


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = (
            '__all__'
        )


class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = (
            '__all__'
        )


class DataFormatSerializer(WritableNestedModelSerializer):
    input = InputSerializer(many=True)
    output = OutputSerializer(many=True)

    class Meta:
        model = DataFormat
        fields = (
            '__all__'
        )


class StandardPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardPrice
        fields = (
            '__all__'
        )


class VolumePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumePrice
        fields = (
            '__all__'
        )


class RetailSerializer(WritableNestedModelSerializer):
    standard = StandardPriceSerializer()
    volume = VolumePriceSerializer()

    class Meta:
        model = Retail
        fields = (
            '__all__'
        )


class AcademicSerializer(WritableNestedModelSerializer):
    standard = StandardPriceSerializer()
    volume = VolumePriceSerializer()

    class Meta:
        model = Academic
        fields = (
            '__all__'
        )


class PricingSerializer(WritableNestedModelSerializer):
    retail = RetailSerializer()
    academic = AcademicSerializer()

    class Meta:
        model = Pricing
        fields = (
            '__all__'
        )


class ProductSerializer(WritableNestedModelSerializer):
    producer = ProducerSerializer()
    value = ValueSerializer()
    standards = StandardsSerializer(many=True)
    data_format = DataFormatSerializer()
    pricing = PricingSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'producer',
            'leader',
            'value',
            'standards',
            'pricing',
            'data_format',
            'complementary_products',
        )


class ProjectSerializer(WritableNestedModelSerializer):
    domain = DomainSerializer()
    vocabulary = VocabularySerializer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'domain',
            'vocabulary',
            'product',
            'author',
        )
        extra_kwargs = {
            'author': {'read_only': True},
        }

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


class DataFormatSerializer(serializers.ModelSerializer):
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


class RetailSerializer(serializers.ModelSerializer):
    standard = StandardPriceSerializer()
    volume = VolumePriceSerializer()

    class Meta:
        model = Retail
        fields = (
            '__all__'
        )


class AcademicSerializer(serializers.ModelSerializer):
    standard = StandardPriceSerializer()
    volume = VolumePriceSerializer()

    class Meta:
        model = Academic
        fields = (
            '__all__'
        )


class PricingSerializer(serializers.ModelSerializer):
    retail = RetailSerializer()
    academic = AcademicSerializer()

    class Meta:
        model = Pricing
        fields = (
            '__all__'
        )


class ProductSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer()
    value = ValueSerializer()
    standards = StandardsSerializer(many=True)
    data_format = DataFormatSerializer()
    pricing = PricingSerializer()

    class Meta:
        model = Product
        fields = (
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


class ProjectSerializer(serializers.ModelSerializer):
    domain = DomainSerializer()
    vocabulary = VocabularySerializer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'name',
            'domain',
            'vocabulary',
            'product',
            'author',
        )
        extra_kwargs = {
            'author': {'read_only': True},
        }

    def create_vocabulary(self, validated_data, project):
        vocabularies = validated_data.pop('vocabulary')
        for vocabulary in vocabularies:
            voc = Vocabulary.objects.create()
            voc.term = vocabulary.get('term')
            voc.description = vocabulary.get('description')
            voc.save()
            project.vocabulary.add(voc)
        project.save()

    def create_domain(self, validated_data, project):
        domain = validated_data.pop('domain')
        dom = Domain.objects.create()
        dom.feasible = domain.get('feasible')
        dom.strategic = domain.get('strategic')
        dom.current = domain.get('current')
        project.domain = dom
        project.save()

    def create_product(self, validated_data, project):
        product = validated_data.pop('product')
        prod = Product.objects.create()
        prod.name = product.get('name')
        prod.description = product.get('description')
        prod.producer = product.get('producer')
        prod.leader = product.get('leader')
        prod.value = product.get('value')
        prod.standards = product.get('standards')
        prod.pricing = product.get('pricing')
        prod.data = product.get('data_format')
        prod.complementary_products = product.get('complementary_products')
        project.product = product
        project.save()

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        self.create_vocabulary(validated_data, project)
        self.create_domain(validated_data, project)
        self.create_product(validated_data, project)

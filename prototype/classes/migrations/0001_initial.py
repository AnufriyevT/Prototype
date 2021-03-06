# Generated by Django 3.2 on 2021-04-25 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DataFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feasible', models.TextField()),
                ('current', models.TextField()),
                ('strategic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.academic')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name', max_length=256, verbose_name='Name')),
                ('description', models.TextField(help_text='Enter description', verbose_name='Description')),
                ('leader', models.BooleanField()),
                ('complementary_products', models.ManyToManyField(blank=True, null=True, related_name='_classes_product_complementary_products_+', to='classes.Product')),
                ('data_format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.dataformat')),
                ('pricing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.pricing')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.producer')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='StandardPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(blank=True, null=True)),
                ('upgrade', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal', models.TextField()),
                ('external', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=512)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VolumePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(blank=True, null=True)),
                ('upgrade', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.standardprice')),
                ('volume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.volumeprice')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.domain')),
                ('product', models.ManyToManyField(to='classes.Product')),
                ('vocabulary', models.ManyToManyField(to='classes.Vocabulary')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='standards',
            field=models.ManyToManyField(to='classes.Standard'),
        ),
        migrations.AddField(
            model_name='product',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.value'),
        ),
        migrations.AddField(
            model_name='pricing',
            name='retail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.retail'),
        ),
        migrations.AddField(
            model_name='dataformat',
            name='input',
            field=models.ManyToManyField(to='classes.Input'),
        ),
        migrations.AddField(
            model_name='dataformat',
            name='output',
            field=models.ManyToManyField(to='classes.Output'),
        ),
        migrations.AddField(
            model_name='academic',
            name='standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.standardprice'),
        ),
        migrations.AddField(
            model_name='academic',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.volumeprice'),
        ),
    ]

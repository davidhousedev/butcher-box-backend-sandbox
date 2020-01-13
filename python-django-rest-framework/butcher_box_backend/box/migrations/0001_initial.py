# Generated by Django 3.0.1 on 2019-12-27 17:59

import box.models.box_item
import box.models.box_type
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('shipped', models.DateTimeField(default=None, help_text='The date and time that this box was shipped.', null=True)),
                ('delivered', models.DateTimeField(default=None, help_text='The date and time this box was reported delivered.', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoxType',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(help_text='User-readable classification of this box type, e.g. "All Beef"', max_length=63)),
                ('description', models.CharField(help_text='User-readable description of this box type.', max_length=511)),
                ('_type', models.CharField(choices=[(box.models.box_type.BoxTypes['CUSTOM'], 'custom'), (box.models.box_type.BoxTypes['STATIC'], 'static'), (box.models.box_type.BoxTypes['ASSORTED'], 'assorted')], db_column='type', help_text='Specifies how box items will be included in this box type. Will they be chosen by the user? Are they always the same?', max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoxItem',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('_type', models.CharField(choices=[(box.models.box_item.BoxItemTypes['SUBSCRIPTION'], 'subscription'), (box.models.box_item.BoxItemTypes['PROMOTION'], 'promotion'), (box.models.box_item.BoxItemTypes['OFFER'], 'offer'), (box.models.box_item.BoxItemTypes['ADDON'], 'addon')], db_column='type', default='SUBSCRIPTION', max_length=63)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='box_items', to='box.Box')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='box',
            name='_type',
            field=models.ForeignKey(db_column='type', help_text='The abstract description of this box.', on_delete=django.db.models.deletion.PROTECT, to='box.BoxType'),
        ),
        migrations.AddField(
            model_name='box',
            name='customer',
            field=models.ForeignKey(help_text='Who was billed for this box.', on_delete=django.db.models.deletion.PROTECT, to='customer.Customer'),
        ),
    ]

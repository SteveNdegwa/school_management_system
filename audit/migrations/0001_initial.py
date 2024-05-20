# Generated by Django 5.0.4 on 2024-05-20 01:52

import base.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('eusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.ForeignKey(default=base.models.State.default_state, on_delete=django.db.models.deletion.CASCADE, to='base.state')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('source_ip', models.CharField(blank=True, max_length=100, null=True)),
                ('request_data', models.TextField(blank=True, null=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('notification_response', models.TextField(blank=True, null=True)),
                ('successful', models.BooleanField(default=False)),
                ('euser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eusers.euser')),
                ('state', models.ForeignKey(default=base.models.State.default_state, on_delete=django.db.models.deletion.CASCADE, to='base.state')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.transactiontype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
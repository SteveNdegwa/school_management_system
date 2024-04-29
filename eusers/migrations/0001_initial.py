# Generated by Django 3.2.18 on 2024-04-28 18:51

import base.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractEUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('other_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('id_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('other_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('state', models.ForeignKey(default=base.models.State.default_state, on_delete=django.db.models.deletion.CASCADE, to='base.state')),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('abstracteuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eusers.abstracteuser')),
            ],
            options={
                'abstract': False,
            },
            bases=('eusers.abstracteuser',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('abstracteuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eusers.abstracteuser')),
                ('tsc_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.role')),
            ],
            options={
                'abstract': False,
            },
            bases=('eusers.abstracteuser',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('other_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('admission_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('state', models.ForeignKey(default=base.models.State.default_state, on_delete=django.db.models.deletion.CASCADE, to='base.state')),
                ('guardian', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guardian', to='eusers.guardian')),
                ('other_guardian', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_guardian', to='eusers.guardian')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('abstracteuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eusers.abstracteuser')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.role')),
            ],
            options={
                'abstract': False,
            },
            bases=('eusers.abstracteuser',),
        ),
    ]
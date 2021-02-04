# Generated by Django 3.1.6 on 2021-02-04 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=25, verbose_name='Group Name')),
                ('group_Description', models.TextField(max_length=200, verbose_name='Details')),
                ('members', models.ManyToManyField(null=True, to='billsplit.AppUser', verbose_name='members')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Amount')),
                ('description', models.TextField(max_length=200, verbose_name='Details')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billsplit.appuser')),
            ],
        ),
    ]

# Generated by Django 3.1.4 on 2021-05-29 07:48

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
            name='AmazeUsersOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderName', models.CharField(max_length=500)),
                ('orderAddress', models.CharField(max_length=1000)),
                ('orderCost', models.FloatField()),
                ('orderStatus', models.CharField(max_length=100)),
                ('orderOtp', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('userInstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userMode', models.CharField(max_length=1)),
                ('adafruitToken', models.CharField(default='', max_length=1000)),
                ('adafruitUserName', models.CharField(default='', max_length=500)),
                ('userInstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AmazeWarriorsOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppHome.amazeusersorders')),
                ('userInstance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

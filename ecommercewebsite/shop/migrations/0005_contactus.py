# Generated by Django 3.1.6 on 2021-06-29 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_totalprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('issue', models.TextField()),
            ],
        ),
    ]

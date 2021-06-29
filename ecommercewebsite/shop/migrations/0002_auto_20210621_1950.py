# Generated by Django 3.1.6 on 2021-06-22 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('catagory', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('size', models.CharField(max_length=5)),
                ('image', models.CharField(max_length=350)),
            ],
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
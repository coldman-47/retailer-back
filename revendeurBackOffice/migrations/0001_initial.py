# Generated by Django 5.1.2 on 2024-10-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tig_id', models.IntegerField(default=-1)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('category', models.IntegerField(default=-1)),
                ('price', models.FloatField(default=0)),
                ('unit', models.CharField(blank=True, default='', max_length=20)),
                ('availability', models.BooleanField(default=True)),
                ('sale', models.BooleanField(default=False)),
                ('sale_percentage', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('comments', models.CharField(blank=True, default='', max_length=100)),
                ('owner', models.CharField(blank=True, default='tig_orig', max_length=20)),
                ('stock', models.IntegerField(default=0)),
                ('unit_sold', models.IntegerField(default=0)),
            ],
        ),
    ]

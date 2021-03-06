# Generated by Django 3.1 on 2021-02-03 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0001_initial'),
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('goal', models.IntegerField()),
                ('ignore_negative', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.product')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel.advertiser')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.promotion')),
            ],
        ),
    ]

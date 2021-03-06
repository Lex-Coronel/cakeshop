# Generated by Django 3.2.4 on 2022-05-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='contact',
        ),
        migrations.AddField(
            model_name='shipping',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='contact',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='payment_method',
            field=models.CharField(choices=[('COD', 'COD'), ('GCASH', 'GCASH')], default='COD', max_length=200),
        ),
    ]

# Generated by Django 3.2.4 on 2022-05-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_shipping_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('message', models.CharField(max_length=10000, null=True)),
            ],
        ),
    ]

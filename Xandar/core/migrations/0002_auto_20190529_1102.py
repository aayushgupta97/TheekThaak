# Generated by Django 2.2.1 on 2019-05-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='attribute',
            field=models.CharField(choices=[('T-Shirts', (('Shirt Size', 'Shirt Size'), ('Shirt Color', 'Shirt Color'), ('Shirt Fabric', 'Shirt Fabric'))), ('Glasses', (('Glass Type', 'Glass Type'), ('Size', 'Glass Size'))), ('Shoes', (('Shoe Type', 'Shoe Type'), ('Shoe Size', 'Shoe Size'))), ('Other', ())], default='Default', max_length=50),
        ),
    ]

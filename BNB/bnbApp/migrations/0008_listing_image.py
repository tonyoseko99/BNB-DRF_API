# Generated by Django 4.1.6 on 2023-02-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnbApp', '0007_delete_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-24 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bnbApp', '0008_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='bnbApp.reservation'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_partners'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partners',
            options={'ordering': ['-id'], 'verbose_name': 'ALL PARTNERS', 'verbose_name_plural': 'ALL PARTNERS'},
        ),
        migrations.AddField(
            model_name='services',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y%m%d', verbose_name='Image in detail page (600X450)'),
        ),
    ]

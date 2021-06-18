# Generated by Django 3.0.6 on 2020-05-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorsBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titles')),
                ('role', models.CharField(max_length=200, verbose_name='Role')),
                ('des', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to='about/images/%y%m%d', verbose_name='Profile Image (255X255)')),
                ('fb_url', models.CharField(blank=True, max_length=250, null=True, verbose_name='FB URL')),
                ('tw_url', models.CharField(blank=True, max_length=250, null=True, verbose_name='TWITTER URL')),
                ('gp_url', models.CharField(blank=True, max_length=250, null=True, verbose_name='Google PLUS URL')),
                ('in_url', models.CharField(blank=True, max_length=250, null=True, verbose_name='INSTAGRAM URL')),
                ('pin_url', models.CharField(blank=True, max_length=250, null=True, verbose_name='PINTEREST URL')),
                ('is_verified', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Directors Board',
                'verbose_name_plural': 'Directors Board',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='aboutintro',
            name='image',
            field=models.ImageField(blank=True, upload_to='about/images/%y%m%d', verbose_name='Image (800X400)'),
        ),
    ]
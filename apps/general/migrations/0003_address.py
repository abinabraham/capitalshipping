# Generated by Django 3.0.6 on 2020-05-31 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_footerourservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=200, verbose_name='line1')),
                ('line2', models.CharField(max_length=200, verbose_name='line2')),
                ('line3', models.CharField(max_length=200, verbose_name='line3')),
                ('line4', models.CharField(max_length=200, verbose_name='line4')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('is_verified', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
                'ordering': ['-id'],
            },
        ),
    ]

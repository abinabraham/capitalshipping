# Generated by Django 3.0.6 on 2020-05-31 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterOurService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('url', models.CharField(blank=True, max_length=250, null=True, verbose_name="url eg: '/services/'")),
                ('is_verified', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Footer Our Service',
                'verbose_name_plural': 'Footer Our Service',
                'ordering': ['-id'],
            },
        ),
    ]

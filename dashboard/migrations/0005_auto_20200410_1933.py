# Generated by Django 3.0.3 on 2020-04-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200410_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fb_access',
            name='app_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='fb_access',
            name='app_secret_key',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fb_access',
            name='user_lg_token',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='fb_page',
            name='page_lg_tk',
            field=models.CharField(max_length=300),
        ),
    ]

# Generated by Django 4.2.6 on 2023-12-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_order_delete_oder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled', max_length=255)),
                ('image', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_content_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='pubdate',
            field=models.DateField(default=0),
        ),
    ]

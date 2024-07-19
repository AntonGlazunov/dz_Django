# Generated by Django 5.0.6 on 2024-07-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_contact_inn_alter_contact_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('massage', models.TextField(verbose_name='текст обращения')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
    ]
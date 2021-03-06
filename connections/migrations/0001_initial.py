# Generated by Django 2.0.5 on 2018-05-16 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(default='', max_length=50)),
                ('client_name', models.CharField(default='', max_length=50)),
                ('f4f_code', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[('movement', 'movement'), ('execution', 'execution'), ('financial', 'financial')], default='', max_length=50)),
                ('direction', models.CharField(choices=[('to partner', 'to partner'), ('from partner', 'from partner')], default='', max_length=50)),
                ('status', models.CharField(choices=[('awaiting approval', 'awaiting approval'), ('approved', 'approved'), ('rejected', 'rejected')], default='awaiting approval', max_length=50)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('client', models.ForeignKey(limit_choices_to={'is_client': True}, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(limit_choices_to={'is_admin': False, 'is_client': False}, on_delete=django.db.models.deletion.CASCADE, related_name='partner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('client', 'direction'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='connectiontable',
            unique_together={('user', 'message_type', 'direction', 'client')},
        ),
    ]

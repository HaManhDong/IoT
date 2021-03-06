# Generated by Django 2.0.3 on 2018-04-26 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='member name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('card_id', models.CharField(max_length=20, unique=True, verbose_name='card id')),
                ('course', models.CharField(max_length=10, null=True, verbose_name='course')),
                ('registered_day', models.DateField(auto_now_add=True)),
                ('avatar', models.ImageField(null=True, upload_to='avatar')),
                ('research_about', models.TextField(null=True, verbose_name='research')),
                ('is_train', models.BooleanField(default=False)),
                ('threshold', models.IntegerField(null=True)),
                ('is_in_lab', models.BooleanField(default=False)),
                ('coefficient', models.IntegerField(default=1, verbose_name='coefficients salary')),
                ('password', models.CharField(default='password', max_length=20, verbose_name='password')),
                ('recognize_label', models.IntegerField(default=1)),
                ('position', models.CharField(choices=[('ST', 'Student'), ('TE', 'Teacher')], default='ST', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('time_stamp', models.DateTimeField(primary_key=True, serialize=False, verbose_name='Time member in/out')),
                ('is_go_in', models.BooleanField()),
                ('result_auth', models.BooleanField()),
                ('image', models.ImageField(upload_to='logs/%Y/%m/%d')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_hour', models.IntegerField(verbose_name='Hour per day')),
                ('date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

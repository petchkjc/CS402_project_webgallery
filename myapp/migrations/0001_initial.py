# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-27 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField()),
                ('age', models.CharField(blank=True, max_length=2, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('job', models.CharField(blank=True, choices=[('\u0e19\u0e31\u0e01\u0e40\u0e23\u0e35\u0e22\u0e19/\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32', '\u0e19\u0e31\u0e01\u0e40\u0e23\u0e35\u0e22\u0e19/\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32'), ('\u0e04\u0e23\u0e39/\u0e2d\u0e32\u0e08\u0e32\u0e23\u0e22\u0e4c', '\u0e04\u0e23\u0e39/\u0e2d\u0e32\u0e08\u0e32\u0e23\u0e22\u0e4c'), ('\u0e41\u0e1e\u0e17\u0e22\u0e4c/\u0e1e\u0e22\u0e32\u0e1a\u0e32\u0e25', '\u0e41\u0e1e\u0e17\u0e22\u0e4c/\u0e1e\u0e22\u0e32\u0e1a\u0e32\u0e25'), ('\u0e17\u0e2b\u0e32\u0e23/\u0e15\u0e33\u0e23\u0e27\u0e08', '\u0e17\u0e2b\u0e32\u0e23/\u0e15\u0e33\u0e23\u0e27\u0e08'), ('\u0e23\u0e31\u0e1a\u0e08\u0e49\u0e32\u0e07', '\u0e23\u0e31\u0e1a\u0e08\u0e49\u0e32\u0e07'), ('\u0e1e\u0e19\u0e31\u0e01\u0e07\u0e32\u0e19\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17', '\u0e1e\u0e19\u0e31\u0e01\u0e07\u0e32\u0e19\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17'), ('\u0e02\u0e49\u0e32\u0e23\u0e32\u0e0a\u0e01\u0e32\u0e23', '\u0e02\u0e49\u0e32\u0e23\u0e32\u0e0a\u0e01\u0e32\u0e23'), ('\u0e40\u0e01\u0e29\u0e15\u0e23\u0e01\u0e23', '\u0e40\u0e01\u0e29\u0e15\u0e23\u0e01\u0e23'), ('\u0e19\u0e31\u0e01\u0e01\u0e0e\u0e2b\u0e21\u0e32\u0e22', '\u0e19\u0e31\u0e01\u0e01\u0e0e\u0e2b\u0e21\u0e32\u0e22'), ('\u0e19\u0e31\u0e01\u0e01\u0e32\u0e23\u0e40\u0e21\u0e37\u0e2d\u0e07', '\u0e19\u0e31\u0e01\u0e01\u0e32\u0e23\u0e40\u0e21\u0e37\u0e2d\u0e07'), ('\u0e19\u0e31\u0e01\u0e27\u0e34\u0e17\u0e22\u0e32\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c', '\u0e19\u0e31\u0e01\u0e27\u0e34\u0e17\u0e22\u0e32\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('\u0e28\u0e34\u0e25\u0e1b\u0e34\u0e19', '\u0e28\u0e34\u0e25\u0e1b\u0e34\u0e19'), ('\u0e40\u0e0a\u0e1f', '\u0e40\u0e0a\u0e1f'), ('\u0e2d\u0e37\u0e48\u0e19 \u0e46', '\u0e2d\u0e37\u0e48\u0e19 \u0e46')], max_length=100, null=True)),
                ('province', models.CharField(blank=True, choices=[('\u0e01\u0e23\u0e38\u0e07\u0e40\u0e17\u0e1e\u0e21\u0e2b\u0e32\u0e19\u0e04\u0e23', '\u0e01\u0e23\u0e38\u0e07\u0e40\u0e17\u0e1e\u0e21\u0e2b\u0e32\u0e19\u0e04\u0e23'), ('\u0e01\u0e23\u0e30\u0e1a\u0e35\u0e48', '\u0e01\u0e23\u0e30\u0e1a\u0e35\u0e48'), ('\u0e01\u0e32\u0e0d\u0e08\u0e19\u0e1a\u0e38\u0e23\u0e35', '\u0e01\u0e32\u0e0d\u0e08\u0e19\u0e1a\u0e38\u0e23\u0e35'), ('\u0e01\u0e32\u0e2c\u0e2a\u0e34\u0e19\u0e18\u0e38\u0e4c', '\u0e01\u0e32\u0e2c\u0e2a\u0e34\u0e19\u0e18\u0e38\u0e4c'), ('\u0e01\u0e33\u0e41\u0e1e\u0e07\u0e40\u0e1e\u0e0a\u0e23', '\u0e01\u0e33\u0e41\u0e1e\u0e07\u0e40\u0e1e\u0e0a\u0e23'), ('\u0e02\u0e2d\u0e19\u0e41\u0e01\u0e48\u0e19', '\u0e02\u0e2d\u0e19\u0e41\u0e01\u0e48\u0e19'), ('\u0e08\u0e31\u0e19\u0e17\u0e1a\u0e38\u0e23\u0e35', '\u0e08\u0e31\u0e19\u0e17\u0e1a\u0e38\u0e23\u0e35'), ('\u0e09\u0e30\u0e40\u0e0a\u0e34\u0e07\u0e40\u0e17\u0e23\u0e32', '\u0e09\u0e30\u0e40\u0e0a\u0e34\u0e07\u0e40\u0e17\u0e23\u0e32'), ('\u0e0a\u0e25\u0e1a\u0e38\u0e23\u0e35', '\u0e0a\u0e25\u0e1a\u0e38\u0e23\u0e35'), ('\u0e0a\u0e31\u0e22\u0e19\u0e32\u0e17', '\u0e0a\u0e31\u0e22\u0e19\u0e32\u0e17'), ('\u0e0a\u0e31\u0e22\u0e20\u0e39\u0e21\u0e34', '\u0e0a\u0e31\u0e22\u0e20\u0e39\u0e21\u0e34'), ('\u0e0a\u0e38\u0e21\u0e1e\u0e23', '\u0e0a\u0e38\u0e21\u0e1e\u0e23'), ('\u0e40\u0e0a\u0e35\u0e22\u0e07\u0e23\u0e32\u0e22', '\u0e40\u0e0a\u0e35\u0e22\u0e07\u0e23\u0e32\u0e22'), ('\u0e40\u0e0a\u0e35\u0e22\u0e07\u0e43\u0e2b\u0e21\u0e48', '\u0e40\u0e0a\u0e35\u0e22\u0e07\u0e43\u0e2b\u0e21\u0e48'), ('\u0e15\u0e23\u0e31\u0e07', '\u0e15\u0e23\u0e31\u0e07'), ('\u0e15\u0e23\u0e32\u0e14', '\u0e15\u0e23\u0e32\u0e14'), ('\u0e15\u0e32\u0e01', '\u0e15\u0e32\u0e01'), ('\u0e19\u0e04\u0e23\u0e19\u0e32\u0e22\u0e01', '\u0e19\u0e04\u0e23\u0e19\u0e32\u0e22\u0e01'), ('\u0e19\u0e04\u0e23\u0e1b\u0e10\u0e21', '\u0e19\u0e04\u0e23\u0e1b\u0e10\u0e21'), ('\u0e19\u0e04\u0e23\u0e1e\u0e19\u0e21', '\u0e19\u0e04\u0e23\u0e1e\u0e19\u0e21'), ('\u0e19\u0e04\u0e23\u0e23\u0e32\u0e0a\u0e2a\u0e35\u0e21\u0e32', '\u0e19\u0e04\u0e23\u0e23\u0e32\u0e0a\u0e2a\u0e35\u0e21\u0e32'), ('\u0e19\u0e04\u0e23\u0e28\u0e23\u0e35\u0e18\u0e23\u0e23\u0e21\u0e23\u0e32\u0e0a', '\u0e19\u0e04\u0e23\u0e28\u0e23\u0e35\u0e18\u0e23\u0e23\u0e21\u0e23\u0e32\u0e0a'), ('\u0e19\u0e04\u0e23\u0e2a\u0e27\u0e23\u0e23\u0e04\u0e4c', '\u0e19\u0e04\u0e23\u0e2a\u0e27\u0e23\u0e23\u0e04\u0e4c'), ('\u0e19\u0e19\u0e17\u0e1a\u0e38\u0e23\u0e35', '\u0e19\u0e19\u0e17\u0e1a\u0e38\u0e23\u0e35'), ('\u0e19\u0e23\u0e32\u0e18\u0e34\u0e27\u0e32\u0e2a', '\u0e19\u0e23\u0e32\u0e18\u0e34\u0e27\u0e32\u0e2a'), ('\u0e19\u0e48\u0e32\u0e19', '\u0e19\u0e48\u0e32\u0e19'), ('\u0e1a\u0e36\u0e07\u0e01\u0e32\u0e2c', '\u0e1a\u0e36\u0e07\u0e01\u0e32\u0e2c'), ('\u0e1a\u0e38\u0e23\u0e35\u0e23\u0e31\u0e21\u0e22\u0e4c', '\u0e1a\u0e38\u0e23\u0e35\u0e23\u0e31\u0e21\u0e22\u0e4c'), ('\u0e1b\u0e17\u0e38\u0e21\u0e18\u0e32\u0e19\u0e35', '\u0e1b\u0e17\u0e38\u0e21\u0e18\u0e32\u0e19\u0e35'), ('\u0e1b\u0e23\u0e30\u0e08\u0e27\u0e1a\u0e04\u0e35\u0e23\u0e35\u0e02\u0e31\u0e19\u0e18\u0e4c', '\u0e1b\u0e23\u0e30\u0e08\u0e27\u0e1a\u0e04\u0e35\u0e23\u0e35\u0e02\u0e31\u0e19\u0e18\u0e4c'), ('\u0e1b\u0e23\u0e32\u0e08\u0e35\u0e19\u0e1a\u0e38\u0e23\u0e35', '\u0e1b\u0e23\u0e32\u0e08\u0e35\u0e19\u0e1a\u0e38\u0e23\u0e35'), ('\u0e1b\u0e31\u0e15\u0e15\u0e32\u0e19\u0e35', '\u0e1b\u0e31\u0e15\u0e15\u0e32\u0e19\u0e35'), ('\u0e1e\u0e23\u0e30\u0e19\u0e04\u0e23\u0e28\u0e23\u0e35\u0e2d\u0e22\u0e38\u0e18\u0e22\u0e32', '\u0e1e\u0e23\u0e30\u0e19\u0e04\u0e23\u0e28\u0e23\u0e35\u0e2d\u0e22\u0e38\u0e18\u0e22\u0e32'), ('\u0e1e\u0e31\u0e07\u0e07\u0e32', '\u0e1e\u0e31\u0e07\u0e07\u0e32'), ('\u0e1e\u0e31\u0e17\u0e25\u0e38\u0e07', '\u0e1e\u0e31\u0e17\u0e25\u0e38\u0e07'), ('\u0e1e\u0e34\u0e08\u0e34\u0e15\u0e23', '\u0e1e\u0e34\u0e08\u0e34\u0e15\u0e23'), ('\u0e1e\u0e34\u0e29\u0e13\u0e38\u0e42\u0e25\u0e01', '\u0e1e\u0e34\u0e29\u0e13\u0e38\u0e42\u0e25\u0e01'), ('\u0e40\u0e1e\u0e0a\u0e23\u0e1a\u0e38\u0e23\u0e35', '\u0e40\u0e1e\u0e0a\u0e23\u0e1a\u0e38\u0e23\u0e35'), ('\u0e40\u0e1e\u0e0a\u0e23\u0e1a\u0e39\u0e23\u0e13\u0e4c', '\u0e40\u0e1e\u0e0a\u0e23\u0e1a\u0e39\u0e23\u0e13\u0e4c'), ('\u0e41\u0e1e\u0e23\u0e48', '\u0e41\u0e1e\u0e23\u0e48'), ('\u0e1e\u0e30\u0e40\u0e22\u0e32', '\u0e1e\u0e30\u0e40\u0e22\u0e32'), ('\u0e20\u0e39\u0e40\u0e01\u0e47\u0e15', '\u0e20\u0e39\u0e40\u0e01\u0e47\u0e15'), ('\u0e21\u0e2b\u0e32\u0e2a\u0e32\u0e23\u0e04\u0e32\u0e21', '\u0e21\u0e2b\u0e32\u0e2a\u0e32\u0e23\u0e04\u0e32\u0e21'), ('\u0e21\u0e38\u0e01\u0e14\u0e32\u0e2b\u0e32\u0e23', '\u0e21\u0e38\u0e01\u0e14\u0e32\u0e2b\u0e32\u0e23'), ('\u0e41\u0e21\u0e48\u0e2e\u0e48\u0e2d\u0e07\u0e2a\u0e2d\u0e19', '\u0e41\u0e21\u0e48\u0e2e\u0e48\u0e2d\u0e07\u0e2a\u0e2d\u0e19'), ('\u0e22\u0e30\u0e25\u0e32', '\u0e22\u0e30\u0e25\u0e32'), ('\u0e22\u0e42\u0e2a\u0e18\u0e23', '\u0e22\u0e42\u0e2a\u0e18\u0e23'), ('\u0e23\u0e49\u0e2d\u0e22\u0e40\u0e2d\u0e47\u0e14', '\u0e23\u0e49\u0e2d\u0e22\u0e40\u0e2d\u0e47\u0e14'), ('\u0e23\u0e30\u0e19\u0e2d\u0e07', '\u0e23\u0e30\u0e19\u0e2d\u0e07'), ('\u0e23\u0e30\u0e22\u0e2d\u0e07', '\u0e23\u0e30\u0e22\u0e2d\u0e07'), ('\u0e23\u0e32\u0e0a\u0e1a\u0e38\u0e23\u0e35', '\u0e23\u0e32\u0e0a\u0e1a\u0e38\u0e23\u0e35'), ('\u0e25\u0e1e\u0e1a\u0e38\u0e23\u0e35', '\u0e25\u0e1e\u0e1a\u0e38\u0e23\u0e35'), ('\u0e25\u0e33\u0e1b\u0e32\u0e07', '\u0e25\u0e33\u0e1b\u0e32\u0e07'), ('\u0e25\u0e33\u0e1e\u0e39\u0e19', '\u0e25\u0e33\u0e1e\u0e39\u0e19'), ('\u0e40\u0e25\u0e22', '\u0e40\u0e25\u0e22'), ('\u0e28\u0e23\u0e35\u0e2a\u0e30\u0e40\u0e01\u0e29', '\u0e28\u0e23\u0e35\u0e2a\u0e30\u0e40\u0e01\u0e29'), ('\u0e2a\u0e01\u0e25\u0e19\u0e04\u0e23', '\u0e2a\u0e01\u0e25\u0e19\u0e04\u0e23'), ('\u0e2a\u0e07\u0e02\u0e25\u0e32', '\u0e2a\u0e07\u0e02\u0e25\u0e32'), ('\u0e2a\u0e15\u0e39\u0e25', '\u0e2a\u0e15\u0e39\u0e25'), ('\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e1b\u0e23\u0e32\u0e01\u0e32\u0e23', '\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e1b\u0e23\u0e32\u0e01\u0e32\u0e23'), ('\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e2a\u0e07\u0e04\u0e23\u0e32\u0e21', '\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e2a\u0e07\u0e04\u0e23\u0e32\u0e21'), ('\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e2a\u0e32\u0e04\u0e23', '\u0e2a\u0e21\u0e38\u0e17\u0e23\u0e2a\u0e32\u0e04\u0e23'), ('\u0e2a\u0e23\u0e30\u0e41\u0e01\u0e49\u0e27', '\u0e2a\u0e23\u0e30\u0e41\u0e01\u0e49\u0e27'), ('\u0e2a\u0e23\u0e30\u0e1a\u0e38\u0e23\u0e35', '\u0e2a\u0e23\u0e30\u0e1a\u0e38\u0e23\u0e35'), ('\u0e2a\u0e34\u0e07\u0e2b\u0e4c\u0e1a\u0e38\u0e23\u0e35', '\u0e2a\u0e34\u0e07\u0e2b\u0e4c\u0e1a\u0e38\u0e23\u0e35'), ('\u0e2a\u0e38\u0e42\u0e02\u0e17\u0e31\u0e22', '\u0e2a\u0e38\u0e42\u0e02\u0e17\u0e31\u0e22'), ('\u0e2a\u0e38\u0e1e\u0e23\u0e23\u0e13\u0e1a\u0e38\u0e23\u0e35', '\u0e2a\u0e38\u0e1e\u0e23\u0e23\u0e13\u0e1a\u0e38\u0e23\u0e35'), ('\u0e2a\u0e38\u0e23\u0e32\u0e29\u0e0e\u0e23\u0e4c\u0e18\u0e32\u0e19\u0e35', '\u0e2a\u0e38\u0e23\u0e32\u0e29\u0e0e\u0e23\u0e4c\u0e18\u0e32\u0e19\u0e35'), ('\u0e2a\u0e38\u0e23\u0e34\u0e19\u0e17\u0e23\u0e4c', '\u0e2a\u0e38\u0e23\u0e34\u0e19\u0e17\u0e23\u0e4c'), ('\u0e2b\u0e19\u0e2d\u0e07\u0e04\u0e32\u0e22', '\u0e2b\u0e19\u0e2d\u0e07\u0e04\u0e32\u0e22'), ('\u0e2b\u0e19\u0e2d\u0e07\u0e1a\u0e31\u0e27\u0e25\u0e33\u0e20\u0e39', '\u0e2b\u0e19\u0e2d\u0e07\u0e1a\u0e31\u0e27\u0e25\u0e33\u0e20\u0e39'), ('\u0e2d\u0e48\u0e32\u0e07\u0e17\u0e2d\u0e07', '\u0e2d\u0e48\u0e32\u0e07\u0e17\u0e2d\u0e07'), ('\u0e2d\u0e38\u0e14\u0e23\u0e18\u0e32\u0e19\u0e35', '\u0e2d\u0e38\u0e14\u0e23\u0e18\u0e32\u0e19\u0e35'), ('\u0e2d\u0e38\u0e17\u0e31\u0e22\u0e18\u0e32\u0e19\u0e35', '\u0e2d\u0e38\u0e17\u0e31\u0e22\u0e18\u0e32\u0e19\u0e35'), ('\u0e2d\u0e38\u0e15\u0e23\u0e14\u0e34\u0e15\u0e16\u0e4c', '\u0e2d\u0e38\u0e15\u0e23\u0e14\u0e34\u0e15\u0e16\u0e4c'), ('\u0e2d\u0e38\u0e1a\u0e25\u0e23\u0e32\u0e0a\u0e18\u0e32\u0e19\u0e35', '\u0e2d\u0e38\u0e1a\u0e25\u0e23\u0e32\u0e0a\u0e18\u0e32\u0e19\u0e35'), ('\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e40\u0e08\u0e23\u0e34\u0e0d', '\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e40\u0e08\u0e23\u0e34\u0e0d')], max_length=20, null=True)),
                ('typeofphone', models.CharField(blank=True, choices=[('OSI', 'IOS'), ('Android', 'Android')], max_length=7, null=True)),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.Session')),
            ],
        ),
    ]

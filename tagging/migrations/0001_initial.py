# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name', db_index=True)),
                ('access', models.CharField(max_length=2, verbose_name='level', choices=[(b'0', b'user'), (b'1', b'staff'), (b'2', b'admin'), (b'3', b'pivot')])),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='object id', db_index=True)),
                ('content_type', models.ForeignKey(on_delete=models.CASCADE, verbose_name='content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(on_delete=models.CASCADE, related_name='items', verbose_name='tag', to='tagging.Tag')),
            ],
            options={
                'verbose_name': 'tagged item',
                'verbose_name_plural': 'tagged items',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('name', 'access')]),
        ),
        migrations.AlterUniqueTogether(
            name='taggeditem',
            unique_together=set([('tag', 'content_type', 'object_id')]),
        ),
    ]

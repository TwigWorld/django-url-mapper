# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlmapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmap',
            name='key',
            field=models.CharField(unique=True, max_length=64, verbose_name='Key', choices=[(b'tigtag_url', b'tigtag_url'), (b'junior_url', b'junior_url'), (b'terms-and-conditions', b'terms-and-conditions'), (b'awards', b'awards'), (b'how-to-use-ttj', b'how-to-use-ttj'), (b'how-to-use-tt', b'how-to-use-tt')]),
            preserve_default=True,
        ),
    ]

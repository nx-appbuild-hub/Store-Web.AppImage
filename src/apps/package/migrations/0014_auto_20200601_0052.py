# Generated by Django 2.2.10 on 2020-06-01 00:52

import chunked_upload.models
import chunked_upload.settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200601_0047'),
        ('package', '0013_auto_20200601_0047'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='packageupload',
        #     name='chunkedupload_ptr',
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='completed_on',
        #     field=models.DateTimeField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='created_on',
        #     field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='file',
        #     field=models.FileField(default=django.utils.timezone.now, max_length=255, upload_to=chunked_upload.settings.default_upload_to),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='filename',
        #     field=models.CharField(default=django.utils.timezone.now, max_length=255),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='id',
        #     field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='offset',
        #     field=models.BigIntegerField(default=0),
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='status',
        #     field=models.PositiveSmallIntegerField(choices=[(1, 'Uploading'), (2, 'Complete')], default=1),
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='upload_id',
        #     field=models.CharField(default=chunked_upload.models.generate_upload_id, editable=False, max_length=32, unique=True),
        # ),
        # migrations.AddField(
        #     model_name='packageupload',
        #     name='user',
        #     field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='package_upload', to='customer.Customer'),
        #     preserve_default=False,
        # ),
    ]

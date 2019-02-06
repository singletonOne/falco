# Generated by Django 2.1.5 on 2019-02-06 15:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0002_auditstatushistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditResults',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('wpt_results_json_url', models.CharField(max_length=1000)),
                ('wpt_metric_tti', models.IntegerField()),
                ('audit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='audits.Audit')),
            ],
            options={
                'ordering': ('-created_at',),
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='auditstatushistory',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ERROR', 'ERROR'), ('SUCCESS', 'SUCCESS')], max_length=10),
        ),
    ]

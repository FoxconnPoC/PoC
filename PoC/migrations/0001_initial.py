# Generated by Django 2.1.8 on 2019-05-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ct_view',
            fields=[
                ('productionline', models.CharField(max_length=20)),
                ('sysserialno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('workorderno', models.CharField(max_length=50)),
                ('assy', models.BigIntegerField()),
                ('test', models.BigIntegerField()),
                ('pack', models.BigIntegerField()),
                ('ship', models.BigIntegerField()),
                ('stage', models.CharField(max_length=20)),
                ('sla_time', models.IntegerField()),
                ('insla', models.IntegerField()),
                ('elapsed_time', models.BigIntegerField()),
                ('currentevent', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'poc_ct_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SfcPoc',
            fields=[
                ('workorderno', models.CharField(max_length=50)),
                ('productlevel', models.CharField(blank=True, max_length=30, null=True)),
                ('productionline', models.CharField(max_length=20)),
                ('routeid', models.CharField(max_length=10)),
                ('sysserialno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('platform', models.CharField(blank=True, db_column='platform', max_length=50, null=True)),
                ('basemod', models.CharField(blank=True, db_column='basemod', max_length=20, null=True)),
                ('ordertype', models.CharField(blank=True, db_column='ordertype', max_length=20, null=True)),
                ('scheduledate', models.DateTimeField(blank=True, null=True)),
                ('assyin_date', models.DateTimeField(blank=True, db_column='assyin_date', null=True)),
                ('assyout_date', models.DateTimeField(blank=True, db_column='assyout_date', null=True)),
                ('testin_date', models.DateTimeField(blank=True, db_column='testin_date', null=True)),
                ('testout_date', models.DateTimeField(blank=True, db_column='testout_date', null=True)),
                ('packin_date', models.DateTimeField(blank=True, db_column='packin_date', null=True)),
                ('packout_date', models.DateTimeField(blank=True, db_column='packout_date', null=True)),
                ('shipin_date', models.DateTimeField(blank=True, db_column='shipin_date', null=True)),
                ('shipout_date', models.DateTimeField(blank=True, db_column='shipout_date', null=True)),
                ('currentevent', models.CharField(blank=True, max_length=30, null=True)),
                ('nextevent', models.CharField(blank=True, max_length=30, null=True)),
                ('etltime', models.DateTimeField(blank=True, db_column='etltime', null=True)),
            ],
            options={
                'db_table': 'sfc_poc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CT_Stages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stageCode', models.IntegerField()),
                ('stageName', models.CharField(max_length=15)),
                ('slatime', models.IntegerField()),
            ],
        ),
    ]
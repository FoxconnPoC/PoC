
from django.db import models

class CT_Stages(models.Model):
    stageCode = models.IntegerField()
    stageName = models.CharField(max_length=15)
    slatime = models.IntegerField()

    def __str__(self):
        return self.stageName


class SfcPoc(models.Model):
    workorderno = models.CharField(max_length=50)
    productlevel = models.CharField(max_length=30, blank=True, null=True)
    productionline = models.CharField(max_length=20)
    routeid = models.CharField(max_length=10)
    sysserialno = models.CharField(primary_key=True, max_length=20)
    platform = models.CharField(db_column='platform', max_length=50, blank=True, null=True)  # Field name made lowercase.
    basemod = models.CharField(db_column='basemod', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ordertype = models.CharField(db_column='ordertype', max_length=20, blank=True, null=True)  # Field name made lowercase.
    scheduledate = models.DateTimeField(blank=True, null=True)
    assyin_date = models.DateTimeField(db_column='assyin_date', blank=True, null=True)  # Field name made lowercase.
    assyout_date = models.DateTimeField(db_column='assyout_date', blank=True, null=True)  # Field name made lowercase.
    testin_date = models.DateTimeField(db_column='testin_date', blank=True, null=True)  # Field name made lowercase.
    testout_date = models.DateTimeField(db_column='testout_date', blank=True, null=True)  # Field name made lowercase.
    packin_date = models.DateTimeField(db_column='packin_date', blank=True, null=True)  # Field name made lowercase.
    packout_date = models.DateTimeField(db_column='packout_date', blank=True, null=True)  # Field name made lowercase.
    shipin_date = models.DateTimeField(db_column='shipin_date', blank=True, null=True)  # Field name made lowercase.
    shipout_date = models.DateTimeField(db_column='shipout_date', blank=True, null=True)  # Field name made lowercase.
    currentevent = models.CharField(max_length=30, blank=True, null=True)
    nextevent = models.CharField(max_length=30, blank=True, null=True)
    etltime = models.DateTimeField(db_column='etltime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sfc_poc'

class ct_view(models.Model):
    productionline = models.CharField(max_length=20)
    sysserialno = models.CharField(primary_key=True, max_length=20)
    workorderno = models.CharField(max_length=50)
    assy = models.BigIntegerField()
    test = models.BigIntegerField()
    pack = models.BigIntegerField()
    ship = models.BigIntegerField()
    stage = models.CharField(max_length=20)
    sla_time = models.IntegerField()
    insla = models.IntegerField()
    elapsed_time = models.BigIntegerField()
    currentevent = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'poc_ct_view'


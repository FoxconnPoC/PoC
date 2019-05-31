from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
import pdb
from django.db import connection
from .models import CT_Stages, ct_view, SfcPoc

def index(request):
    # cursor = connection.cursor()
    # # Write the SQL code
    # sql_string = 'SELECT * FROM poc_ct_view'
    # # Execute the SQL
    # cursor.execute(sql_string)
    # result = cursor.fetchall()

    line_data_dict = {}

    stage_list = CT_Stages.objects.order_by('stageCode')
    # group by
    # line_data_count_raw = ct_view.objects\
    #     .values('productionline', 'stage', 'inSLA')\
    #     .annotate(cnt=Count('sysserialno'))\
    #     .order_by('productionline','stage','inSLA')

    line_data_raw_columns = ['productionline', 'sysserialno', 'workorderno', 'stage','insla','elapsed_time','currentevent']
    line_data_raw = ct_view.objects.values(*line_data_raw_columns).order_by('-elapsed_time')

    workorder_data = {}
    for line_data in line_data_raw:
        if line_data['workorderno'] not in workorder_data:
            workorder_data[line_data['workorderno']] = [0,0]
        if workorder_data[line_data['workorderno']][1] < int(line_data['elapsed_time']):
            workorder_data[line_data['workorderno']][1] = int(line_data['elapsed_time'])
        workorder_data[line_data['workorderno']][0] += 1

    line_data_grouped = line_data_raw\
        .values('productionline', 'stage', 'insla') \
        .annotate(cnt=Count('sysserialno')) \
        .order_by('productionline', 'stage', 'insla')

    print(workorder_data)

    for line_data in line_data_grouped:
        if not line_data['productionline'] in line_data_dict:
            line_data_dict[line_data['productionline']] = { i.stageName:{'insla':0,'outsla':0} for i in stage_list}
        try:
            line_data_dict[line_data['productionline']][line_data['stage']]['insla' if int(line_data['insla'])==1 else 'outsla'] = \
                line_data['cnt']
        except KeyError as e:
            pass
    print(line_data_grouped.query)
    context = {
        'stage_list': stage_list,
        'line_data_dict': line_data_dict,
        'line_data_raw': line_data_raw,
        'line_data_raw_columns': line_data_raw_columns,
        'workorder_data': workorder_data,
    }

    return render(request, 'PoC/index.html', context)



def serial_detail(request, sysserialno):
    serial_qs = SfcPoc.objects.filter(sysserialno=sysserialno)

    serial_qs_fileds = [f.name for f in SfcPoc._meta.get_fields()]
    testing = {}

    for k, v in serial_qs.values()[0].items():
        testing[k] = v
    context ={
        'serial_qs': testing,
        'serial_qs_fileds':serial_qs_fileds,
    }

    return render(request, 'PoC/serialno_detail.html', context)

def line_detail(request, line, stage, inSLA):
    line_data_raw_columns = ['productionline', 'sysserialno', 'workorderno', 'stage', 'insla', 'elapsed_time',
                             'currentevent']
    line_data_raw = ct_view.objects.values(*line_data_raw_columns).filter(productionline=line,
                                                                          insla=int(inSLA),stage=stage).order_by('-elapsed_time')

    context = {
        'line_data_raw': line_data_raw,
        'line_data_raw_columns': line_data_raw_columns,
    }
    print(request,line,stage,inSLA)
    print(line_data_raw.query)
    return render(request, 'PoC/line_detail.html', context)
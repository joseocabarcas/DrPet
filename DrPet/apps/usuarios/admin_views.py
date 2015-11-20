from .models import Auditoria,Procedimientos
from django.db.models import Count
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse,HttpResponse


def report(request):
	return render_to_response("reporte.html",{},RequestContext(request, {}),)

def reportesajax(request):
	#queryset=Auditoria.objects.all().values('operacion','fechahora').annotate(total=Count('operacion')).order_by('operacion')
	#serialized_q = json.dumps(list(queryset), cls=DjangoJSONEncoder)
	procedimientos= Procedimientos()
	try:
		auditorias=procedimientos.Auditorias_total()
		print auditorias
	except Exception, e:
		print e
		auditorias={}
	return JsonResponse({'auditorias':auditorias})

report = staff_member_required(report)
reportesajax = staff_member_required(reportesajax)


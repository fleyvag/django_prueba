import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

from  core.erp.models import  Type


#############LISTAR########
#select * from tabla
#query=Type.objects.all()
#print(query)


#############CREAR#########
#t=Type()
#t.name='Analista'
#t.save()

#############edicion########
#t=Type.objects.get(id=4)
#t.name='profesor'
#t.save()


############eELIMINAR#########
#t= Type.objects.get(id=4)
#t.delete()

##############filtros#############
# se le agrega la i cuando quiere que no se diferencie de min y mayus
#obj=Type.objects.filter(name__icontains='ana')
#obj=Type.objects.filter(name__istartswith='a')
#obj = Type.objects.filter(name__in=['limpieza','programador']).count()
#obj=Type.objects.filter(name__contains='ana').query
#obj=Type.objects.filter(name__contains='ana').exclude(id=5)
#print(obj)
#for i in Type.objects.all():
#    print(i)

#
for i in Type.objects.filter(name__iendswith='a')[:2]:
    print(i)

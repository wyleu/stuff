from django.contrib import admin

# Register your models here.
from .models import Node
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

def export_selected_objects(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

admin.site.add_action(export_selected_objects, 'export_selected')

class NodeAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'id',
                    'order',
                    'x',
                    'y',
                    'z',
                    'r',
                    'g',
                    'b'
                    )
    pass

admin.site.register(Node, NodeAdmin)

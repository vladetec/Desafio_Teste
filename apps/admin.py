from django.contrib import admin
from .models import Serv, OrdemServ
# Register your models here.
@admin.register(Serv)
class ServAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_valor')
    search_fields = ('descricao',)
    list_filter = ('valor',)


@admin.register(OrdemServ)
class OrdemServAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'quantidade', 'valor_total', 'data',
     'horaInicio', 'horaFim', 'nomeFuncionario', 'detalhe')
    search_fields = ('servico',)
    list_filter = ('data',)

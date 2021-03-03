
from django.db import models
from django.utils import timezone
from users.models import User
from django.utils.formats import number_format


class Serv(models.Model):
  descricao = models.CharField(max_length=255, unique=True)
  valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)

  def get_valor(self):
        return u"R$ %s" % number_format(self.valor, 2)

  def __str__(self):
        return self.descricao

  class Meta:
    ordering = ('descricao',)
    verbose_name = 'Serviço'
    verbose_name_plural = 'Serviços'

# horas = ([(str(x), str(x)) for x in range(1, 25)])

class OrdemServ(models.Model):
  servico = models.ForeignKey(Serv, on_delete=models.CASCADE)
  quantidade = models.IntegerField(default=1)
  data = models.DateField(default=timezone.now)
  horaInicio = models.TimeField(blank=True, null=True)
  horaFim = models.TimeField(blank=True, null=True)
  nomeFuncionario = models.ForeignKey(User, on_delete=models.CASCADE)
  detalhe = models.TextField()

  def get_data(self):
        return self.data.strftime('%d/%m/%y')

  def valor_total(self):
    return self.servico.valor * self.quantidade

  def __str__(self):
        return "{}-{}".format(self.servico, self.data)

  class Meta:
      ordering = ('data',)
      verbose_name = 'Ordem_Serviço'
      verbose_name_plural = 'Ordens_Servico'

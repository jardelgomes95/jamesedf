from django.db import models

# Create your models here.
class aluno(models.Model):

    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outros"),
        ("NI", "Não Informado")

    )
    #parte 1
    nome = models.CharField(max_length=55, blank=False, null=False, verbose_name="Nome do Aluno")
    cpf = models.CharField(max_length=15, blank=True, null=True, unique=True, verbose_name="CPF")
    profissao = models.CharField(max_length=36, blank=False, null=False, verbose_name="Profissão")
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=3, blank=False,  null=False, verbose_name="Sexo")
    idade = models.FloatField(null=False, blank=False, verbose_name="Idade")
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False, verbose_name="Altura")
    ativo = models.BooleanField(null=False, blank=False, verbose_name="Já Fez Atividade Física")
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="Peso (Kg)")
    imc = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, verbose_name="IMC")
    cintura = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False, verbose_name="Medida Cintura (cm)")
    quadril = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False, verbose_name="Medida Quadril (cm)")


    #parte 2
    torax = models.FloatField(null=True, blank=False, verbose_name="Tórax")
    ombro = models.FloatField(null=True, blank=False, verbose_name="Ombro")
    abdomen = models.FloatField(null=True, blank=False, verbose_name="Abdomên")
    biceps = models.FloatField(null=True, blank=False, verbose_name="Biceps Relaxado")
    bicesps = models.FloatField(null=True, blank=False, verbose_name="Biceps Contraído")
    coxa = models.FloatField(null=True, blank=False, verbose_name="Coxa")
    panturrilha = models.FloatField(null=True, blank=False, verbose_name="Panturrilha")
    rcq = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, verbose_name="RCQ")

    #parte 3
    d1 = models.FloatField(null=True, blank=False, verbose_name="Subescapular")
    d2 = models.FloatField(null=True, blank=False, verbose_name="Tricipital")
    d3 = models.FloatField(null=True, blank=False, verbose_name="Peitoral")
    d4 = models.FloatField(null=True, blank=False, verbose_name="Axilar Média")
    d5 = models.FloatField(null=True, blank=False, verbose_name="Supra-Ilíaca")
    d6 = models.FloatField(null=True, blank=False, verbose_name="Cutânea Abdominal")
    d7 = models.FloatField(null=True, blank=False, verbose_name="Femural Médio")
    d_soma = models.FloatField(null=True, blank=True, verbose_name="Soma Dobras", editable=False)
    dc1 = models.FloatField(null=True, blank=True, verbose_name="Dobras Cutâneas 1", editable=False)
    dc2 = models.FloatField(null=True, blank=True, verbose_name="Dobras Cutâneas 2", editable=False)
    dc3 = models.FloatField(null=True, blank=True, verbose_name="Dobras Cutâneas 3", editable=False)
    dctotal = models.FloatField(null=True, blank=True, verbose_name="Densidade Corporal", editable=False)
    gordura = models.FloatField(null=True, blank=True, verbose_name="gordura em %")

    def __str__(self):
        return f' {self.nome}'

    def save(self, *args, **kwargs):
        self.rcq = self.cintura / self.quadril #calculo relação cintura quadril
        self.imc = self.peso / (self.altura * self.altura) #calculo de imc
        self.d_soma = self.d1 + self.d2 + self.d3 + self.d4 + self.d5 + self.d6 + self.d7 #soma das dobras cutâneas

        if self.sexo == 'F':
            self.dc1 = 1.0970
            self.dc2 = (0.00046971 * self.d_soma) + (0.00000056 * self.d_soma ** 2)
            self.dc3 = 0.00012828 * self.idade
        else:
            self.dc1 = 1.11200000
            self.dc2 = (0.00043499 * self.d_soma) + (0.00000055 * self.d_soma ** 2)
            self.dc3 = 0.0002882 * self.idade

        self.dctotal = self.dc1 - self.dc2 - self.dc3  #densidade corporal
        self.gordura = round(((4.95 / self.dctotal) - 4.50) * 100, 2)  #% de gordura corporal
        return super(aluno, self).save(*args, **kwargs)


####################################################################### - ###################################################


class ficha_de_saude(models.Model):
    VERDADEIRO_CHOICES = (
        ("S", "Sim"),
        ("N", "Não"),
        ("NI", "Não Informado")
    )
    nome = models.ForeignKey('aluno', on_delete=models.DO_NOTHING, default=1, verbose_name="Aluno")
    diabetes = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Diabetes")
    hipertensao = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Hipertensão")
    artrite = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Artrite")
    artrose = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Artrose")
    reumatismo = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Reumatismo")
    doencas_cardiacas = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Doenças Cardiacas")
    avc = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Já Sofreu AVC")
    fuma = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Tabagismo")
    BEBIDA_CHOICES = (
        ("S", "Sempre que Posso"),
        ("O", "Ocasionalmente"),
        ("R", "Raramente"),
        ("N", "Não Bebo")
    )
    bebe = models.CharField(max_length=1, choices=BEBIDA_CHOICES, blank=False, null=True, verbose_name="Bebe")
    insulina = models.BooleanField(null=False, blank=False, verbose_name="Insulina")
    antidepressivos = models.BooleanField(null=False, blank=False, verbose_name="Antidepressivos")
    antihistaminicos = models.BooleanField(null=False, blank=False, verbose_name="Anti-Histaminicos (Alergia)")
    betabloqueadores = models.BooleanField(null=False, blank=False, verbose_name="Betabloqueadores (Hipertensão)")
    analgesicos = models.BooleanField(null=False, blank=False, verbose_name="Analgésicos")
    ansiolitico = models.BooleanField(null=False, blank=False, verbose_name="Ansiolítico (Ansiedade)")
    suplementos_vit = models.BooleanField(null=False, blank=False, verbose_name="Suplementos Vitamínicos")
    observacoes = models.TextField(max_length=255, blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return f'{self.nome}'

############################################################### --- ###################################################################

class treinoA(models.Model):
    nome = models.ForeignKey('aluno', on_delete=models.DO_NOTHING, default=None, verbose_name="Aluno")
    aexc_1 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A1')
    rep1 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_2 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A2')
    rep2 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_3 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A3')
    rep3 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_4 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A4')
    rep4 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_5 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A5')
    rep5 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_6 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A6')
    rep6 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_7 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A7')
    rep7 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_8 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A8')
    rep8 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_9 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A9')
    rep9 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_10 = models.CharField(max_length=32, blank=True, null=False, verbose_name='A10')
    rep10 = models.CharField(max_length=6, blank=True, null=False, verbose_name='RP')
    aexc_11 = models.CharField(max_length=32, blank=True, null=False, verbose_name='A11')
    rep11 = models.CharField(max_length=6, blank=True, null=False, verbose_name='RP')
    aexc_12 = models.CharField(max_length=32, blank=True, null=False, verbose_name='A12')
    rep12 = models.CharField(max_length=6, blank=True, null=False, verbose_name='RP')

    def __str__(self):
        return f'{self.nome}'
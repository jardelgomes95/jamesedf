# Generated by Django 3.1.7 on 2021-09-06 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55, verbose_name='Nome do Aluno')),
                ('cpf', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='CPF')),
                ('profissao', models.CharField(max_length=36, verbose_name='Profissão')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros'), ('NI', 'Não Informado')], max_length=3, verbose_name='Sexo')),
                ('idade', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Idade')),
                ('altura', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Altura')),
                ('ativo', models.BooleanField(verbose_name='Já Fez Atividade Física')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Peso (Kg)')),
                ('imc', models.DecimalField(decimal_places=3, editable=False, max_digits=5, verbose_name='IMC')),
                ('cintura', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Medida Cintura (cm)')),
                ('quadril', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Medida Quadril (cm)')),
                ('rcq', models.DecimalField(decimal_places=2, editable=False, max_digits=3, verbose_name='Medida Quadril (cm)')),
            ],
        ),
    ]

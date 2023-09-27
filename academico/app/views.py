from django.shortcuts import render
from .models import *

def ocupacao(request):
    ocupacao = {
        'ocupacao': ManterOcupacao.objects.all()
    }
    return render(request, 'ocupacao/ocupacao.html', ocupacao)

def cidade(request):
    cidade = {
        'cidade': ManterCidade.objects.all()
    }
    return render(request, 'cidade/cidade.html', cidade)

def avaliacoes(request):
    avaliacoes = {
        'avaliacoes': TiposAvaliacoes.objects.all()
    }
    return render(request, 'avaliacao/avaliacao.html', avaliacoes)
# Create your views here.
def pessoas(request):
    pessoas = {
        'pessoas': ManterPessoas.objects.all()
    }
    return render(request, 'pessoas/pessoas.html', pessoas)

def ensino(request):
    ensino = {
        'ensino': ManterEnsino.objects.all()
    }
    return render(request, 'ensino/ensino.html', ensino)

def areas(request):
    areas = {
        'areas': ManterAreas.objects.all()
    }
    return render(request, 'areas/areas.html', areas)

def cursos(request):
    cursos = {
        'cursos': ManterCursos.objects.all()
    }
    return render(request, 'cursos/cursos.html', cursos)

def semestres(request):
    semestres = {
        'semestres': manterSemestres.objects.all()
    }
    return render(request, 'semestres/semestres.html', semestres)

def diciplina(request):
    diciplina = {
        'diciplina': ManterDiciplina.objects.all()
    }
    return render(request, 'diciplina/diciplina.html', diciplina)

def matricula(request):
    matricula = {
        'matricula': ManterMatriculas.objects.all()
    }
    return render(request, 'matricula/matricula.html', matricula)

def avaliacoes(request):
    avaliacoes = {
        'avaliacoes': Avaliacoes.objects.all()
    }
    return render(request, 'avaliacoes/avaliacoes.html', avaliacoes)

def frequencia(request):
    frequencia = {
        'frequencia': ManterFrequencia.objects.all()
    }
    return render(request, 'frequencia/frequencia.html', frequencia)

def turma(request):
    turma = {
        'turma': ManterTurmas.objects.all()
    }
    return render(request, 'turma/turma.html', turma)

def advertencia(request):
    advertencia = {
        'advertencia': Advertencias.objects.all()
    }
    return render(request, 'advertencia/advertencia.html', advertencia)

def diciplinacurso(request):
    diciplinacurso = {
        'diciplinacurso': ManterDisciplinaCurso.objects.all()
    }
    return render(request, 'diciplinacurso/diciplinacurso.html', diciplinacurso)


import sys
sys.path.append('../')

from cadastros.models import Aluno, Frequencia, Disciplinas, Notas
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def errorXFF(request):
    return render(request,'leagueofclass/error.html')


def failUserXFF(request):

    return render(request,'leagueofclass/failAutenticate.html')



def logoutUser(request):
    if request.user != None:
        logout(request)
    return redirect('/index')

def chosePerfil(request):
    return render(request,'leagueofclass/telaescolha.html')


def acessoProfessor(request):

    return render(request,'leagueofclass/painel_professor.html')

def acessoAluno(request):
    data = {}
    #ideia... fazer um filter que compare request.user com o usuário o login
    data['exibeInicio'] = True
    data['exibeNotas'] = False
    data['exibeDisciplinas'] = False
    data['exibeFrequencia'] = False
    data['msg'] = 'Suas informações:'
    data['alunos'] = Aluno.objects.filter(login=request.user)
    data['usuario'] = request.user
    return render(request,'leagueofclass/painel_aluno.html', data)

def notasAluno(request):
    data = {}
    data['exibeInicio'] = False
    data['exibeNotas'] = True
    data['exibeDisciplinas'] = False
    data['exibeFrequencia'] = False
    data['msg'] = 'Escolha uma disciplina para visualizar suas notas:'
    data ['qsDisciplinas'] = Disciplinas.objects.filter(aluno__login__exact=request.user)

    if request.method == 'POST':
        disciplinaEsc = request.POST.get('notasDisc', 'null')
        data['exibeNotasDisciplina'] = True
        data['msg2'] = disciplinaEsc
        data['qsNotas'] = Notas.objects.filter(aluno__login__exact=request.user).filter(disciplina__nomeDisciplina__exact=disciplinaEsc)
    return render(request,'leagueofclass/painel_aluno.html', data)


    return render(request,'leagueofclass/painel_aluno.html', data)

def disciplinasAluno(request):
    data = {}
    data['exibeInicio'] = False
    data['exibeNotas'] = False
    data['exibeDisciplinas'] = True
    data['exibeFrequencia'] = False
    data['disciplinas'] = Disciplinas.objects.filter(aluno__login__exact=request.user)
    data['msg'] = 'Disciplinas Matriculadas:'
    return render(request,'leagueofclass/painel_aluno.html', data)

def frequenciaAluno(request):
    data = {}
    data['exibeInicio'] = False
    data['exibeNotas'] = False
    data['exibeDisciplinas'] = False
    data['exibeFrequencia'] = True
    data ['qsDisciplinas'] = Disciplinas.objects.filter(aluno__login__exact=request.user)
    data ['msg'] = 'Escolha uma discipina para ver a frequência:'

    if request.method == 'POST':
        disciplinaEsc = request.POST.get('freqDisc', 'null')
        data['exibeFreqDisciplina'] = True
        data['msg2'] = disciplinaEsc
        data['qsFreqDisciplinas'] = Frequencia.objects.filter(aluno__login__exact=request.user).filter(disciplina__nomeDisciplina__exact=disciplinaEsc)
    return render(request,'leagueofclass/painel_aluno.html', data)

def atividadesAluno(request):
    return render(request,'leagueofclass/painel_aluno.html')

def clickMe(request):
    return render(request,'click.html')

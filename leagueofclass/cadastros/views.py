from django.shortcuts import render
from .models import Aluno,Professor,Perguntasx
from .form import ProfessorForm,AlunoForm,AtividadeForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.shortcuts import redirect
from .form import UsuarioForm
from django.contrib import messages

# Create your views here.

'''
 __VAR__
'''
user_aut=''

def cadastroProfessor(request):
	#url cadastro/ retorna o template de cadastros Professor!
	#Ñ implementada ainda


	if request.method=="POST":
		form = ProfessorForm(request.POST)

		if form.is_valid():

				try:

					verificaExistenciaPass = User.objects.get(password=form.cleaned_data['password'])
					verificaExistencia = User.objects.get(email=form.cleaned_data['email'])

					if verificaExistenciaPass or verificaExistencia:
						return render(request,'/home', {'msg': 'Ja existe um usuario com o mesmo email!'})


				except User.DoesNotExist:
					nome_professor = form.cleaned_data['nome']
					email_professor = form.cleaned_data['email']
					password_professor = form.cleaned_data['password']
					new_professor = User.objects.create_user(username=nome_professor, email=email_professor,
															 password=password_professor)

					new_professor.save()
					form.save()
					return redirect("/home")




		else:
			messages.warning(request, 'Preencha todos os campos corretamente!')

	else:
		form = ProfessorForm()
	return render(request,'leagueofclass/cadastroprofessor.html' , {'form':form})

dados_aluno_necessario={}
def cadastroAluno(request):
	if request.method=="POST":
		form = AlunoForm(request.POST)
		'''
		dados_aluno_necessario['nome'] = request.POST.get('nome')
		dados_aluno_necessario['sexo'] = request.POST.get('sexo')
		dados_aluno_necessario['dataNascimento'] = request.POST.get('dataNascimento')
		dados_aluno_necessario['email'] = request.POST.get('email')
		dados_aluno_necessario['login'] = request.POST.get('login')
		dados_aluno_necessario['password'] = request.POST.get('senha')
		dados_aluno_necessario['nomeInstituicao'] = request.POST.get('nomeInstituicao')
		'''

		if form.is_valid():
			try:


				verificaExistencia = User.objects.get(email=form.cleaned_data['email'])
				verificaExistenciaPass = User.objects.get(email=form.cleaned_data['email']).password
				if verificaExistenciaPass or verificaExistencia:
					return render(request, '/home', {'msg': 'Ja existe um usuario com o mesmo email!'})


			except User.DoesNotExist:
				nome_aluno = form.cleaned_data['nome']
				email_aluno = form.cleaned_data['email']
				password_aluno = form.cleaned_data['password']
				new_aluno = User.objects.create_user(username=nome_aluno, email=email_aluno,
														 password=password_aluno)

				new_aluno.save()
				form.save()
				return redirect("/home")
		else:

			messages.warning(request, 'Preencha todos os campos corretamente!')
	else:
		form = AlunoForm()


	return render(request,'leagueofclass/cadastroaluno.html', {'form':form})


def createAuthentic(request):
	# Responsavel por criar a autenticaçao do usuario!



	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			object_user = User.objects.get(email=form.cleaned_data['email'])
			user_aut = authenticate(username=object_user.username, password=form.cleaned_data['senha'])
			try:
				# Pegar os dados do formulario da pagina inicial!

				# Procura por um usuario da que contem o email (x)
				# é necessario que seja um "uSER" metodo padrao de busca
				# user.object.get('meuemail@hotmail.com1').getpassword().getusername();
				professor_matricula = Professor.objects.get(email=form.cleaned_data['email']).matricula


				if user_aut is not None and professor_matricula!=None:
					login(request, user_aut)
					return redirect('/dashboardProfessor')

				else:
					messages.warning(request, 'Email ou Senha errados!')
					return redirect('/failUser')
			except Professor.DoesNotExist:
				if user_aut is not None:
					login(request,user_aut)
					return redirect('/dashboardAluno')
				else:
					messages.warning(request, 'Email ou Senha errados!')
					return redirect('/failUser')

	else:
		form = UsuarioForm()

	return render(request, 'index.html', {'form': form})

def cadastroAtividade(request):
    if request.user.is_authenticated:
        if request.method=="POST":

            form = AtividadeForm(request.POST)
            if form.is_valid():

                titulo = form.cleaned_data['titulo']
                pergunta = form.cleaned_data['pergunta']
                alternativa_a = form.cleaned_data['alternativa_a']
                alternativa_b = form.cleaned_data['alternativa_b']
                alternativa_c = form.cleaned_data['alternativa_c']
                alternativa_d = form.cleaned_data['alternativa_d']
                opcaoCorreta = form.cleaned_data['alternativa_correta']
                # -------------------------------------------------------- Perguntas e titulo

                professor=request.user
                if professor!= None:
                    xd = ''

                    #lista =["'",request.user.email,"'"]
                    #for i in lista:
                    #    xd += i

                    # PQ ? isso exemplo 'osvaldo.airon@dce.ufpb.br' <- precisa estar em apas simples!
                    # nao precisou no final das contas;

                    param=Professor.objects.get(email=request.user.email)
                    if  param.matricula != None:

                        perguntas = Perguntasx(ask=pergunta, alternativa_a=alternativa_a, alternativa_b=alternativa_b,
                                           alternativa_c=alternativa_c, alternativa_d=alternativa_d,
                                           alternativaCorreta=opcaoCorreta,titulo=titulo,matricula_professor=param.matricula)
                        Perguntasx.save(perguntas)
                        return redirect("/dashboardProfessor")
                    else:
                        return redirect("/error")

        else:
            form = AtividadeForm()


    return render(request, 'leagueofclass/cadastroAtividade.html', {'form': form})


def cadastroDisciplinaAluno(request):
    # form
	return render(request,"leagueofclass/cadastrarDisciplina.html")

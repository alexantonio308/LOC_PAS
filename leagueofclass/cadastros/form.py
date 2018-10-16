from django import forms
from .models import Professor
from .models import Aluno
from .models import Usuarios
from .models import Disciplinas
from .models import Perguntasx

class DisciplinaAlunoForm(forms.ModelForm):
    class Meta:
        model = Disciplinas
        fields = '__all__'


class AtividadeForm(forms.Form):
	opcao = (('A', 'Alternativa A'), ('B', 'Alternativa B'), ('C', 'Alternativa C'), ('D', 'Alternativa D'))
	titulo = forms.CharField(max_length=200)
	pergunta = forms.CharField(max_length=100)
	alternativa_a = forms.CharField(max_length=200)
	alternativa_b = forms.CharField(max_length=200)
	alternativa_c = forms.CharField(max_length=200)
	alternativa_d = forms.CharField(max_length=200)
	alternativa_correta = forms.ChoiceField(widget=forms.RadioSelect, choices=opcao)
	"""
		Professor, insere atividade, uma atividade tem uma matricula do professor.
		pra dps puxar essa atv;

	"""



	#class Meta:
	#	model = Perguntasx
	#	fields = ['ask','alternativa_a','alternativa_b','alternativa_c', 'alternativa_d','alternativaCorreta','titulo']





class ProfessorForm(forms.ModelForm):
	'''
	Responsavel por criar o modelo de formulario a partir do modelo que esta sendo criado no db;
	'''
	class Meta:
		model = Professor
		fields = ['nome', 'sexo','dataNascimento','email','login','password','nomeInstituicao', 'matricula']



class AlunoForm(forms.ModelForm):
	class Meta:
		model = Aluno
		#NÃO É PRECISO RECUPERAR TODOS OS FIELDS NESSE FORM O CADASTRO DE ALUNO, É MAIS SIMPLES QUE O DE PROFESSOR
		# É NECESSARIO O NOME DA INSTITUIÇÃO TAMBEM!
		#
		# form mais simples é isso #PAZ
		fields = [

		'nome', 'sexo','dataNascimento','email','login','password','nomeInstituicao',

			];



class UsuarioForm(forms.ModelForm):
	'''
	Responsavel por criar o modelo do form de USers para autenticação!;
	'''
	class Meta:
		model = Usuarios
		fields = ['email','senha','matricula']

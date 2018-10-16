from django import forms
from .models import Professor
from .models import Aluno, Notas
from .models import Usuarios
from .models import AtividadesProfessor
from .models import Disciplinas
from .models import Perguntasx

class DisciplinaAlunoForm(forms.ModelForm):
    class Meta:
        model = Disciplinas
        fields = '__all__'

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        exclude = ['aluno', 'disciplina']
        #disciplina = forms.ModelChoiceField(queryset=Discplina.objects.all(), )
        #fields = '__all__'


class AtividadeObject(forms.ModelForm):
    class Meta:
        model = AtividadesProfessor
        fields = '__all__'

class AtividadeForm(forms.Form):
    opcao = (('A','Alternativa A'),('B','Alternativa B'),('C','Alternativa C'),('D','Alternativa D'))
    titulo = forms.CharField(max_length=200)
    pergunta=forms.CharField(max_length=100)
    alternativa_a = forms.CharField(max_length=200)
    alternativa_b = forms.CharField(max_length=200)
    alternativa_c = forms.CharField(max_length=200)
    alternativa_d = forms.CharField(max_length=200)
    alternativa_correta = forms.ChoiceField(widget=forms.RadioSelect,choices=opcao)

    '''
    	Responsavel por criar uma Atividade q esta relacionada a um Professor
    	Cada atividade precisa ter um Professor.
    	uma Atividade pode ter Diversas Perguntas
    	uma Atividade precisa de um titulo;
    '''


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

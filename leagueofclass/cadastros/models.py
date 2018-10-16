from django.db import models
import datetime
# Create your models here.
# Responsavel por criar os models do cad de professor e aluno
class Pessoa(models.Model):
		options_sexo=(('M','Masculino'),('F','Feminino'),('NDA','Qualquer Outro'))
		nome=models.CharField(max_length=60)
		sexo=models.CharField(max_length=1,choices=options_sexo)
		dataNascimento=models.DateField(("Data"), default=datetime.date.today)
		email=models.CharField(max_length=50)
		login=models.CharField(max_length=20)
		password=models.CharField(max_length=20);

		class Meta:
			verbose_name_plural = "Pessoas"

		def __str__(self):
			return self.nome

class Professor(Pessoa):
	nomeInstituicao=models.CharField(max_length=30)
	#codigo=models.CharField(max_length=10)

	#Adm deleta professor pela matricula;
	matricula=models.CharField(max_length=12,primary_key=True)

	class Meta:
		verbose_name_plural = "Professores"

	def __str__(self):
		return self.nome

class Aluno(Pessoa):
	nomeInstituicao=models.CharField(max_length=30,primary_key=True)
	descricaoDesempenho=models.CharField(max_length=150,blank=True)
	professor=models.ManyToManyField("Professor",blank=True)
	'''
	primeiraUnidade = models.CharField(max_length=4, blank=True)
	segundaUnidade = models.CharField(max_length=4, blank=True)
	terceiraUnidade = models.CharField(max_length=4, blank=True)
	media = models.CharField(max_length=4, blank=True)
	'''
	class Meta:
		verbose_name_plural = "Alunos"

	def __str__(self):
		return self.nome

#Models que eu criei
#daqui

class Frequencia(models.Model):
	#toda vez que é feita uma chamada deve ser criado um novo objeto para cada aluno, de cada disciplina
	options_frequencia=(('Presente', 'Presente'), ('Faltou', 'Faltou'))
	frequencia = models.CharField(max_length=8, choices=options_frequencia)
	data = models.DateField(default=datetime.date.today)
	disciplina = models.ForeignKey('Disciplinas', on_delete=models.CASCADE)
	aluno  = models.ForeignKey('Aluno', on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Frequência"


	def __str__(self):
		return self.disciplina.nomeDisciplina + ' - ' + self.aluno.nome + ' - ' + str(self.data)



class Instituicao(models.Model):
	#usei a lógica de que o admin quem cadastra as intiuições, por isso usei choices
	option_instituicao = (('UFPB', 'UFPB'), ('UFCG', 'UFCG'), ('UEPB', 'UEPB'))
	nome = models.CharField(max_length=10, choices=option_instituicao)
	aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, blank=True)
	professor = models.ForeignKey('Professor', on_delete=models.CASCADE, blank = True)

	class Meta:
		verbose_name_plural = "Instituição"

	def __str__(self):
		return self.nome

#até aqui


class Notas(models.Model):
	aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
	disciplina = models.ForeignKey("Disciplinas", on_delete=models.CASCADE)
	nota1 = models.CharField(max_length=20, default='Nota não cadastrada')
	nota2 = models.CharField(max_length=20, default='Nota não cadastrada')
	nota3 = models.CharField(max_length=20, default='Nota não cadastrada')
	media = models.CharField(max_length=20, default='Nota não cadastrada')

	class Meta:
		verbose_name_plural = "Notas"

	def __str__(self):
		return self.disciplina.nomeDisciplina + ' - ' + self.aluno.nome


class Disciplinas(models.Model):
	nomeDisciplina=models.CharField(max_length=30)
	##descricaoDisciplina=models.CharField(max_length=120)
	professor = models.ForeignKey("Professor",on_delete=models.CASCADE, blank = True, null = True)
	aluno = models.ManyToManyField("Aluno")

	class Meta:
		verbose_name_plural = "Disciplinas"

	def __str__(self):
		return self.nomeDisciplina

class Usuarios(models.Model):
    login=models.CharField(max_length=15)
    senha=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    matricula=models.CharField(max_length=12,blank=True)

class Perguntasx(models.Model):

   opcoes_alternativa_correta = \
   (
   ('A', 'Alternativa A'), ('B', 'Alternativa B'), ('C', 'Alternativa C'), ('D', 'Alternativa D')
   )
   ask=models.CharField(max_length=100,blank=False)
   alternativa_a = models.CharField(max_length=200,blank=False)
   alternativa_b = models.CharField(max_length=200,blank=False)
   alternativa_c = models.CharField(max_length=200,blank=False)
   alternativa_d = models.CharField(max_length=200,blank=False)
   alternativaCorreta = models.CharField(max_length=1,choices=opcoes_alternativa_correta)
   matricula_professor = models.CharField(max_length=100, blank=False)
   titulo= models.CharField(max_length=200,blank=True,unique=False)



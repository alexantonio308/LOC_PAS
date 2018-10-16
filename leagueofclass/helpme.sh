#!/bin/bash

# Inicializa o shell python django e exibe os comandos que estou ulizando
# para verifica de objects no models


function initialize(){
	echo 'Pacotes: Python para utilizacao de Users'
	echo 'Precisa de um superUser?'
	echo 'Comando super user: python3 manage.py createsuperuser'
	echo 'pede: username,password,email'
	echo 'from django.contrib.auth.models import User'
	echo 
	echo '--------------------------------------------'
	echo 'Meus models'
	echo ' from cadastros.models import Professor/Usuarios/Alunos'
	echo ' from django.contrib.auth.models import User'
	echo ' comandos base'
	echo '-------------------------------------------'
	echo
	echo 'User.objects.get(email=ahsuash@hotmail.com).atr '
	echo 'User.objects.create_user(username=x,email=x,password=x)'

	echo ' Professor.objects.get(email=professor@email.com).atributos(matricula,password) '
	echo ''
	python3 manage.py shell
}
dir=$(pwd)

echo 'Diretorio Atual: ' $dir

result_script=(find manage.py)

if [ -z $result_script ]; then
	echo 'Script django nao encontrado!'
else
	initialize
fi


drop() {
    echo "Deletar a tabela com o nome $1_."
    echo
    echo "show tables" | ./manage.py dbshell |
    egrep "^$1_" | xargs -I "@@" echo "DROP TABLE @@;" |
    ./manage.py dbshell
    echo "Tabela dropped."
    echo
}

cancel() {
    echo "Operação Cancelada!."
    echo
}

if [ -z "$1" ]; then
    echo "Nome da tabela precisa ser coerente"
else
    echo "Drop toda as tabelas ? $1_ prefix?"
    select choice in drop cancel;do
        $choice $1
        break
    done
fi

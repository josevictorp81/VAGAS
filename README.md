# VAGAS

Este é um BOT de vagas, scraping que tem como objetivo buscar por vagas para desenvolvedores, estas, são listadas em alguns repositórios do GitHub.

Durante a busca, as informações obtidas são as seguintes: o título da vaga, o link para acessar no repositório e os requisitos para a vaga. Após a busca, essas informações são enviadas via webhook para canais específicos em um servidor no discord.

### Executar

Para execução, siga os seguintes comandos:

- Criar e ativar um ambiente virtual

```
python3 -m venv venv && source venv/bin/activate
```

- Instalar as dependências

```
pip3 install -r requirements.txt
```

- Executar script principal, resposável por buscar e armazenar em um arquivo _jobs.txt_

```
python3 main.py
```

- Executar script que limpa os dados salvos no arquivo _jobs.py_

```
python3 delete.py
```

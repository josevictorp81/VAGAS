# VAGAS

Este é um BOT de vagas, scraping que tem como objetivo buscar por vagas para desenvolvedores, estas, são listadas em alguns repositórios do GitHub.

Durante a busca, as informações trazidas são as seguintes: o título, o link para acessar no repositíorio e os requisitos para a vaga. Após a buscas, essas informações são enviadas via webhook para canais específicos em um servidor no discord.

### Executar

Para executar, primeiro deve-se criar e ativar um ambiente virtual, e executar os seguintes comandos:

-   Instalar as dependências

```
pip3 install -r requirements.txt
```

-   Executar script principal, resposável pela buscar e armazenar em um arquivo _jobs.txt_

```
python3 main.py
```

-   Executar script que limpa os dados salvos no arquivo _jobs.py_

```
python3 delete.py
```

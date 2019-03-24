# Interpretação Automática de Artigos Científicos

Este repositório apresenta duas soluçoes para analisar dados em artigos científicos:

* Preprocessa, gera token e uma nuvem de palavras do texto de artigos científicos a partir de uma pasta local de destino;

* Analisa os metados de artigos científicos a partir de um arquivo .json gerado pelo software Zotero;

## Como Usar

Cada arquivo apresenta um classe modularizada para ser reutilizada referente a sua funçao. Mas os arquivos também pode ser executados diretamente pelo terminal a partir dos argumentos que detalhados abaixo:

### PDF Reader

Exemplo:
```
python pdfReader.py --path 'home/artigos'
```
Argumentos:
* --path, -p: Pasta com os pdf's **(Obrigatório)**;
* --wordcloud, -p: True: gera uma nuvem de palavras, False: apenas printa os tokens gerados (Default: True);
* --stopwords, -s: Uma lista python com stopwords adicionais as geradas pelo NLTK na linguagem especificada (Default: ['et', 'al']);
* --language, -l: Linguagem dos pdf's (Default: 'enlgish').

**Obs:** Para gerar uma nuvem de palavras com com conjunto específico de palavras, coloque-as em um arquivo e salve no formato pdf. Use a classe pdfReader() neste arquivo normalmente.

**Obs2:** Caso o argumento --wordcloud seja colocado como falso, o método apenas irá retornar a lista de tokens gerados no terminal.

### Zotero Json Reader

Exemplo:
```
python zoteroJsonReader.py --path 'example.json'
```
Argumentos:
* --path, -p: Caminho do arquivo json **(Obrigatório)**;
* --infos, -i: Lista de informaçoes para serem (Default: todos os possíveis = ['type', 'source', 'language', 'event', 'author', 'date']);

**Obs**: Certifique que o arquivo .json gerado pelo software Zotero tenha todos os campos de interesse preenchidos, caso contrário o método acusará index error para o campo que esteja faltando.

### Dependencias

* Python 3.x
* Textract
* NLTK
* Argparse

## Autor

* **Albano Borba** - albano.b06@gmail.com


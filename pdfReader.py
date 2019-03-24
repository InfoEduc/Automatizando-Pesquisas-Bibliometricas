'''
Classe pdfReader que a partir do caminho de pdf, extrai texto contido nele

Argumentos:
path: caminho do pdf (OBRIGATORIO)
language: linguagem do pdf
stopw: stopwords adicionais alem das fornecidas pelo NLTK na linguagem escolhida
'''

import textract
import nltk
from nltk.corpus import stopwords

class PDFReader(object):
    def __init__(self, path, language = 'english', add_stopwords = []):
        
        # Linaguagem do pdf, ingles padrao
        self.language = language
        self.bytes = textract.process(path)
        self.add_stopwords = add_stopwords

        # Preprocessamento do texto ainda em bytes
        self.preprocess()

    def preprocess(self):
        # Conversao para string
        self.text = self.bytes.decode("utf-8")

        # Remoçao de quebras de linhas
        self.text = self.text.replace('\n', ' ')
        
        # Biblio NLTK para tokenizar o texto
        self.text = nltk.word_tokenize(self.text)
         # Remoçao de pontuaçaoes e letras maiusculas
        self.text = [i.lower() for i in self.text if i.isalnum()]
        # Conjunto de stopwords da linguagem
        stop = set(stopwords.words(self.language) + self.add_stopwords)

        # Remove todas as stopwrods do texto
        self.preprocess_text = [i for i in self.text if i not in stop]    

    def getText(self):
        # Retorna uma lista de strings que compoem o texto completo (raw)
        return self.text

    def getTokens(self):
        # Retorna uma lista de tokens preprocessados do texto completo
        return self.preprocess_text

if __name__ == '__main__':
    
    import os
    import argparse
    import wordCloudGenerator

    # Parser dos argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', required=True, help='Caminho para a pasta com os arquivos pdf')
    parser.add_argument('--wordcloud', '-w', default=True, help='Gerar nuvem de palavras com os tokens gerados (Default = True)')
    parser.add_argument('--stopwords', '-s', default=['et', 'al'], help="Lista python com stopwords adiconais (Default = ['et', 'al'])")
    parser.add_argument('--language', '-l', default='english', help="Linguagem dos papers (Default = english")

    arguments = parser.parse_args()

    # Percorre todos os pdf da pasta indicada recolhendo os respectivos tokens
    tokens = []
    for file in os.listdir(arguments.path):
        if file.endswith(".pdf"):
            reader = PDFReader(arguments.path+'/'+file, language=arguments.language, add_stopwords=arguments.stopwords)
            tokens = reader.getTokens() + tokens

    # Gera a word cloud ou printa o conjunto de tokens gerado
    if arguments.wordcloud:
        wc = wordCloudGenerator.wordCloud(tokens)
        wc.generator()
    else:
        print(tokens)
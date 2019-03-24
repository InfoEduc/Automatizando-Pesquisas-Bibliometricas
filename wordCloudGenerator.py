'''
Classe wordCloudGenerator que a partir de um conjunto de token gera uma nuvem de palavra

Argumentos:
text: lista de token (preferencilmente geradas pela classe pdfReader) (OBRIGATORIO)
max_font_size: tamanho maximo das palavras na nuvem
max_words: numero maximo de palavras na nuvem
background_color: color de fundo da nuvem
'''

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

class wordCloud(object):
    def __init__(self, text, max_font_size=50, max_words=100, background_color="white"):
        
        # Transforma token em uma string unica
        self.text = ' '.join(text)
        self.wordcloud = WordCloud(max_font_size=max_font_size, max_words=max_words, background_color=background_color).generate(self.text)

    def generator(self):
        # Gera e plota a wordcloud
        plt.imshow(self.wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def save(self, file_name):
        # Gera e salva no diretorio atual a wordcloud
        self.wordcloud.to_file(file_name)

if __name__ == '__main__':
    # Exemplo de uso da classe

    import pdfReader as pdf

    # classe pdfReader para gerar o conjunto de tokens do pdf e stopwords adicionais como parametro
    reader = pdf.PDFReader('example.pdf', add_stopwords=['et', 'al'])

    # classe wordCloud com os tokens gerados como parametros
    wc = wordCloud(reader.getTokens())
    
    # Plota e salva
    wc.generator()
    #wc.save('wc.png')
'''
Classe ZoteroJsonReader que le um arquivo json com um conjunto de metadatos gerado pelo software Zotero

ATENÇAO: Certifique-se de que o arquivo no formato json esteja com os todos os metadados que deseja 
buscar em todos os artigos

Argumentos:
path: caminho do arquivo json (OBRIGATORIO)
infos: conjuntos de informacoes que deseja buscar. Default: todas possíveis
'''

import json
from collections import Counter
from pprint import pprint

class ZoteroJsonReader(object):
    def __init__(self):
        pass

    def processJson(self, path, infos=['type', 'source', 'language', 'event', 'author', 'date']):
        self.infos = infos
        
        # Le o arquivo json lozalizado em path
        with open(path) as f:
            self.data = json.load(f)

        # Inicializa um dicionario para as infos selecionadas
        raw = {}
        for info in infos:
            raw[info] = []

        # Percorre todas as intancias (metadados de artigos) do arquivo json
        for d in self.data:
            
            # Encontra cada info em cada instancia
            if 'type' in infos:
                raw['type'].append(d['type'])
            if 'source' in infos:
                raw['source'].append(d['source'])
            if 'language' in infos:            
                raw['language'].append(d['language'])
            if 'event' in infos:
                raw['event'].append(d['event'])
            if 'date' in infos:    
                raw['date'].append(d['issued']['date-parts'][0][0])
            if 'author' in infos:    
                for author in d['author']:
                    raw['author'].append(author['family'] + ', ' + author['given'])

        # Conta a ocorrencia de cada papes em cada info
        out = {}
        for r in raw:
            out[r] = Counter(raw[r])

        # Printa no terminal o dicionario final
        pprint(out)

if __name__ == '__main__':   

    import os
    import argparse

    # Parser dos argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', required=True, help='Caminho do arquivo json')
    parser.add_argument('--infos', '-i', default=['type', 'source', 'language', 'event', 'author', 'date'], help='Lista python de infos a serem retiradas do arquivo (Default = Todas)')
    
    arguments = parser.parse_args()

    # Instancia um objeto ZoteroJsonReader
    reader = ZoteroJsonReader()

    # Invoca o metodo processJson com o caminho do arquivo e as infos desejadas
    reader.processJson(arguments.path, infos=arguments.infos)

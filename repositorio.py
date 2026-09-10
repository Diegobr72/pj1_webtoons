import os
from constantes import ARQUIVO_CSV, SEPARADOR
from modelos import Webtoon

class RepositorioCSV:
    def __init__(self, caminho_arquivo=ARQUIVO_CSV):
        self.caminho_arquivo = caminho_arquivo
        if not self.existe():
            self.inicializar()

    def existe(self):
        return os.path.exists(self.caminho_arquivo)

    def inicializar(self):
        with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            cabecalho = f"titulo{SEPARADOR}nota_media{SEPARADOR}ranking{SEPARADOR}popularidade{SEPARADOR}capitulos{SEPARADOR}situacao{SEPARADOR}genero"
            arquivo.write(cabecalho + "\n")

    def _valor_para_csv(self, valor):
        if valor is None:
            return ""
        return str(valor)

    def salvar(self, obra):
        with open(self.caminho_arquivo, 'a', encoding='utf-8') as arquivo:
            campos = [
                self._valor_para_csv(obra.titulo),
                self._valor_para_csv(obra.nota_media),
                self._valor_para_csv(obra.ranking),
                self._valor_para_csv(obra.popularidade),
                self._valor_para_csv(obra.capitulos),
                self._valor_para_csv(obra.situacao),
                self._valor_para_csv(obra.genero)
            ]
            linha = SEPARADOR.join(campos)
            arquivo.write(linha + "\n")

    def salvar_todas(self, obras):
        self.inicializar()
        for obra in obras:
            self.salvar(obra)

    def contar(self):
        contador = 0
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            next(arquivo) 
            for linha in arquivo:
                if linha.strip():
                    contador += 1
        return contador

    def buscar_todas(self):
        obras = []
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            next(arquivo) 
            for linha in arquivo:
                linha_limpa = linha.strip()
                if linha_limpa:
                    obras.append(self._criar_obra_de_linha(linha_limpa))
        return obras

    def _csv_para_float(self, valor):
        valor = valor.strip()
        if not valor:
            return None
        return float(valor)

    def _csv_para_int(self, valor):
        valor = valor.strip()
        if not valor:
            return None
        return int(float(valor))

    def _csv_para_str(self, valor):
        valor = valor.strip()
        if not valor:
            return None
        return valor

    def _criar_obra_de_linha(self, linha):
        campos = linha.split(SEPARADOR)
        return Webtoon(
            titulo=campos[0].strip(),
            nota_media=self._csv_para_float(campos[1]),
            ranking=self._csv_para_int(campos[2]) or 0,
            popularidade=self._csv_para_int(campos[3]),
            capitulos=self._csv_para_int(campos[4]),
            situacao=self._csv_para_str(campos[5]),
            genero=self._csv_para_str(campos[6]) if len(campos) > 6 else None
        )


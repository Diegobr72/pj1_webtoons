from constantes import (
    NOTA_MINIMA, NOTA_MAXIMA,
    RANKING_MINIMO, POPULARIDADE_MINIMA,
    CAPITULOS_MINIMO
)

class Validador:
    @staticmethod
    def validar_nota(valor):
        return NOTA_MINIMA <= valor <= NOTA_MAXIMA

    @staticmethod
    def validar_ranking(valor):
        return valor >= RANKING_MINIMO

    @staticmethod
    def validar_popularidade(valor):
        return valor >= POPULARIDADE_MINIMA

    @staticmethod
    def validar_capitulos(valor):
        return valor >= CAPITULOS_MINIMO

    @staticmethod
    def validar_situacao(texto):
        situacoes_validas = ["em publicacao", "concluida", "cancelada", "em hiato"]
        return texto in situacoes_validas

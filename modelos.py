from constantes import (
    NOTA_BAIXA_LIMITE,
    NOTA_INTERMEDIARIA_LIMITE,
    RANKING_DESTAQUE_ALTO,
    RANKING_DESTAQUE_INTERMEDIARIO
)

class Webtoon:
    def __init__(self, titulo, nota_media=None, ranking=0, popularidade=None, capitulos=None, situacao=None, genero=None):
        self.titulo = titulo
        self.nota_media = nota_media
        self.ranking = ranking
        self.popularidade = popularidade
        self.capitulos = capitulos
        self.situacao = situacao
        self.genero = genero

    def classificar_por_nota(self):
        if self.nota_media is None:
            return "Sem nota"
        if self.nota_media < NOTA_BAIXA_LIMITE:
            return "Nota baixa"
        elif self.nota_media < NOTA_INTERMEDIARIA_LIMITE:
            return "Nota intermediaria"
        else:
            return "Nota alta"

    def classificar_por_ranking(self):
        if self.ranking is None or self.ranking == 0:
            return "Sem ranking"
        if self.ranking <= RANKING_DESTAQUE_ALTO:
            return "Destaque alto"
        elif self.ranking <= RANKING_DESTAQUE_INTERMEDIARIO:
            return "Destaque intermediario"
        else:
            return "Destaque menor"

    def campos_faltantes(self):
        faltantes = []
        if self.nota_media is None:
            faltantes.append("nota_media")
        if self.popularidade is None:
            faltantes.append("popularidade")
        if self.capitulos is None:
            faltantes.append("capitulos")
        if self.situacao is None:
            faltantes.append("situacao")
        if self.genero is None:
            faltantes.append("genero")
        return faltantes

    def esta_completa(self):
        return len(self.campos_faltantes()) == 0

    def _formatar_valor(self, valor):
        if valor is None:
            return "(nao informado)"
        return valor

    def exibir_dados(self):
        print(f"  Titulo:           {self.titulo}")
        print(f"  Nota media:       {self._formatar_valor(self.nota_media)}")
        print(f"  Ranking:          {self._formatar_valor(self.ranking)}")
        print(f"  Popularidade:     {self._formatar_valor(self.popularidade)}")
        print(f"  Capitulos:        {self._formatar_valor(self.capitulos)}")
        print(f"  Situacao:         {self._formatar_valor(self.situacao)}")
        print(f"  Genero:           {self._formatar_valor(self.genero)}")
        print(f"  Classif. nota:    {self.classificar_por_nota()}")
        print(f"  Classif. ranking: {self.classificar_por_ranking()}")

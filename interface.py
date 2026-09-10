from constantes import (
    NOTA_MINIMA, NOTA_MAXIMA, RANKING_MINIMO,
    POPULARIDADE_MINIMA, CAPITULOS_MINIMO, SEPARADOR
)
from modelos import Webtoon
from validacoes import Validador

class InterfaceUsuario:
    def exibir_menu_principal(self):
        print("\n" + "=" * 50)
        print("      ANALISE DE WEBTOONS E MANHWA")
        print("=" * 50)
        print("  1. cadastrar dados das obras ")
        print("  2. Exibir estatisticas")
        print("  3. Classificar obra com dados incompletos")
        print("  4. Filtrar obras por criterio")
        print("  5. Exibir dados de todas as obras")
        print("  0. Sair")
        print("=" * 50)

    def exibir_menu_filtros(self):
        print("\n" + "-" * 50)
        print("  FILTRAR OBRAS POR CRITERIO")
        print("-" * 50)
        print("  1. Nota minima")
        print("  2. Posicao maxima no ranking")
        print("  3. Quantidade minima de capitulos")
        print("  4. Situacao da obra")
        print("  5. Genero principal")
        print("-" * 50)

    def ler_float(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("  [ERRO] Por favor, digite um numero valido.")

    def ler_inteiro(self, mensagem):
        while True:
            try:
                return int(input(mensagem))
            except ValueError:
                print("  [ERRO] Por favor, digite um numero inteiro valido.")

    def ler_nota(self):
        while True:
            valor = self.ler_float("  Nota media (0 a 100): ")
            if Validador.validar_nota(valor):
                return valor
            print(f"  [ERRO] A nota deve estar entre {NOTA_MINIMA} e {NOTA_MAXIMA}.")

    def ler_popularidade(self):
        while True:
            valor = self.ler_inteiro("  Popularidade (inteiro nao negativo): ")
            if Validador.validar_popularidade(valor):
                return valor
            print(f"  [ERRO] A popularidade deve ser >= {POPULARIDADE_MINIMA}.")

    def ler_capitulos(self):
        while True:
            valor = self.ler_inteiro("  Quantidade de capitulos (inteiro nao negativo): ")
            if Validador.validar_capitulos(valor):
                return valor
            print(f"  [ERRO] A quantidade deve ser >= {CAPITULOS_MINIMO}.")

    def ler_situacao(self):
        opcoes = {
            1: "em publicacao",
            2: "concluida",
            3: "cancelada",
            4: "em hiato"
        }
        while True:
            print("  Opcoes de situacao:")
            print("  1. em publicacao")
            print("  2. concluida")
            print("  3. cancelada")
            print("  4. em hiato")
            escolha = self.ler_inteiro("  Escolha a situacao (1 a 4): ")
            if escolha in opcoes:
                return opcoes[escolha]
            print("  [ERRO] Escolha invalida. Tente novamente.")

    def ler_titulo(self):
        while True:
            titulo = input("  Titulo: ").strip()
            if not titulo:
                print("  [ERRO] O titulo nao pode ser vazio.")
            elif SEPARADOR in titulo:
                print(f"  [ERRO] O titulo nao pode conter o caractere '{SEPARADOR}'.")
            else:
                return titulo

    def ler_genero(self):
        while True:
            genero = input("  Genero principal: ").strip()
            if not genero:
                print("  [ERRO] O genero nao pode ser vazio.")
            elif SEPARADOR in genero:
                print(f"  [ERRO] O genero nao pode conter o caractere '{SEPARADOR}'.")
            else:
                return genero

    def ler_nota_opcional(self):
        entrada = input("  Nota media (0 a 100) [Enter para pular]: ").strip()
        if not entrada:
            return None
        try:
            valor = float(entrada)
        except ValueError:
            print("  [!] Dados invalidos. Campo ignorado.")
            return None
        if not Validador.validar_nota(valor):
            print(f"  [!] Dados invalidos. A nota deve estar entre {NOTA_MINIMA} e {NOTA_MAXIMA}. Campo ignorado.")
            return None
        return valor

    def ler_popularidade_opcional(self):
        entrada = input("  Popularidade (inteiro >= 0) [Enter para pular]: ").strip()
        if not entrada:
            return None
        try:
            valor = int(entrada)
        except ValueError:
            print("  [!] Dados invalidos. Campo ignorado.")
            return None
        if not Validador.validar_popularidade(valor):
            print(f"  [!] Dados invalidos. Popularidade deve ser >= {POPULARIDADE_MINIMA}. Campo ignorado.")
            return None
        return valor

    def ler_capitulos_opcional(self):
        entrada = input("  Quantidade de capitulos (>= 0) [Enter para pular]: ").strip()
        if not entrada:
            return None
        try:
            valor = int(entrada)
        except ValueError:
            print("  [!] Dados invalidos. Campo ignorado.")
            return None
        if not Validador.validar_capitulos(valor):
            print(f"  [!] Dados invalidos. Capitulos deve ser >= {CAPITULOS_MINIMO}. Campo ignorado.")
            return None
        return valor

    def ler_situacao_opcional(self):
        print("  Opcoes de situacao:")
        print("  1. em publicacao")
        print("  2. concluida")
        print("  3. cancelada")
        print("  4. em hiato")
        entrada = input("  Escolha a situacao (1 a 4) [Enter para pular]: ").strip()
        if not entrada:
            return None
        opcoes = {1: "em publicacao", 2: "concluida", 3: "cancelada", 4: "em hiato"}
        try:
            escolha = int(entrada)
        except ValueError:
            print("  [!] Dados invalidos. Campo ignorado.")
            return None
        if escolha not in opcoes:
            print("  [!] Dados invalidos. Opcao inexistente. Campo ignorado.")
            return None
        return opcoes[escolha]

    def ler_genero_opcional(self):
        entrada = input("  Genero principal [Enter para pular]: ").strip()
        if not entrada:
            return None
        if SEPARADOR in entrada:
            print(f"  [!] Dados invalidos. Genero nao pode conter '{SEPARADOR}'. Campo ignorado.")
            return None
        return entrada

    def coletar_dados_obra(self):
        print(f"\n--- Inserir Nova Obra ---")
        print("  (Pressione Enter para pular campos opcionais)\n")
        
        titulo = self.ler_titulo()
        nota_media = self.ler_nota_opcional()
        popularidade = self.ler_popularidade_opcional()
        capitulos = self.ler_capitulos_opcional()
        situacao = self.ler_situacao_opcional()
        genero = self.ler_genero_opcional()

        obra = Webtoon(titulo, nota_media, 0, popularidade, capitulos, situacao, genero)

        print(f"\n  [OK] Obra '{titulo}' registrada com sucesso!")
        if obra.esta_completa():
            print(f"    Classificacao por nota: {obra.classificar_por_nota()}")
        else:
            campos = obra.campos_faltantes()
            nomes_legveis = {
                "nota_media": "Nota media",
                "popularidade": "Popularidade",
                "capitulos": "Capitulos",
                "situacao": "Situacao",
                "genero": "Genero"
            }
            faltantes_str = ", ".join(nomes_legveis.get(c, c) for c in campos)
            print(f"    [AVISO] Dados incompletos. Faltam: {faltantes_str}")
            print(f"    Use a opcao 3 para completar a classificacao desta obra.")

        return obra

    def listar_obras_incompletas(self, obras_incompletas):
        print("\n" + "=" * 50)
        print("   CLASSIFICAR OBRA COM DADOS INCOMPLETOS")
        print("=" * 50)
        nomes_legveis = {
            "nota_media": "Nota media",
            "popularidade": "Popularidade",
            "capitulos": "Capitulos",
            "situacao": "Situacao",
            "genero": "Genero"
        }
        for i, obra in enumerate(obras_incompletas, 1):
            campos = obra.campos_faltantes()
            faltantes_str = ", ".join(nomes_legveis.get(c, c) for c in campos)
            print(f"  {i}. {obra.titulo} - Faltam: {faltantes_str}")
        print("  0. Voltar ao menu")
        print("=" * 50)

    def coletar_dados_faltantes(self, obra):
        campos = obra.campos_faltantes()
        print(f"\n  Completando dados de '{obra.titulo}':")
        print(f"  (Preencha os campos faltantes. Enter para manter vazio.)\n")

        if "nota_media" in campos:
            valor = self.ler_nota_opcional()
            if valor is not None:
                obra.nota_media = valor

        if "popularidade" in campos:
            valor = self.ler_popularidade_opcional()
            if valor is not None:
                obra.popularidade = valor

        if "capitulos" in campos:
            valor = self.ler_capitulos_opcional()
            if valor is not None:
                obra.capitulos = valor

        if "situacao" in campos:
            valor = self.ler_situacao_opcional()
            if valor is not None:
                obra.situacao = valor

        if "genero" in campos:
            valor = self.ler_genero_opcional()
            if valor is not None:
                obra.genero = valor

        return obra

    def exibir_resultado_classificacao(self, obra):
        print(f"\n  Resultado da classificacao de '{obra.titulo}':")
        print("-" * 50)
        obra.exibir_dados()
        if obra.esta_completa():
            print(f"\n  [OK] Obra completamente classificada!")
        else:
            campos = obra.campos_faltantes()
            nomes_legveis = {
                "nota_media": "Nota media",
                "popularidade": "Popularidade",
                "capitulos": "Capitulos",
                "situacao": "Situacao",
                "genero": "Genero"
            }
            faltantes_str = ", ".join(nomes_legveis.get(c, c) for c in campos)
            print(f"\n  [AVISO] Ainda faltam dados: {faltantes_str}")
        print("=" * 50)

    def mensagem(self, texto):
        print(texto)

    def mensagem_aviso_vazio(self, titulo_secao):
        print("\n" + "=" * 50)
        print(f"  {titulo_secao}")
        print("=" * 50)
        print("  [AVISO] Nenhuma obra cadastrada. Por favor,")
        print("  cadastre obras na opcao 1 primeiro.")
        print("=" * 50)

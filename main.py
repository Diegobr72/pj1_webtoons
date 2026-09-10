from repositorio import RepositorioCSV
from gerenciador import GerenciadorWebtoons
from interface import InterfaceUsuario

class Aplicacao:
    def __init__(self):
        self.repositorio = RepositorioCSV()
        self.gerenciador = GerenciadorWebtoons(self.repositorio)
        self.interface = InterfaceUsuario()

    def processar_filtro(self):
        self.interface.exibir_menu_filtros()
        opcao_filtro = self.interface.ler_inteiro("  Escolha o filtro: ")

        if opcao_filtro == 1:
            nota_min = self.interface.ler_float("  Informe a nota minima: ")
            self.gerenciador.filtrar_por_nota_minima(nota_min)
        elif opcao_filtro == 2:
            ranking_max = self.interface.ler_inteiro("  Informe a posicao maxima no ranking: ")
            self.gerenciador.filtrar_por_ranking_maximo(ranking_max)
        elif opcao_filtro == 3:
            cap_min = self.interface.ler_inteiro("  Informe a quantidade minima de capitulos: ")
            self.gerenciador.filtrar_por_capitulos_minimos(cap_min)
        elif opcao_filtro == 4:
            situacao = self.interface.ler_situacao()
            self.gerenciador.filtrar_por_situacao(situacao)
        elif opcao_filtro == 5:
            genero = self.interface.ler_genero()
            self.gerenciador.filtrar_por_genero(genero)
        else:
            print("  [ERRO] Opcao de filtro invalida.")

    def executar(self):
        self.interface.mensagem("\n" + "=" * 50)
        self.interface.mensagem("  Bem-vindo ao Sistema de Analise de Webtoons!")
        self.interface.mensagem("=" * 50)

        while True:
            self.interface.exibir_menu_principal()
            opcao = self.interface.ler_inteiro("  Escolha uma opcao: ")

            if opcao == 1:
                obra = self.interface.coletar_dados_obra()
                rank_atribuido = self.gerenciador.cadastrar_obra(obra)
                if obra.nota_media is not None:
                    print(f"    Classificacao por ranking: {obra.classificar_por_ranking()} (Posicao calculada: {rank_atribuido})")

            elif opcao == 2:
                sucesso = self.gerenciador.exibir_estatisticas()
                if not sucesso:
                    self.interface.mensagem_aviso_vazio("ESTATISTICAS")

            elif opcao == 3:
                self.gerenciador.classificar_obra_incompleta(self.interface)

            elif opcao == 4:
                if self.repositorio.contar() == 0:
                    self.interface.mensagem_aviso_vazio("FILTROS")
                else:
                    self.processar_filtro()

            elif opcao == 5:
                sucesso = self.gerenciador.exibir_todas_obras()
                if not sucesso:
                    self.interface.mensagem_aviso_vazio("DADOS DE TODAS AS OBRAS")

            elif opcao == 0:
                self.interface.mensagem("\n  Programa encerrado. Ate logo!")
                break

            else:
                self.interface.mensagem("  [ERRO] Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    app = Aplicacao()
    app.executar()

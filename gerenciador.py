class GerenciadorWebtoons:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def _atualizar_rankings(self, obras):
        obras_com_nota = [o for o in obras if o.nota_media is not None]
        obras_sem_nota = [o for o in obras if o.nota_media is None]

        obras_com_nota.sort(key=lambda x: x.nota_media, reverse=True)
        for i, obra in enumerate(obras_com_nota, 1):
            obra.ranking = i

        for obra in obras_sem_nota:
            obra.ranking = 0

        return obras_com_nota + obras_sem_nota

    def cadastrar_obra(self, obra):
        obras = self.repositorio.buscar_todas()
        obras.append(obra)

        obras_atualizadas = self._atualizar_rankings(obras)
        self.repositorio.salvar_todas(obras_atualizadas)

        return obra.ranking

    def classificar_obra_incompleta(self, interface):
        obras = self.repositorio.buscar_todas()

        if not obras:
            interface.mensagem_aviso_vazio("CLASSIFICAR OBRA")
            return

        obras_incompletas = [o for o in obras if not o.esta_completa()]

        if not obras_incompletas:
            print("\n" + "=" * 50)
            print("  [INFO] Todas as obras ja possuem dados completos!")
            print("=" * 50)
            return

        interface.listar_obras_incompletas(obras_incompletas)
        escolha = interface.ler_inteiro("  Escolha a obra para completar: ")

        if escolha == 0:
            return

        if escolha < 1 or escolha > len(obras_incompletas):
            print("  [ERRO] Opcao invalida.")
            return

        obra_selecionada = obras_incompletas[escolha - 1]

        interface.coletar_dados_faltantes(obra_selecionada)
        obras_atualizadas = self._atualizar_rankings(obras)
        self.repositorio.salvar_todas(obras_atualizadas)
        interface.exibir_resultado_classificacao(obra_selecionada)

    def exibir_estatisticas(self):
        obras = self.repositorio.buscar_todas()

        if not obras:
            return False

        quantidade = len(obras)

        obras_com_nota = [o for o in obras if o.nota_media is not None]
        obras_com_pop = [o for o in obras if o.popularidade is not None]
        obras_com_rank = [o for o in obras if o.ranking is not None and o.ranking > 0]

        print("\n" + "=" * 50)
        print("          ESTATISTICAS DAS OBRAS")
        print("=" * 50)
        print(f"  Quantidade de obras analisadas:  {quantidade}")

        if obras_com_nota:
            soma_notas = sum(obra.nota_media for obra in obras_com_nota)
            media_notas = soma_notas / len(obras_com_nota)
            obra_maior_nota = max(obras_com_nota, key=lambda o: o.nota_media)
            obra_menor_nota = min(obras_com_nota, key=lambda o: o.nota_media)
            contador_acima_media = sum(1 for obra in obras_com_nota if obra.nota_media > media_notas)

            print(f"  Maior nota:                      {obra_maior_nota.nota_media} ({obra_maior_nota.titulo})")
            print(f"  Menor nota:                      {obra_menor_nota.nota_media} ({obra_menor_nota.titulo})")
            print(f"  Nota media das obras:            {media_notas:.2f}")
            print(f"  Obras acima da media:            {contador_acima_media}")
        else:
            print("  [AVISO] Nenhuma obra possui nota para calcular estatisticas.")

        contador_concluidas = sum(1 for obra in obras if obra.situacao == "concluida")
        contador_em_publicacao = sum(1 for obra in obras if obra.situacao == "em publicacao")
        print(f"  Obras concluidas:                {contador_concluidas}")
        print(f"  Obras em publicacao:             {contador_em_publicacao}")

        if obras_com_pop:
            obra_maior_pop = max(obras_com_pop, key=lambda o: o.popularidade)
            print(f"  Maior popularidade:              {obra_maior_pop.popularidade} ({obra_maior_pop.titulo})")

        if obras_com_rank:
            obra_melhor_rank = min(obras_com_rank, key=lambda o: o.ranking)
            print(f"  Melhor posicao no ranking:       {obra_melhor_rank.ranking} ({obra_melhor_rank.titulo})")

        obras_incompletas = [o for o in obras if not o.esta_completa()]
        if obras_incompletas:
            print(f"  Obras com dados incompletos:     {len(obras_incompletas)}")

        print("=" * 50)
        return True

    def _exibir_resultados_filtro(self, resultados, criterio_desc):
        print(f"\n  {criterio_desc}:")
        if not resultados:
            print("    [!] Nenhuma obra encontrada com esse criterio.")
        else:
            for i, obra in enumerate(resultados, 1):
                print(f"\n  -- Resultado {i} --")
                obra.exibir_dados()
        print("-" * 50)

    def filtrar_por_nota_minima(self, nota_min):
        resultados = [o for o in self.repositorio.buscar_todas() if o.nota_media is not None and o.nota_media >= nota_min]
        self._exibir_resultados_filtro(resultados, f"Obras com nota >= {nota_min}")

    def filtrar_por_ranking_maximo(self, ranking_max):
        resultados = [o for o in self.repositorio.buscar_todas() if o.ranking is not None and o.ranking > 0 and o.ranking <= ranking_max]
        self._exibir_resultados_filtro(resultados, f"Obras com ranking <= {ranking_max}")

    def filtrar_por_capitulos_minimos(self, cap_min):
        resultados = [o for o in self.repositorio.buscar_todas() if o.capitulos is not None and o.capitulos >= cap_min]
        self._exibir_resultados_filtro(resultados, f"Obras com capitulos >= {cap_min}")

    def filtrar_por_situacao(self, situacao_filtro):
        resultados = [o for o in self.repositorio.buscar_todas() if o.situacao is not None and o.situacao == situacao_filtro]
        self._exibir_resultados_filtro(resultados, f"Obras com situacao '{situacao_filtro}'")

    def filtrar_por_genero(self, genero_filtro):
        resultados = [o for o in self.repositorio.buscar_todas() if o.genero is not None and o.genero.lower() == genero_filtro.lower()]
        self._exibir_resultados_filtro(resultados, f"Obras do genero '{genero_filtro}'")

    def exibir_todas_obras(self):
        obras = self.repositorio.buscar_todas()
        if not obras:
            return False

        print("\n" + "=" * 50)
        print("         DADOS DE TODAS AS OBRAS")
        print("=" * 50)
        for i, obra in enumerate(obras, 1):
            print(f"\n  -- Obra {i} --")
            obra.exibir_dados()
        print("=" * 50)
        return True


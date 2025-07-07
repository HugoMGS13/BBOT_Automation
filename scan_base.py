import pandas as pd 
import abc #Abstract Base Class
#Seria como uma interface em Java, ela cria um contrato com as classes que a utilizam
import random 
import asyncio
from bbot.scanner import Scanner
#Importando o scan do BBOT

class PerfilDeScanBase(abc.ABC):

    name: str = "Nome do Perfil Indefinido"
    description: str = "Descrição do Perfil Indefinida"
    modules: list[str] = []
    presets: list[str] = []
    config: dict = {}
    #Atributos 

    def __init__(self, targets: list[str], output_filename: str):
    #Construtor da classe PerfilDeScanBase
        if not targets:
            raise ValueError("A lista de alvos não pode ser vazia.")
        
        self.targets = targets
        self.output_filename = f"{output_filename.replace(' ', '_')}_{str(random.randint(1, 40))}"
        self.scan_name = f"{self.name.replace(' ', '_')}_{str(random.randint(1, 40))}"
        #Criando o nome do scan com a string retornada + seu horário de criação

    async def run(self):
    #Main
        print(f"\n--- Iniciando Scan do Perfil: '{self.name}' ---")
        print(f"Alvos: {self.targets}")
        print(f"Módulos: {self.modules}")
        print(f'Presets: {self.presets}')

        resultados_scan = []
        #Lista que vai armazenar os resultados do scan

        final_config = self.config.copy()
        final_config['scan_name'] = self.scan_name

        targets = self.targets

        scan_instance = Scanner(
            #Criando o scan

            #Alvo
            *targets,

            #Presets
            presets=self.presets, 

            #Módulos
            modules=self.modules, 

            #Configurações
            config=final_config
        )
        
        async for event in scan_instance.async_start():
            #Usamos o async para adicionar cada informação enquanto o scan roda, fazendo as duas coisas em concorrência

            # Criamos um dicionário base com informações que todo evento terá
            dados_base = {
                'event_type': event.type,
                'event_module': event.module
            }
            
            # Verificamos se o dado principal (event.data) é um dicionário
            if isinstance(event.data, dict):

                # Se for, podemos mesclar os dois dicionários (O criado e o padrão do BBOT) para ter uma linha completa
                dados_completos = dados_base | event.data

            else:
                # Se não for (ex: é um texto), criamos uma chave 'message' para armazená-lo
                dados_completos = dados_base

                dados_completos['message'] = str(event.data) # Converte para string por segurança
            
            # Adicionamos o dicionário à nossa lista
            resultados_scan.append(dados_completos)

        print("INFO: Scan finalizado. Tratando o output com o Pandas...")

        if not resultados_scan:
            print("WARN: Nenhum evento foi gerado pelo scan.")
            return
        #Caso o scan não rode ou não traga resultados

        df_bruto = pd.DataFrame(resultados_scan)
        #Criando um DataFrame com os resultados do scan

        colunas_desejadas = ['event_type', 'event_module', 'message', 'host', 'technology']
        #Informando as únicas colunas que queremos ver

        colunas_existentes = df_bruto.columns.tolist()
        #LIstando as colunas que existem no dataframe bruto

        colunas_finais = [coluna for coluna in colunas_desejadas if coluna in colunas_existentes]
        #Filtrando o dataframe para mostrar apenas as colunas que queremos

        if colunas_finais:
            
            # Criamos o novo DataFrame usando a lista de colunas válidas
            df_tratado = df_bruto[colunas_finais]

            nome_arquivo = f'{self.output_filename}.xlsx'

            print("\n--- DataFrame Final e Tratado ---\n")
            print(df_tratado)

            #Com o DataFrame filtrado, nós exportamos para uma pasta em formato xlsx
            try:
                df_tratado.to_excel(f'/home/sec/Documentos/projetoBBOT/scans/{nome_arquivo}')
            except Exception as e:
                print(f"ERRO ao exportar para Excel: {e}")
                
        else:
            print("\nERRO: Nenhuma das colunas desejadas foi encontrada no DataFrame original.")

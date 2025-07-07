import asyncio
import os
import pkgutil
import importlib
from scan_base import PerfilDeScanBase

def descobrir_e_carregar_perfis(caminho_pacote):
 
    print("INFO: Procurando perfis de scan...")
    caminho_real = os.path.join(os.path.dirname(__file__), caminho_pacote)
    #Monta o caminho completo e absoluto para a pasta dos perfis
    
    #Itera sobre todos os módulos Python na pasta de perfis
    for (_, module_name, _) in pkgutil.iter_modules([caminho_real]):
        #Importa cada módulo encontrado dinamicamente
        importlib.import_module(f"{caminho_pacote}.{module_name}")
    
    # Retorna todas as subclasses da classe base que agora estão na memória
    return PerfilDeScanBase.__subclasses__()

async def main():
    print("--- Ferramenta de Scan com BBOT (Versão Modular) ---")
    
    # Carrega dinamicamente todos os perfis da pasta 'profiles'
    perfis_disponiveis = descobrir_e_carregar_perfis('profiles')
    
    if not perfis_disponiveis:
        print("ERRO: Nenhum perfil de scan foi encontrado na pasta 'profiles'.")
        return

    print("\nEscolha um perfil de scan:")
    for i, perfil in enumerate(perfis_disponiveis):
        print(f"  {i + 1}. {perfil.name} - {perfil.description}")

    try:
        escolha = int(input("\nDigite o número do perfil desejado: "))
        if not (1 <= escolha <= len(perfis_disponiveis)):
            raise ValueError
        perfil_escolhido = perfis_disponiveis[escolha - 1]
    except ValueError:
        print("ERRO: Escolha inválida.")
        return

    alvos_input = input("Digite o(s) alvo(s), separados por vírgula: ")
    alvos = [alvo.strip() for alvo in alvos_input.split(',')]

    output_filename = input("Digite o nome do arquivo (sem especificar o tipo): ")

    scan_obj = perfil_escolhido(targets=alvos, output_filename=output_filename)
    await scan_obj.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScan interrompido pelo usuário.")
# BBOT_Automation
Automatização do uso do BigHuge Black lantern security OSINT Tool.
O objetivo desse código é automatizar o uso do BBOT, sem mais uso de comandos gigantescos, tudo que você precisa fazer é escolher o tipo de scan que quer rodar, o alvo e o nome do arquivo, PUM!
Foram criados vários tipos de perfis de scan para diferentes propósitos:
1. scan_dataleak_treatment: Scan de exploração de bases de dados buscando vazamentos de senhas. (output tratado com pandas)
2. scan_domain_treatment: Scan de exploração profunda de domínios. (output tratado com pandas)
3. scan_vuln_treatment: Scan de exploração de domínios em busca de vulnerabilidades. (output tratado com pandas)

É possível criar ou modificar os perfis na pasta "profiles".

Adicione sua própria pasta destino para armazenar os resultados dos scans, que vêm em .xlsx e .json, no arquivo scan_base.py.

!Os outputs continuam sendo salvos na pasta padrão do BBOT!

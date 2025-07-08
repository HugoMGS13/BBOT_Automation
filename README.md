# BBOT_Automation
Automatização do uso do BigHuge Black lantern security OSINT Tool.
Foram criados vários tipos de perfis de scan para diferentes propósitos:
1. scan_dataleak_treatment: Scan de exploração de bases de dados buscando vazamentos de senhas. (output tratado com pandas)
2. scan_domain_treatment: Scan de exploração profunda de domínios. (output tratado com pandas)
3. scan_vuln_treatment: Scan de exploração de domínios em busca de vulnerabilidades. (output tratado com pandas)

É possível criar ou modificar os perfis na pasta "profiles".

Adicione sua própria pasta destino para armazenar os resultados dos scans, que vêm em .xlsx, no arquivo scan_base.py.

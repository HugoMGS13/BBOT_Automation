from scan_base import PerfilDeScanBase

class PerfilDataLeak(PerfilDeScanBase):
    name = "scan_dataleak_treatment"
    description = "Scan de exploração de bases de dados buscando de vazamentos de senhas"
    presets = ['subdomain-enum','spider']
    modules = ["baddns","shodan_idb","shodan_dns",'pgp']
    config = {'allow_deadly': True}
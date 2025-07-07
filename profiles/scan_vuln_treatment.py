from scan_base import PerfilDeScanBase

class PerfilVuln(PerfilDeScanBase):
    name = "scan_vuln_treatment"
    description = "Scan de exploração de domínios em busca de vulnerabilidades"
    modules = ["baddns","shodan_idb","nuclei",'pgp']
    config = {'allow_deadly': True}
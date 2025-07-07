from scan_base import PerfilDeScanBase

class PerfilDomain(PerfilDeScanBase):
    name = "scan_domain_treatment"
    description = "Scan de exploração de domínios"
    presets = ['subdomain-enum','spider']
    modules = ["baddns","shodan_idb","shodan_dns",'pgp']
    config = {'allow_deadly': True}
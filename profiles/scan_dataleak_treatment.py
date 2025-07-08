from scan_base import PerfilDeScanBase

class PerfilDataLeak(PerfilDeScanBase):
    name = "scan_dataleak_treatment"
    description = "Scan de exploração de bases de dados buscando vazamentos de senhas"
    modules = ["baddns","dehashed",'pgp']
    config = {
        "modules": {
            "dehashed": {
                "api_key": "1SS44Jqy/hZD5IfQgDZ9HX4VkCJiM3f2b/QUt6xFreRN2LHNmpVGOMs="
            }
        }
    }

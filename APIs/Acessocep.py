import requests


class Acessocep:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def __str__(self):
        return self.format()

    def acessar_url(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados['ddd'],
            dados['localidade'],
            dados['uf']
        )

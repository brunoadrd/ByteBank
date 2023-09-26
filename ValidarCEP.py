import requests

class BuscarEndereco:
    def __init__(self, cep):
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido.')
        
    def validar_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def formatar_cep(self):
        return f'{self.cep[:2]}.{self.cep[2:5]}-{self.cep[5:]}'
    
    def acessar_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        dados_json = requests.get(url).json()
        return (
            dados_json['bairro'],
            dados_json['localidade'],
            dados_json['uf']
        )

    def __str__(self):
        return self.formatar_cep()
from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:
    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de caracteres inválido.')

class DocCpf:
    validador = CPF()

    def __init__(self, documento):
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido.')

    def validar(self, documento):
        return DocCpf.validador.validate(documento)
        
    def formatar(self):
        return DocCpf.validador.mask(self.cpf)

    def __str__(self):
        return self.formatar()
        
class DocCnpj:
    validador = CNPJ()

    def __init__(self, documento):
        if self.validar(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido.')
    
    def validar(self, documento):
        return DocCnpj.validador.validate(documento)
        
    def formatar(self):
        return DocCnpj.validador.mask(self.cnpj)

    def __str__(self):
        return self.formatar()
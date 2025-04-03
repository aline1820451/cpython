import json

class OficinaMecanica:
    def __init__(self):
        self.clientes = {}
        self.carregar_dados()
    
    def salvar_dados(self):
        with open("clientes.json", "w") as arquivo:
            json.dump(self.clientes, arquivo, indent=4)
    
    def carregar_dados(self):
        try:
            with open("clientes.json", "r") as arquivo:
                self.clientes = json.load(arquivo)
        except FileNotFoundError:
            self.clientes = {}
    
    def cadastrar_cliente(self, cpf, nome, telefone, endereco, placa, modelo, km, data, servico, orcamento):
        self.clientes[cpf] = {
            "dados_pessoais": {
                "nome": nome,
                "telefone": telefone,
                "endereco": endereco
            },
            "dados_veiculo": {
                "placa": placa,
                "modelo": modelo,
                "km": km
            },
            "ultimo_servico": {
                "data": data,
                "servico_realizado": servico,
                "orcamento": orcamento
            }
        }
        self.salvar_dados()
    
    def buscar_cliente(self, cpf):
        return self.clientes.get(cpf, "Cliente não encontrado.")
    
    def listar_clientes(self):
        return self.clientes
    
    def editar_cliente(self, cpf, nome=None, telefone=None, endereco=None, placa=None, modelo=None, km=None, data=None, servico=None, orcamento=None):
        if cpf in self.clientes:
            if nome:
                self.clientes[cpf]["dados_pessoais"]["nome"] = nome
            if telefone:
                self.clientes[cpf]["dados_pessoais"]["telefone"] = telefone
            if endereco:
                self.clientes[cpf]["dados_pessoais"]["endereco"] = endereco
            if placa:
                self.clientes[cpf]["dados_veiculo"]["placa"] = placa
            if modelo:
                self.clientes[cpf]["dados_veiculo"]["modelo"] = modelo
            if km:
                self.clientes[cpf]["dados_veiculo"]["km"] = km
            if data:
                self.clientes[cpf]["ultimo_servico"]["data"] = data
            if servico:
                self.clientes[cpf]["ultimo_servico"]["servico_realizado"] = servico
            if orcamento:
                self.clientes[cpf]["ultimo_servico"]["orcamento"] = orcamento
            self.salvar_dados()
            return "Cliente atualizado com sucesso."
        return "Cliente não encontrado."
    
    def remover_cliente(self, cpf):
        if cpf in self.clientes:
            del self.clientes[cpf]
            self.salvar_dados()
            return "Cliente removido com sucesso."
        return "Cliente não encontrado."

# Exemplo de uso
oficina = OficinaMecanica()
oficina.cadastrar_cliente("12345678900", "João Silva", "11999999999", "Rua A, 123", "ABC-1234", "Gol", "150000", "01/04/2025", "Troca de óleo", "R$ 150,00")
print(oficina.buscar_cliente("12345678900"))
oficina.editar_cliente("12345678900", telefone="11988888888")
print(oficina.buscar_cliente("12345678900"))
oficina.remover_cliente("12345678900")
print(oficina.buscar_cliente("12345678900"))

class MaterialConstrucao:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    def calcular_custo_total(self):
        return self.preco_unitario * self.quantidade


if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Cálculo de Custos de Materiais de Construção")

    # Coleta de informações do usuário
    nome_material = input("Informe o nome do material de construção: ")
    preco_unitario = float(input("Informe o preço unitário do material: "))
    quantidade = int(input("Informe a quantidade necessária: "))

    # Criação de uma instância do material de construção
    material = MaterialConstrucao(nome_material, preco_unitario, quantidade)

    # Calcula o custo total
    custo_total = material.calcular_custo_total()

    # Exibe o resultado
    print(f"O custo total do material {
          material.nome} é de R$ {custo_total: .2f}")

#Alunos:
#Lucas da Silva Duarte
#Claudenilson da Silva Clemente
#Sandro Marcelo Fernandes Monteiro

class Produto:
  imposto = 0.15
  lista_produtos = []

  @staticmethod
  def listar_tudo():
    for i in Produto.lista_produtos:
      print('nome: ', i['nome'], ', valor: ', i['valor'], ', quantidade: ', i['qt'], ', valor total: ', float("{:.2f}".format(i['valor']*i['qt'])))

  @staticmethod
  def calc_imposto(x):
    return float("{:.2f}".format(x*(Produto.imposto + 1)))

  def __init__(self):
    i = 0
    while i == 0:
      try:
        self.nome = input('Digite o nome do produto: ')
        self.valor = Produto.calc_imposto(float(input('Digite o valor do produto: ')))
        self.qt = int(input('Digite a quantidade do produto: '))
        i = 1
        self.lista_produtos.append({"nome": self.nome, "valor": self.valor, "qt": self.qt})
      except ValueError:
        print("Entrada(s) inválida(s). Digite outra vez.")
        print('CADASTRO DE PRODUTOS')
def interface(mensagem):
  x = input(mensagem)
  while (x.lower() != 's') and (x.lower() != 'n'):
    print('Entrada inválida.')
    x = input(mensagem)
  return x.lower()

x = interface('Você deseja cadastrar um novo produto? S/N ')

if x == 'n':
  print('Fim.')
else:
  while x == 's':
    produto = Produto()
    x = interface('Você deseja cadastrar um novo produto? S/N ')

  y = interface('Você deseja listar os produtos cadastrados? S/N ')
  if y == 's':
    Produto.listar_tudo()
  else:
    print('Fim.')
def ler_arquivo(teste.txt):
  """
  Esta função abre um arquivo para leitura e retorna seu conteúdo.
  """
  try:
    with open(nome_do_arquivo, "r") as arquivo:
      conteudo = arquivo.read()
      return conteudo
  except FileNotFoundError:
    return "Arquivo não encontrado."

# Para usar a função:
nome_do_arquivo = "meu_arquivo.txt"
conteudo = ler_arquivo(nome_do_arquivo)
print(conteudo)
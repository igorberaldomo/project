Esse código pega dados da banco de dados banco_dados usando flask, trata a id e manda para o navegador

para ver os dados no back-end use abra o terminal e digite:
python3 projeto.py (linux)
py .\projeto.py(windows)

abra o navegador e vá para o endereço:
para ver todas as cores http://localhost:5000/cores 
para buscar determinada cor vá para http://localhost:5000/cores/?id=1

para ver a execução do aplicativo http://localhost:8501

O aplicativo consiste em uma lista com um exemplo de 3 corres.
ele tem 3 caixas de texto para input e 3 botões:

o botão 'cadastrar' vai gerar o próximo id por ordem numérico e vai pegar o nome e o rgb dos inputs e vai por comando POST envia-lo para o back-end, a seguir ele vai atualizar o front-end

o botão 'Listar uma cor' vai pegar o Id do input e vai verifica-lo se ele existe, se ele existir ele vai ser mostrado abaixo dos botões

o botão 'deletar uma cor' vai pegar o Id do input verificar se ele existe, remover essa cor
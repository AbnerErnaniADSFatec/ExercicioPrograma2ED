#Definindo as funções e importando as bibliotecas
from itertools import cycle

def lista_vazia(lista):
      return len(lista) == 0

def getIndexLast(lista):
      return len(lista) - 1

def getFirst(lista):
      return lista[0]

def getLast(lista):
      return lista[getIndexLast(lista)]

def distintos(lista):
      return len(lista) == len(set(lista))

#Escolha do teste
num_teste = str(input('\nQual o número do teste (1, 2, 3): '))
print('\n', end = '')

#Abrindo as listas com as damas e os cavalheiros
list_damas = open('damas.txt', 'r').read().split('\n')
list_cavalheiros = open('cavalheiros.txt', 'r').read().split('\n')

#===================================== Verificando os Casamentos =====================================
dado = open('casamento_test' + num_teste + '.txt', 'r').read().split('\n')

#Analisando as preferencias das damas
preferencias = {}
for i in range(len(dado)):
   cavalheiros = dado[i].split(' ')
   dama = getFirst(cavalheiros)
   if len(cavalheiros) == 1:
      preferencias[dama] = ['sem preferencia']
   else:
      cavalheiros.remove(dama)
      preferencias[dama] = cavalheiros

#Verificando se todas tem preferencia ou não
todas_sem_preferencia = True
for dama in list_damas:
   if getFirst(preferencias[dama]) == 'sem preferencia':
      todas_sem_preferencia = todas_sem_preferencia and True
   else:
      todas_sem_preferencia = todas_sem_preferencia and False

#Casando as damas, mas algumas podem ficar encalhadas
casamentos_feitos = {}
cavalheiros_sem_casar = open('cavalheiros.txt', 'r').read().split('\n')
for dama in list_damas:
   cavalheiros_para_casar = []
   if todas_sem_preferencia:
      cavalheiros_para_casar = cavalheiros_sem_casar
   else:
      cavalheiros_para_casar = preferencias[dama]
   for cavalheiro in cavalheiros_para_casar:
      if cavalheiro in cavalheiros_sem_casar:
         cavalheiros_sem_casar.remove(cavalheiro)
         casamentos_feitos[dama] = cavalheiro
         break
      else:
         casamentos_feitos[dama] = 'encalhada'
         continue

#Verificando se todas conseguiram casar
casamento_OK = True
for dama in list_damas:
   if casamentos_feitos[dama] == 'encalhada':
      casamento_OK = casamento_OK and False
   else:
      casamento_OK = casamento_OK and True

#Exibindo o resultado na tela
print("Quanto aos casamentos: \n")
if casamento_OK:
   print(' Sim é possível casar todas as damas\n')
   print('   Os possíveis casamentos são: \n')
   for dama in list_damas:
      if todas_sem_preferencia:
         print('       ', dama,'com', casamentos_feitos[dama], ', sem preferências')
      else:
         print('       ', dama,'com', casamentos_feitos[dama])
   print('\n')
   print('Os seguintes cavalheiros não conseguiram casar: ')
   for cavalheiro in cavalheiros_sem_casar:
      print(cavalheiro, end = ' ')
else:
   print(' Não é possível casar todas as damas\n')
   print('   Porque \n')
   damas_sem_preferencia = []
   damas_casadas = []
   damas_encalhadas = []
   for dama in list_damas:
      if preferencias[dama][0] == 'sem preferencia':
         damas_sem_preferencia.append(dama)
      elif casamentos_feitos[dama] != 'encalhada':
         damas_casadas.append(dama)
      else:
         damas_encalhadas.append(dama)
   if not lista_vazia(damas_sem_preferencia):
      for dama in damas_sem_preferencia:
         print('       As preferências da', dama, 'são insuficientes')
   if not lista_vazia(damas_casadas):
      for dama in damas_casadas:
         print('       Apenas a', dama, 'conseguiu casar com', casamentos_feitos[dama])
   if not lista_vazia(damas_encalhadas):
      for dama in damas_encalhadas:
         print('       A', dama, 'não conseguiu casar')
print('\n\n')

#===================================== Verificando se todos os cavalheiros podem sentar na mesa =====================================
dado = open('cavalheiros_test' + num_teste + '.txt', 'r').read().split('\n')

#Analisando as amizades dos cavalheiros
amizades = {}
for i in range(len(dado)):
   amigos = dado[i].split(' ')
   cavalheiro = getFirst(amigos)
   if len(amigos) == 1:
      amizades[cavalheiro] = ['sem amigos']
   else:
      amigos.remove(getFirst(amigos))
      amizades[cavalheiro] = amigos

#Verificando se todos tem amigos ou não
todos_sem_amigos = True
for cavalheiro in list_cavalheiros:
   if getFirst(amizades[cavalheiro]) == 'sem amigos':
      todos_sem_amigos = todos_sem_amigos and True
   else:
      todos_sem_amigos = todos_sem_amigos and False

#Organizando a mesa de acordo com as amizades e verificando se todos sentaram
#Usando uma lista circular para verificar a disposição final da mesa
todos_sentados = None
if todos_sem_amigos:
      todos_sentados = False
else:
      todas_as_combinacoes = []
      primeiro = getFirst(list_cavalheiros)
      for a in amizades[primeiro]:
         for b in amizades[a]:
            for c in amizades[b]:
               for d in amizades[c]:
                  for e in amizades[d]:
                     for f in amizades[e]:
                           if distintos([primeiro,a,b,c,d,e,f]):
                              todas_as_combinacoes.append([primeiro,a,b,c,d,e,f])
      for combinacao in todas_as_combinacoes:
            mesa = cycle(combinacao)
            mesa_pronta = []
            todos_sentados = True
            for cavalheiro in mesa:
                  if len(mesa_pronta) == 8:
                        break
                  if cavalheiro in amizades[next(mesa)]:
                        todos_sentados = todos_sentados and True
                        mesa_pronta.append(cavalheiro)
                  else:
                        todos_sentados = todos_sentados and False
                        break
            if todos_sentados:
                  mesa_pronta = mesa
                  break

#Exibindo resultado na tela
print("Enquanto isso na távola redonda: ")
if todos_sentados:
      print("\n  Todos os cavalheiros conseguiram sentar!!!\n")
      cadeira = 0
      for cavalheiro in mesa_pronta:
            if cadeira == 7:
                  break
            print("    ",cavalheiro, "senta ao lado de ", next(mesa_pronta),", pois são amigos")
            cadeira = cadeira + 1
elif todos_sem_amigos:
      print("\n    Impossível arrumar a mesa, pois nenhum dos cavalheiros tem amigos !!!\n\n")
else:
      print("\n    Alguns cavalheiros não conseguiram sentar !!!\n\n")

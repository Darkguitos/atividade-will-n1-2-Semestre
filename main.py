class no:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class listaduplamenteligada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        if self.inicio is None:
            print("lista vazia.")
            return

        atual = self.inicio
        valores = []
        
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo

        print(" <-> ".join(valores))

    def inserir_final(self, valor):
        novo = no(valor)
        
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            return

        novo.anterior = self.fim
        self.fim.proximo = novo
        self.fim = novo

    def inserir_inicio(self, valor):
        novo = no(valor)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            return

        novo.proximo = self.inicio
        self.inicio.anterior = novo
        self.inicio = novo
    
    def inserir_meio(self, valor, posicao):
        if posicao <= 0 or self.inicio is None:
            self.inserir_inicio(valor)
            return

        atual = self.inicio
        indice = 0
        #quer dizer que enquanto o atual nao for nulo e o indice for menor que a posicao, ele vai percorrer a lista ate chegar na posicao que ele quer
        while atual is not None and indice < posicao:
            atual = atual.proximo
            indice += 1 

        if atual is None:
            self.inserir_final(valor)
            return
        #essa parte abaixo faz o nos se ligarem, o proximo do anterior vai ser o novo e o proximo do novo vai ser o atual(nao pensa muito nisso, vai enquentar cabeça atoa)
        novo = no(valor)
        anterior = atual.anterior
        novo.anterior = anterior
        novo.proximo = atual
        anterior.proximo = novo
        atual.anterior = novo

    def remover_inicio(self):
        if self.inicio is None:
            print("nao da pra remover ta vazio.")
            return

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
            return

        self.inicio = self.inicio.proximo
        self.inicio.anterior = None
    #aqui é a parte que remove o ultimo elemento da lista, o fim da lista
    def remover_final(self):
        if self.fim is None:
            print("nao da pra remover ta vazio.")
            return
        
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
            return

        self.fim = self.fim.anterior
        self.fim.proximo = None


if __name__ == "__main__":
    lista = listaduplamenteligada()

    lista.inserir_final(10)
    lista.inserir_final(20)
    lista.inserir_final(30)
    lista.imprimir() #essa parte tem que ficar vazia pois vai ser inserida nela os valores 10, 20 e 30

    lista.inserir_inicio(5)
    lista.imprimir()  

    lista.inserir_meio(15, 2)
    lista.imprimir()  

    lista.remover_inicio()
    lista.imprimir()   

    lista.imprimir()  
    lista.remover_final()
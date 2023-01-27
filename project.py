class Fila:
    ''' Para implementar uma fila, podemos usar duas listas: uma para armazenar os itens e 
        outra como uma "ponteiro" para o próximo item a ser removido. 
        A classe teria métodos para adicionar e remover itens, além de um método 
        para verificar se a fila está vazia.
    '''
    def __init__(self):
        self.itens = []
        self.ponteiro = 0
        
    def adicionar(self, item):
        self.itens.append(item)
        
    def remover(self):
        if self.ponteiro >= len(self.itens):
            raise ValueError("A fila está vazia.")
        item = self.itens[self.ponteiro]
        self.ponteiro += 1
        return item
    
    def vazia(self):
        return self.ponteiro == len(self.itens)


class Pilha:
    '''
        Para implementar uma pilha, podemos usar uma lista e adicionar e 
        remover itens usando o método append() e pop(), 
        respectivamente. A classe teria também um método para verificar 
        se a pilha está vazia.
    '''
    def __init__(self):
        self.itens = []
        
    def adicionar(self, item):
        self.itens.append(item)
        
    def remover(self):
        if self.vazia():
            raise ValueError("A pilha está vazia.")
        return self.itens.pop()
    
    def vazia(self):
        return len(self.itens) == 0

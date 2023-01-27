# TESTE PROJECT

# Desenolvi o projeto de test sobre Fila e Pilha, deixei comentado os códigos com método


# TEST STACK - UNITTEST
- **A classe possui os seguintes métodos:**
- O método init() é o construtor da classe, ele é chamado quando uma nova instância da classe é criada. Ele inicializa o atributo "items" como uma lista vazia.
- O método str() é chamado quando é necessário converter uma instância da classe para uma string. Ele retorna uma string vazia se a pilha estiver vazia ou uma string composta pela representação dos itens na pilha, separados por " -> ". Ele também inverte a ordem dos itens da pilha, para que o item do topo da pilha esteja na primeira posição.
- O método push() adiciona um item na pilha. Ele simplesmente adiciona o item dado na lista "items".
- O método pop() remove o último item adicionado na pilha. Ele remove o item do final da lista "items" e o retorna. Se a pilha estiver vazia, ele lança uma exceção do tipo StackPopException.
- O método is_empty() retorna verdadeiro se a pilha estiver vazia e falso caso contrário.
- O método len() retorna o número de itens na pilha.
- O método add() é um alias para o método push().
- A classe StackPopException é uma subclasse de Exception e é utilizada para indicar que um erro ocorreu ao tentar remover um item de uma pilha vazia.

# TEST STACK (PILHA) - UNITTEST
- *Na classe Queue, temos alguns métodos:**
- O método init() inicializa uma fila vazia.
- O método str() retorna uma string representando a fila, com os elementos separados por " -> ". Se a fila estiver vazia, retorna uma string vazia.
- O método enqueue() adiciona um elemento na fila.
- O método dequeue() remove e retorna o elemento que está no início da fila. Se a fila estiver vazia, é lançada uma exceção QueueUnderflowException.
- O método is_empty() retorna True se a fila estiver vazia e False caso contrário.
- O método len() retorna o número de elementos na fila.
- Além disso, temos uma classe QueueUnderflowException que é uma subclasse de Exception, e pode ser usada para tratar erros de underflow(tentar retirar elementos de uma lista vazia) na fila


# TEST PROJETO ADICIONAL - PYTEST
## Fila
Para implementar uma fila, podemos usar duas listas: uma para armazenar os itens e 
outra como uma "ponteiro" para o próximo item a ser removido. 
A classe teria métodos para adicionar e remover itens, além de um método 
para verificar se a fila está vazia.

## Pilha
Para implementar uma pilha, podemos usar uma lista e adicionar e 
remover itens usando o método append() e pop(), 
respectivamente. A classe teria também um método para verificar 
se a pilha está vazia.
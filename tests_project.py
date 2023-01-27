import pytest
from project import Fila, Pilha


""" pytest tests_project.py """

def test_fila_adicionar():
    fila = Fila()
    fila.adicionar(1)
    fila.adicionar(2)
    assert fila.itens == [1, 2]

def test_fila_remover():
    fila = Fila()
    fila.adicionar(1)
    fila.adicionar(2)
    assert fila.remover() == 1
    assert fila.remover() == 2
    with pytest.raises(ValueError):
        fila.remover()

def test_fila_vazia():
    fila = Fila()
    assert fila.vazia() == True
    fila.adicionar(1)
    assert fila.vazia() == False

def test_pilha_adicionar():
    fila = Fila()
    fila.adicionar(1)
    fila.adicionar(2)
    assert fila.itens == [1, 2]
    
def test_pilha_remover():
    fila = Fila()
    fila.adicionar(1)
    fila.adicionar(2)
    assert fila.remover() == 1
    assert fila.remover() == 2
    with pytest.raises(ValueError):
        fila.remover()

def test_pilha_vazia():
    fila = Fila()
    assert fila.vazia() == True
    fila.adicionar(1)
    assert fila.vazia() == False
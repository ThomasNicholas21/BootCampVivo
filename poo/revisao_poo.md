# Pragramação Orientada a Objetos (POO)
Paradigma de programação é um estilo de programação de como solucionar problemas através do código. O paradigma de programação orientada a objetos faz a estruturação do código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais flexível e modular.
- Classes
    - É o que define as características e comportamentos de um objeto, porém não é possível utilizar diretamente, ou seja, é algo abstrato.
- Objetos
    - O objeto instanciado por uma classe pode utilizar as características e comportamentos que foram definidos na clase.

Exemplo:
```python
class Calculadora:
    def somar(self, a, b):
        return a + b

calc = Calculadora()
resultado = calc.somar(3, 4)
print(resultado)  # 7
```
- [Mais exemplos](https://github.com/ThomasNicholas21/BootCampVivo/tree/master/poo/classes_objetos)
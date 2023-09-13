#Python va a buscar los metodos o propiedades buscando en los nodos padres derecho y si no encuentra nada busca en los nodos padres izquierdo
# Ejemplo D(A,F) => Primero busca en B, luego en A si no encuentra nada, busca por el lado izquierdo en C
#             A
#          B    C
#            D
class A:
    def hablar(self):
        print('Hola soy A')
class B(A):
    def hablar(self):
        print('Hola soy B')
class C(A):
    def hablar(self):
        print('Hola soy C')
class D(B,C):
    pass               
    
d = D()
B.hablar(d)    
         
        
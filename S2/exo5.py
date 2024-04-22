# Exercice 5: Générateurs
# Écrivez une fonction génératrice qui génère les termes de la suite de Fibonacci jusqu'à un certain nombre donné.



# générateur apl fonction 1 fois / plusieurs fois jusqu'à la conditon remplis
def foo(n):
    a, b = 0, 1

    for i in range(n):
            # yield est le mot clé du générateur 
            yield a
            a, b = b, a + b

            
           


ln = int(input('How long ?'))
print(list(foo(ln)))
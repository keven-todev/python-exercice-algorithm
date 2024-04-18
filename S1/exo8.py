# Liste des nombres premiers:
# Écrivez un programme qui génère une liste des nombres premiers jusqu'à un certain nombre donné.

limite = int(input("Entrez une limite : "))
nombres_premiers = [num for num in range(2, limite+1) if all(num % i != 0 for i in range(2, int(num**0.5)+1))]
print("Nombres premiers jusqu'à", limite, ":", nombres_premiers)

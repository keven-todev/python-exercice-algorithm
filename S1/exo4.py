# Conversion de température:
# Écrivez un programme qui convertit une température donnée en degrés Celsius en degrés Fahrenheit.

question = input('Quelle température fait il ? ')
conversion = float(question) 
calcul = (conversion * 9/5) + 32
print(calcul)
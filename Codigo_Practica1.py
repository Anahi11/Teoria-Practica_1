import math

# Ingresar el titulo.txt del libro
print("Ingresa el libro en formato .txt")
txt = input()

# Se abre el archivo txt y se asigna a la variable libro; con la variable "texto" se leen los caracteres del libro
# y se cambian mayusculas a minusculas y se quitan acentos.
with open(txt, encoding="utf-8") as libro:
    texto = libro.read().lower().replace("á", "a").replace("é", "e").replace('í', 'i').replace('ó', 'o').replace('ú', 'u') \
        .replace('ö', 'o').replace('ë', 'e').replace('ï', 'i').replace('ü', 'u').replace('à', 'a').replace('è', 'e')\
        .replace('ù', 'u').replace('ç', 'c').replace('â', 'a').replace('ê', 'e').replace('î', 'i').replace('ô', 'o').replace('û', 'u')

    # se pide la letra a buscar en minuscula o mayuscula.
    letra = input('Ingresa la letra que te gustaria contar: ').lower()

    # se crea el alfabeto en donde solo estaran los caracteres que nos interesan
    alfabeto = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']

    # se itera y compara el alfabeto con los caracteres del texto y esa es la cantidad total de caracteres en el archivo
    ca_esp = 0
    for a in alfabeto:
        for i in texto:
            if i == a:
                ca_esp += 1

# aqui se guarda el numero total de la letra solicitada
letrastexto = texto.count(letra)

# Si la letra de interes no se encuentra en el texto, imprime el mensaje; en caso de que exista calculara la probabilidad, información de cada letra
if letrastexto == 0:
    print('No existe la letra o combinación en el texto: \n ')
else:
    prob_letra = letrastexto / ca_esp
    informacion = math.log((1 / prob_letra),2)

    # Impresion en pantalla de los valores obtenidos
    print("LETRA DE INTERES: \n")
    print("El total de '", letra, "' en el texto: ", letrastexto)
    print("El total de caracteres: ", ca_esp)
    print(f"La probabilidad de la(s) letra(s) es P(Xj): {prob_letra:.4f} %")
    print(f"La información de la(s) letra(s) es: {informacion:.4f}")


print("TODAS LAS LETRAS DEL ABECEDARIO EN EL TEXTO \n ")
Entropia_Total = 0
for a in alfabeto:
    LetraConteo = texto.count(a)
    if LetraConteo == 0:
        print('No existe la combinación en el texto: ',a,"\n")
    else:
        probabilidad_caracter = LetraConteo / ca_esp
        informacion_caracter = math.log((1/probabilidad_caracter),2)
        entropia = probabilidad_caracter * informacion_caracter
        Entropia_Total = Entropia_Total + entropia
        # Impresion en pantalla de los valores obtenidos
        print("El total de '", a, "' en el texto: ", LetraConteo)
        print("El total de caracteres: ", ca_esp)
        print(f"La probabilidad de la(s) letra(s) es P(Xj): {probabilidad_caracter:.4f} %")
        print(f"La información de la(s) letra(s) es: {informacion_caracter:.4f} \n")

print("Entropia Total")
print(f"La entropía H(x) = {Entropia_Total:.4f} ")
print(f"Entropia de segundo orden: {(Entropia_Total * 2):.4f} ")
print(f"Entropia de tercer orden: {(Entropia_Total * 3):.4f} \n")

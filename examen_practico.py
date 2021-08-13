# Importamos las librerías:
import json

# Abrir archivo Json
tweet_json = open('tweets_test.json', 'r').read()
tweet = json.loads(tweet_json)

# Métrica 1: Número de tweets.
print('El número de tweets es', len(tweet))
print()

# Métrica 2: Lista de usuarios autores de los tweets.
print("Los usuarios autores de los tweets son:")
print()
for i in tweet:
    usuario = tweet[i]["user"]
    nombre = usuario["screen_name"]
    
    print(i , "->", nombre)

print()

# Métrica 3: Totalizador del número de seguidores de todos los usuarios

lista =[]
for i in tweet:
    usuario = tweet[i]["user"]
    numero_seguidores = usuario["followers_count"]
    lista.append(numero_seguidores)
    
totalizador = 0
for suma in lista:
    totalizador += suma

print("El total del número de seguidores de todos los usuarios es: ", totalizador)

print()

# Métrica 4: Lista de todos los usuarios mencionados en todos los tweets:
print("Lista de los usuarios mencionados en todos los tweets:")
print()
for t in tweet:
    entities= tweet[t]["real_entities"]
    mentions = entities["user_mentions"]
    for x in mentions:
        nombre_mencion = x["screen_name"]
        print(nombre_mencion)

print()

# Métrica 5: Total de tweets con tendencia 0,1 y 2 respectivamente

lista_tendencia = []
for w in tweet:
    tendencia = tweet[w]["tendencia"]
    lista_tendencia.append(tendencia)
    #print(lista_tendencia)

tendencia_0 = lista_tendencia.count("0")
tendencia_1 = lista_tendencia.count("1")
tendencia_2 = lista_tendencia.count("2")

print("El total de tweets con tendencia 0 es: ", tendencia_0)
print()
print("El total de tweets con tendencia 1 es: ", tendencia_1)
print()
print("El total de tweets con tendencia 2 es: ", tendencia_2)





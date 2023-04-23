text = """Este capítulo presenta la clase de lenguajes conocidos como lenguajes regulares.Estos lenguajes son aquellos que pueden describirse mediante un autómata finito,los cuales hemos descrito brevemente en la Sección 111.Después de ver un ejemplo que proporcionará la motivación necesaria para continuar con este estudio, definiremos formalmente los autómatas finitos.
Como hemos mencionado anteriormente,un autómata finito tiene un conjunto de estados y su control pasa de un estado a otro en respuesta a las entradas externas.Una de las diferencias fundamentales entre las clases de autómatas finitos es si dicho control es determinista, lo que quiere decir que el autómata no puede encontrarse en más de un estado a un mismo tiempo,o no determinista, lo que significa que sí puede estar en varios estados a la vez. Comprobaremos que añadir el no determinismo no nos permite definir ningún lenguaje que no pueda ser definido mediante un autómata finito determinista, aunque se obtiene una eficacia sustancial al describir una aplicación utilizando un autómata no determinista. En efecto,el no determinismo nos permite
programar soluciones para los problemas utilizando un lenguaje de alto nivel. Entonces el autómata finito no determinista se compila mediante un algoritmo que vamos a ver en este capítulo, en un autómata determinista que puede ejecutarse en una computadora convencional.
Concluiremos este capítulo con el estudio de un autómata no determinista extendido que dispone de la opción adicional de hacer una transición de un estado a otro de forma espontánea, es decir, de aceptar la cadena vacía como entrada. Estos autómatas también aceptan los lenguajes regulares. Sin embargo, esto adquirirá importancia en el Capítulo 3, donde estudiaremos las expresiones regulares y su equivalencia con los autómatas.
El estudio de los lenguajes regulares continúa en el Capítulo 3,en el que presentaremos otra forma de describirlos: la notación algebraica conocida como expresiones regulares. Después de estudiar las expresiones regulares y demostrar su equivalencia con los autómatas finitos, emplearemos tanto los autómatas como las expresiones regulares como herramientas en el Capítulo 4 para demostrar algunas propiedades importantes de
los lenguajes regulares. Algunos ejemplos de estas propiedades son las propiedades de clausura, que permiten asegurar que un lenguaje es regular porque se sabe que uno o más lenguajes son regulares, y las propiedades de decisión. Éstas son algoritmos que permiten responder preguntas acerca de los autómatas o de las expresiones regulares, como por ejemplo, si dos autómatas o expresiones representan el mismo lenguaje."""

divisor = text.split()
count = len(divisor)
dictionary = {}

for word in divisor:
    if word in divisor:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(dictionary)

repeat_word = max(dictionary)
print(dictionary)




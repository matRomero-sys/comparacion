nombre = input("escriba su nombre: ")
saludador = f"hola {nombre}, ¡que alegria que estes por aquí!"
print(saludador) 

import random

chistes = [
    "¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 == DEC 25.",
    "¿Qué le dice un bit al otro? Nos vemos en el bus.",
    "¿Cómo se llama el campeón de buceo japonés? Tokofondo.",
    "¿Y el subcampeón? Kasitoko.",
    "—Camarero, ese filete tiene muchos nervios. —Pues normal, es la primera vez que se lo comen.",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Por qué está feliz la escoba? Porque ba-rriendo.",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Qué le dice un jardinero a otro? ¡Disfrutemos mientras podamos!",
    "¿Qué hace una computadora cuando tiene frío?¡Se pone un Windows!"
]

print("🤖 Bienvenido al contador de chistes!")
print("Presiona Enter para que te cuente un chiste o escribe 'salir' para terminar.")

while True:
    entrada = input("👉 ")
    if entrada.lower() == 'salir':
        print("Hasta luego 😄")
        break
    else:
        print("😂", random.choice(chistes))

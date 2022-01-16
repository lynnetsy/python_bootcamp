#Vamos a encriptar un string que introduzcamos utilizando SHIFT como el numero de casillas
#Que nuestras letras se van a modificar para mostrar algo que no pueda entender otra persona
#"ENCRYPT ES PARA DESPLAZAR HACIA ATRAS Y ENCODE HACIA ADELANTE"

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","t","s","u","v","w","x","y","z"]
direction = input("Encrypt or Encode\n").lower()
shifts = int(input("# of shifts\n"))
word = list(input("Word to encrypt or decode\n"))
word_as_arr=list(word)
i = 0
indices = []
nuevo_mensaje = []
for letter in word:
    index_letters = alphabet.index( word_as_arr[i])
    i+=1
    indices.append(index_letters)
    if direction == "encrypt":
        nuevo_mensaje.append(alphabet[index_letters - shifts])

    elif direction == "encode":
        nuevo_mensaje.append(alphabet[index_letters + shifts])

print(f"Este es el mensaje real: {word_as_arr}")
print(f"Estas son las posiciones que ocupan{indices}")
print(f"Este es el mensaje encriptado{nuevo_mensaje}")
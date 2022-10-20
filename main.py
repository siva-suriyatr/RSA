from generateKeys import generate_key_pair

def encrypt(pk, plaintext):
    
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    aux = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux] #int to string
    return ''.join(plain)


if __name__ == '__main__':
    
    p = int(input(" - Enter a prime number: "))
    q = int(input(" - Enter another unique prime number: "))

    public, private = generate_key_pair(p, q)

    print(" Public key - ", public, " Private key - ", private)

    message = input("Enter a string to be encrypted")
    encrypted_msg = encrypt(public, message)

    print(" - Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is - ", decrypt(private, encrypted_msg))

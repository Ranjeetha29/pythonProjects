#Encryption and decryption using ceaser cipher

print("****************************************************");print("✹✹✹ Ceaser Cipher✹✹✹".center(50));print("****************************************************")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt():
    message=input("Enter the message to encrypt: ").lower()
    key=int(input("Enter the key size : "))
    ciphertext=""
    for i in message:
        if i in letters:
            C=(letters.index(i)+key)%26
            ciphertext+=letters[C]
        else:
            ciphertext+=i
    print(f"The Encrypted text is {ciphertext}")

def decrypt():
    message=input("Enter the message to decrypt: ").lower()
    key=int(input("Enter the key size : "))
    plaintext=""
    for i in message:
        if i in letters:
            P=(letters.index(i)-key)%26
            plaintext+=letters[P]
        else:
            plaintext+=i
    print(f"The Decrypted text is {plaintext}")

choice="yes"
while choice!='No':
    process=input("Type 'Encrypt' for Encryption or 'Decrypt' for Decryption : ").capitalize()
    if process=='Encrypt':
        encrypt()
    elif process=='Decrypt':
        decrypt()
    else:
        print("Enter the valid operation")
    choice=input("Enter 'Yes' to continue or 'No' to Quit:").capitalize()

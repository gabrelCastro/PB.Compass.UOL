import hashlib

while(1):
    string = input("Digite uma string: ")

    sha1 = hashlib.sha1(string.encode())

    print(sha1.hexdigest())

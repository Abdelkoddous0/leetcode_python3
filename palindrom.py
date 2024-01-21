def palindrom(string):
    return string == string [::-1]

if __name__ == "__main__":
    string = input("string : ")
    print ("palindrom" if palindrom(string) else "n'est pas palindrom")

import os


f = open("myfile.txt", "r")
print(f.read())

f = open("myfile.txt", "r")
print(f.read())

f = open("myfile.txt", "r")
print(f.readline())
print(f.readline())

f = open("myfile.txt")
for x in f:
    print(x)

    f = open("myfile.txt", "r")
    print(f.readline())
    f.close()

f = open("myfile.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("myfile.txt", "r")
print(f.read())

f = open("myfile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())

f = open("myfile.txt", "w")
f = open("myfile.txt", "w")

# import os
# os.remove("D:\ESCRITORIO\compu lucho CARPETAS/myfile.txt")

if os.path.exists("myfile.txt"):
   # os.remove("myfile.txt")
    print("Se removio el archivo")
else:
    print("El archivo no existe")


    os.rmdir("D:\ESCRITORIO\compu lucho CARPETAS/Nueva carpeta")

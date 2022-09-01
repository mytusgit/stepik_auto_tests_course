import os

print("1.")
print(os.path.abspath(__file__))
print("2.")
print(os.path.abspath(os.path.dirname(__file__)))

# не забываем оставить пустую строку в конце файла

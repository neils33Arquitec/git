lenguajes = ["Python", "JavaScript", "Java", "C++", "Ruby"]
lenguajes.insert(3, "Go")  # Insertamos Go en la posición 3
print(lenguajes)  # ['Python', 'JavaScript', 'Java', 'Go', 'C++', 'Ruby']
lenguajes.insert(0, "C#")  # Insertamos C# al inicio de la lista
print(lenguajes)  # ['C#', 'Python', 'JavaScript', 'Java', 'Go', 'C++', 'Ruby']
lenguajes.remove("C++")  # Eliminamos C++ de la lista
print(lenguajes)    # ['C#', 'Python', 'JavaScript', 'Java', 'Go', 'Ruby']
lenguajes.append("Rust")  # Agregamos Rust al final de la lista
print(lenguajes)  # ['C#', 'Python', 'JavaScript', 'Java', 'Go', 'Ruby', 'Rust']

print(lenguajes.index("Go"))  # 4
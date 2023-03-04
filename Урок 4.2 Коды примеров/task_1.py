"""Простейший пример"""

new_obj = 5
print(new_obj)
a = new_obj
del new_obj
a = None
print(new_obj)  # -> NameError: name 'new_obj' is not defined

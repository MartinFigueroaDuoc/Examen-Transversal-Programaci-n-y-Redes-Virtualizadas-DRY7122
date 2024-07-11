from db_setup import add_user

# Agregar usuarios
if add_user('Martin', 'contraseña1'):
    print("Usuario 'Martin' agregado con éxito.")
else:
    print("El usuario 'Martin' ya existe.")

if add_user('Jose', 'contraseña2'):
    print("Usuario 'Jose' agregado con éxito.")
else:
    print("El usuario 'Jose' ya existe.")

if add_user('Vicente', 'contraseña2'):
    print("Usuario 'Vicente' agregado con éxito.")
else:
    print("El usuario 'Vicente' ya existe.")

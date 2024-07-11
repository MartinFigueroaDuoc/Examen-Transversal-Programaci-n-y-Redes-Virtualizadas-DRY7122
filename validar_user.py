from db_setup import get_db, hash_password

# Función para validar usuario
def validate_user(username, password):
    password_hash = hash_password(password)
    with get_db() as conn:
        cursor = conn.execute('SELECT * FROM users WHERE username = ? AND password_hash = ?', (username, password_hash))
        user = cursor.fetchone()
        return user is not None

# Validación de usuarios
if validate_user('Martin', 'contraseña1'):
    print("Usuario 'Martin' validado con éxito.")
else:
    print("Fallo en la validación del usuario 'Martin'.")

if validate_user('Jose', 'contraseña2'):
    print("Usuario 'Jose' validado con éxito.")
else:
    print("Fallo en la validación del usuario 'Jose'.")

if validate_user('Vicente', 'contraseña2'):
    print("Usuario 'Vicente' validado con éxito.")
else:
    print("Fallo en la validación del usuario 'Vicente'.")


# vlan.py

vlan_number = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan_number <= 1005:
    print(f"La VLAN {vlan_number} está en el rango normal.")
elif 1006 <= vlan_number <= 4094:
    print(f"La VLAN {vlan_number} está en el rango extendido.")
else:
    print("Número de VLAN fuera de rango.")


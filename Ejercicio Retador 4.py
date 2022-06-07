ID_Producto_Precio = [[1,"Maíz grano",285.55],[2,"Pepino",334.72],[3,"Tomate verde",129.00]]

ID_producto_vender = int(input("Ingrese el ID del producto a vender: "))
numero_cajas = int(input("Ingrese el numero de cajas a vender: "))

for producto in ID_Producto_Precio:
  if producto[0] == ID_producto_vender:
    print(f"El producto es: {producto[1]}")
    print(f"El precio del producto es: ${producto[2]}")
    
    subtotal = producto[2] * numero_cajas
    subtotal_str = str(subtotal) 
    print("El subtotal es: $" + subtotal_str)
    
    if numero_cajas <= 100:
      print("Su costo de envio es de $1500")
      subtotal_a_pagar = subtotal + 1500
      subtotal_a_pagar_str = str(subtotal_a_pagar)
      print("El costo total a pagar es de: $" + subtotal_a_pagar_str)
    else:
      print("¡Felicades! Su envio será gratis")
  #elif producto[0] != ID_producto_vender:
    #print("Este producto no está disponible")
  #else:
   # print("Este producto no está disponible")
#print("Fin de la sentencia if")

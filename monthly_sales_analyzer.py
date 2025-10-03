# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]
#función para calcular las ventas totales de un prodcuto específico#
def total_sales_by_product(data, product_key):
    #Agrego una variable para acumular las ventas#
    total = 0 
    
    #Recorro cada diccionario (día) dentro de la lista de datos#
    for day in data:
        #sumo la venta del producto específico usando su clave (product_key)
        total += day[product_key]

    #devolvemos el total acumulado#
    return total


#función para calcular el promedio de ventas diarias de un producto#
def average_daily_sales(data, product_key):
    #uso la función anterior para obtener el total#
    total = total_sales_by_product(data, product_key)

    #dividimos el total por la cantidad de días (20)#
    average = total / len(data)

    #Devuelvo el promedio#
    return average



#función para encontrar el día con la mayor suma de ventas totales#
def best_selling_day(data):
    #variable para encontrar el día con más ventas (se actualizará)
    best_day = None

    #variable para registrar la cantidad máxima encontrada hasta ahora#
    max_sales = 0 

    #recorremos cada día#
    for day in data:
        #sumamos las ventas de los tres productos en ese día#
        total = day["product_a"] + day["product_b"] + day["product_c"]

        #si la suma es mayor a la anterior máxima,  actualizamos#
        if total > max_sales:
            max_sales = total
            best_day = day      #guardo el día completo#

    #retornamos el diccionario del mejor día#
    return best_day
    
    
   
#función que cuenta cuantos días las ventas de un producto superan cierto umbral#
def days_above_threshold(data, product_key, threshold):
    #contador de días#
    count = 0
 
    #recorremos los datos#
    for day in data:
        #si las ventas del producto en ese día superan el umbral#
        if day[product_key] > threshold:
            count += 1      #aumentamos el contador#

    #retorno cuantos días cumplieron la condición#
    return count       

#función para encontrar cuál producto fue el más vendido en total#
def top_product(data):
    #calculo el total de cada producto usando la función que ya creamos#
    total_a = total_sales_by_product(data, "product_a")
    total_b = total_sales_by_product(data, "product_b")
    total_c = total_sales_by_product(data, "product_c")

    #comparamos los totales y retornamos el producto con mayor venta#
    if total_a > total_b and total_a > total_c:
        return "product_a"
    elif total_b > total_a and total_b > total_c:
        return "product_b"
    else:
        return "product_c"
    




# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))


#Día con peores ventas#
#función para encontrar el día con la menor suma de ventas totales#
def worst_selling_day(data):
    #guardo el peor día hasta ahora (actualización si se encuentra uno peor)
    worst_day = None

    #iniciamos con un número muy alto para que cualquier suma real sea menor#
    min_sales = float("inf")        #con inf comparo cualquier número real, así puedo actualizar el mínimo asegurándome de que cualquier venta total sea menor#

    #recorremos todos los días en la lista#
    for day in data:
        #sumo las ventas de los 3 productos de ese día#
        total = day["product_a"] + day["product_b"] + day["product_c"]

        #si esta  suma es menor a la mínima encontrada hasta ahora#
        if total < min_sales:
            min_sales = total   #guardo la mínima nueva#
            worst_day = day     #y el día correspondiente#

    #devuelvo el diccionario con los datos del peor día#
    return worst_day
        
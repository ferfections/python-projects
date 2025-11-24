import pandas as pd
import random

# --- 1. Definición de Productos por Categoría ---
# (Categorías originales)
fruits = ["apple", "banana", "grape", "orange", "strawberry", "blueberry"]
vegetables = ["potato", "onion", "carrot", "lettuce", "broccoli"]
canned_goods = ["canned tuna", "canned beans", "canned corn", "tomato soup", "canned peas"]
dairy = ["milk", "cheese", "yogurt", "butter", "eggs"]
meat = ["chicken breast", "ground beef", "pork chops", "sausages", "bacon"]
fish_seafood = ["salmon fillet", "shrimp", "cod", "mussels", "scallops"]

# (Nuevas categorías solicitadas)
deli = ["sliced ham", "sliced turkey", "salami", "provolone cheese", "potato salad"]
condiments = ["ketchup", "mustard", "mayonnaise", "hot sauce", "soy sauce", "olive oil"]
snacks = ["potato chips", "pretzels", "cookies", "crackers", "popcorn"]
bread_bakery = ["white bread", "wheat bread", "baguette", "bagels", "muffins"]
beverages = ["cola", "orange juice", "bottled water", "coffee", "tea", "beer"]
pasta_rice = ["spaghetti", "penne", "white rice", "brown rice", "quinoa"]
baking = ["all-purpose flour", "sugar", "baking soda", "chocolate chips", "vanilla extract"]
frozen_foods = ["frozen pizza", "ice cream", "frozen vegetables", "waffles", "fish sticks"]
personal_care = ["shampoo", "conditioner", "body soap", "toothpaste", "deodorant"]
health_care = ["band-aids", "pain reliever", "antiseptic wipes", "cough drops"]
cleaning_supplies = ["all-purpose cleaner", "dish soap", "laundry detergent", "paper towels"]
baby_items = ["diapers", "baby wipes", "baby formula", "baby food jars"]
pet_care = ["dry dog food", "dry cat food", "cat litter", "dog treats"]

# Agrupamos TODO en un diccionario para facilitar el procesamiento
categories_data = {
    # Originales
    "Fruits": fruits,
    "Vegetables": vegetables,
    "Canned Goods": canned_goods,
    "Dairy": dairy,
    "Meat": meat,
    "Fish & Seafood": fish_seafood,
    # Nuevas
    "Deli": deli,
    "Condiments": condiments,
    "Snacks": snacks,
    "Bread & Bakery": bread_bakery,
    "Beverages": beverages,
    "Pasta & Rice": pasta_rice,
    "Baking": baking,
    "Frozen Foods": frozen_foods,
    "Personal Care": personal_care,
    "Health Care": health_care,
    "Cleaning Supplies": cleaning_supplies,
    "Baby Items": baby_items,
    "Pet Care": pet_care
}

# --- 2. Generación de la Lista de Productos ---

products_list = []
product_id_counter = 1001  # Empezamos los IDs desde 1001

print("Generando lista de productos con todas las categorías...")

for category, items in categories_data.items():
    for item_name in items:
        
        # Asignar un precio aleatorio "realista" según la categoría
        if category in ["Fruits", "Vegetables"]:
            price = round(random.uniform(0.50, 4.00), 2)
        elif category == "Canned Goods":
            price = round(random.uniform(1.00, 3.50), 2)
        elif category == "Dairy":
            price = round(random.uniform(1.20, 6.00), 2)
        elif category == "Meat":
            price = round(random.uniform(5.00, 15.00), 2)
        elif category == "Fish & Seafood":
            price = round(random.uniform(7.00, 18.00), 2)
        elif category == "Deli":
            price = round(random.uniform(3.00, 10.00), 2)
        elif category == "Condiments":
            price = round(random.uniform(1.50, 5.00), 2)
        elif category == "Snacks":
            price = round(random.uniform(1.00, 4.50), 2)
        elif category == "Bread & Bakery":
            price = round(random.uniform(1.50, 5.00), 2)
        elif category == "Beverages":
            price = round(random.uniform(1.00, 8.00), 2)
        elif category == "Pasta & Rice":
            price = round(random.uniform(1.00, 6.00), 2)
        elif category == "Baking":
            price = round(random.uniform(1.50, 7.00), 2)
        elif category == "Frozen Foods":
            price = round(random.uniform(2.00, 10.00), 2)
        elif category == "Personal Care":
            price = round(random.uniform(2.00, 12.00), 2)
        elif category == "Health Care":
            price = round(random.uniform(3.00, 15.00), 2)
        elif category == "Cleaning Supplies":
            price = round(random.uniform(2.50, 10.00), 2)
        elif category == "Baby Items":
            price = round(random.uniform(5.00, 25.00), 2)
        elif category == "Pet Care":
            price = round(random.uniform(5.00, 20.00), 2)
        else:
            price = round(random.uniform(1.00, 10.00), 2)
        
        # Añadir el producto al diccionario
        products_list.append({
            "product_id": product_id_counter,
            "product_name": item_name.title(),  # Pone la primera letra en mayúscula
            "category": category,
            "price": price
        })
        
        product_id_counter += 1

# --- 3. Creación del DataFrame ---

df_products = pd.DataFrame(products_list)

# --- 4. Guardado en CSV ---

PATH = "datasets/"
csv_filename = PATH + "products_full.csv" # He cambiado el nombre para no sobrescribir el anterior
df_products.to_csv(csv_filename, index=False) # index=False para no guardar el índice de pandas

# --- 5. Mostrar Resultados ---

print(f"\n--- Vista Previa del DataFrame de Productos (Completo) ---")
print(df_products.head()) # Muestra las primeras 5 filas

print(f"\n--- Resumen del DataFrame ---")
print(df_products.info())

print(f"\n--- Productos Totales por Categoría ---")
print(df_products['category'].value_counts())

print(f"\n✅ ¡DataFrame completo guardado exitosamente como '{csv_filename}'!")
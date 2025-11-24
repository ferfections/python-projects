import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

try:
    df_products = pd.read_csv("products_macro.csv")
except "FileNotFoundError":
    print("ERROR: no se ha podido encontrar el archivo products_macro.csv")

# --- PASO 1: LIMPIEZA DE DATOS ---
# Asumo que tu DataFrame se llama df_products
# (Si no lo tienes cargado, cárgalo primero. Ej: df_products = pd.read_csv('mercadona.csv'))

print("--- 1. Limpiando DataFrame de Productos ---")

def clean_price(price_str):
    """Convierte un string de precio como '1,50 €' a un float 1.50"""
    if isinstance(price_str, (int, float)):
        return price_str
    if price_str is None or pd.isna(price_str):
        return np.nan
    
    # Elimina el símbolo '€', quita espacios y reemplaza la coma decimal
    try:
        cleaned = str(price_str).replace('€', '').strip().replace('.', '').replace(',', '.')
        return float(cleaned)
    except ValueError:
        return np.nan

# Aplicamos la limpieza a las columnas de precio
df_products['price'] = df_products['price'].apply(clean_price)
df_products['discount_price'] = df_products['discount_price'].apply(clean_price)

# Creamos una columna 'final_price'
# Usa el 'discount_price' si existe (no es NaN), si no, usa el 'price'
df_products['final_price'] = df_products['discount_price'].fillna(df_products['price'])

# Verificamos que ya no hay productos sin precio final (¡importante!)
df_products.dropna(subset=['final_price'], inplace=True)

# Guardamos solo los productos que necesitamos para la simulación
# (IDs y precios)
products_catalog = df_products[['id', 'final_price']].copy()
# Convertimos a una lista para que la simulación sea más rápida
# (product_id, price)
products_lookup = list(products_catalog.itertuples(index=False, name=None))

# También guardamos una lista de todos los IDs de productos válidos
valid_product_ids = products_catalog['id'].tolist()

print(f"Productos limpios y listos para simular: {len(products_lookup)}")
print(df_products[['name', 'price', 'discount_price', 'final_price']].head())

# --- PASO 2: SIMULACIÓN DE PEDIDOS ---

print("\n--- 2. Iniciando Simulación de Pedidos ---")

# --- Parámetros de la Simulación ---
N_ORDERS = 50000       # Número de tickets a simular
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 12, 31)

# Rango de productos DIFERENTES por ticket (ej. 1-15 productos)
MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 15

# Rango de UNIDADES por cada producto (ej. 1-5 unidades de leche)
MIN_QTY_PER_ITEM = 1
MAX_QTY_PER_ITEM = 5

# --- Generar la Tabla `df_orders` (Tickets) ---
order_data = []
current_order_id = 10001 # Empezamos desde el ID 10001
time_delta_seconds = int((END_DATE - START_DATE).total_seconds())

for i in range(N_ORDERS):
    # Genera una fecha y hora aleatoria dentro del rango de 1 año
    random_seconds = random.randint(0, time_delta_seconds)
    random_timestamp = START_DATE + timedelta(seconds=random_seconds)
    
    order_data.append({
        "order_id": current_order_id,
        "timestamp": random_timestamp
    })
    current_order_id += 1

df_orders = pd.DataFrame(order_data)
print(f"Generados {len(df_orders)} pedidos (tickets).")

# --- Generar la Tabla `df_order_details` (Líneas de producto) ---
order_details_list = []

for order_id in df_orders['order_id']:
    # 1. Decidir cuántos productos distintos tendrá este ticket
    num_different_items = random.randint(MIN_ITEMS_PER_ORDER, MAX_ITEMS_PER_ORDER)
    
    # 2. Elegir N productos al azar de TODO el catálogo
    # Usamos sample para asegurar que no se repite el mismo product_id
    # en el mismo ticket (aunque podríamos permitirlo si quisiéramos)
    chosen_product_ids = random.sample(valid_product_ids, num_different_items)
    
    # 3. Para cada producto, decidir la cantidad
    for prod_id in chosen_product_ids:
        quantity = random.randint(MIN_QTY_PER_ITEM, MAX_QTY_PER_ITEM)
        
        order_details_list.append({
            "order_id": order_id,
            "product_id": prod_id,
            "quantity": quantity
        })

df_order_details = pd.DataFrame(order_details_list)
print(f"Generados {len(df_order_details)} detalles de pedido (líneas de producto).")

# --- Guardar en CSV ---
df_orders.to_csv("sim_orders.csv", index=False)
df_order_details.to_csv("sim_order_details.csv", index=False)

print("\n--- Simulación Completa ---")
print("Head de 'sim_orders.csv':")
print(df_orders.head())
print("\nHead de 'sim_order_details.csv':")
print(df_order_details.head())

# --- PASO 3: UNIR TODO PARA EL ANÁLISIS ---

print("\n--- 3. Combinando todos los datos para el análisis ---")

# 1. Unimos los detalles (qué se compró) con los pedidos (cuándo se compró)
df_merged = pd.merge(
    df_order_details,  # Izquierda
    df_orders,         # Derecha
    on="order_id"      # Clave común
)

# 2. Ahora unimos el resultado con el catálogo de productos
#    para obtener nombres, categorías y precios.
#    Usamos 'id' de df_products y 'product_id' de df_merged
df_final_analysis = pd.merge(
    df_merged,
    df_products, # Tu DF limpio del Paso 1
    left_on="product_id",
    right_on="id"
)

# 3. Calculamos la columna más importante para el negocio:
#    el total de esa línea de producto
df_final_analysis['line_total'] = df_final_analysis['quantity'] * df_final_analysis['final_price']

# 4. Limpiamos columnas duplicadas o innecesarias
df_final_analysis = df_final_analysis.drop(columns=['id']) # 'id' (de producto) es duplicado de 'product_id'
df_final_analysis = df_final_analysis.sort_values(by="timestamp") # Ordenamos cronológicamente

# --- Guardar el DataFrame final de análisis ---
df_final_analysis.to_csv("analysis_dataset.csv", index=False)

print("¡DataFrame final de análisis creado y guardado como 'analysis_dataset.csv'!")
print("\n--- Vista Previa del Dataset Final ---")
print(df_final_analysis.head())

print("\n--- Información del Dataset Final ---")
df_final_analysis.info()

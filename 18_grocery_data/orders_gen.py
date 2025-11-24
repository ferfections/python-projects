import pandas as pd
import random

products = pd.read_csv("datasets/products.csv")

def generate_purchase():
    num_items = random.randint(1, 20)

    purchase = []

    for _ in range(num_items):
        quantity = random.randint(1,4)
        product_id = random.randint(products["product_id"].min(), products["product_id"].max())
        
        purchase.append([quantity, product_id])

    return purchase

def main():
    print("Compra de hoy:")
    purchase = generate_purchase()
    print(purchase)

if __name__ == "__main__":
    main()
import pandas as pd

def limpiar_df(df):
    # 2. Convertir 'OrderDate' a un objeto de fecha real
    # Esto nos dará acceso a .dt.month, .dt.year, etc.
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])

    # 3. Convertir 'Shipped' (Yes/No) a un booleano (True/False)
    # El método .map() es perfecto para reemplazar valores.
    df['Shipped'] = df['Shipped'].map({'Yes': True, 'No': False})

    # 4. Crear la columna de ingresos que usamos en los ejercicios
    df['TotalRevenue'] = df['Quantity'] * df['Price']


def main():
    df = pd.read_csv('orders.csv')
    limpiar_df(df)


    # print(df[["CustomerName", "Product", "Country"]])
    # print(df[df['Country'] == 'Mexico'])
    # print(df[(df["Category"] == "Electronics") & (df["Shipped"] == False)])

    # print(df[(df["Country"] == 'Argentina') | (df['Country'] == 'Mexico')])

    # paises_buscados = ['Argentina', 'Mexico']
    # df['Country'].isin(paises_buscados)

    # print(f'Total Revenue: {df['TotalRevenue'].sum():.2f}')

    # print(f'Mean price: {df['Price'].mean():.2f}')
    # print('\n')

    # ingresos_por_pais = df.groupby('Country')['TotalRevenue'].sum()
    # print(ingresos_por_pais)

    cantidad_por_categoria = df.groupby('Category')['Quantity'].sum()
    print(cantidad_por_categoria)

    metricas_por_categoria = df.groupby('Category').agg(
        Ingresos_Totales = ('TotalRevenue', 'sum'),
        Precio_Medio = ('Price', 'mean')
    )

    print(metricas_por_categoria)

    top_3_clients = df.sort_values(by='TotalRevenue',ascending=False)[:3]
    print(top_3_clients[["CustomerName", "TotalRevenue"]])



if __name__ == '__main__':
    main()
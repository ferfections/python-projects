import pandas as pd

df = pd.DataFrame(
    {
        "Nombre":["Fernando", "Lucía", "Pablo"],
        "Edad":[24, 23, 24]
    })

df.to_csv("personas.csv")
print(df)
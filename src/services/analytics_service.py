import pandas as pd


def analyze_transactions():

    df = pd.read_csv("data/transacoes.csv")

    total = df["valor"].sum()

    average = df["valor"].mean()

    return {
        "total_gastos": total,
        "media_gastos": average
    }
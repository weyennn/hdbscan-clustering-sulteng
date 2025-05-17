import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def load_data():
    path = os.path.join("data", "raw", "sulteng_indikator.csv")
    df = pd.read_csv(path, sep=";")  # ganti separator jika perlu
    return df

def rename_columns(df):
    df = df.rename(columns={
        "Kabupaten/Kota": "Kabupaten",
        "AHH": "ahh",
        "RLS": "rls",
        "HLS": "hls",
        "Pengeluaran Per Kapita": "pengeluaran",
        "Persentase Penduduk Miskin": "miskin",
        "Gini Rasio": "gini",
        "TPT": "tpt"
    })
    return df

def normalize(df, save_path):
    scaler = StandardScaler()
    X = df.drop(columns=["Kabupaten"])
    X_scaled = scaler.fit_transform(X)
    df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    df_scaled["Kabupaten"] = df["Kabupaten"]
    df_scaled.to_csv(save_path, index=False)
    print(f" Data scaled disimpan ke: {save_path}")
    return df_scaled

def save_clean(df, save_path):
    df.to_csv(save_path, index=False)
    print(f"Data asli disimpan ke: {save_path}")

def main():
    out_dir = os.path.join("data", "processed")
    os.makedirs(out_dir, exist_ok=True)

    df = load_data()
    df = rename_columns(df)

    raw_out = os.path.join(out_dir, "sulteng_clean.csv")
    scaled_out = os.path.join(out_dir, "sulteng_scaled.csv")

    save_clean(df, raw_out)
    normalize(df, scaled_out)

if __name__ == "__main__":
    main()

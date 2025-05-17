import pandas as pd
import os

# Load data hasil clustering
df = pd.read_csv("data/processed/sulteng_clustered.csv")

# Kolom numerik untuk dirata-ratakan
num_cols = df.select_dtypes(include="number").drop(columns=["cluster", "probability"], errors="ignore").columns

# Rata-rata indikator per klaster
summary = df.groupby("cluster")[num_cols].mean().round(2)

# Tambahkan jumlah wilayah per klaster
summary["jumlah_wilayah"] = df.groupby("cluster")["Kabupaten"].count()

# Tambahkan daftar kabupaten per klaster (dalam satu kolom)
summary["daftar_kabupaten"] = df.groupby("cluster")["Kabupaten"].apply(lambda x: ", ".join(sorted(x)))

# Simpan ke CSV
output_path = "data/processed/ringkasan_per_klaster.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
summary.to_csv(output_path)

print(f"Ringkasan per klaster disimpan ke: {output_path}")

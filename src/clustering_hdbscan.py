import pandas as pd
import hdbscan
import os

def load_scaled_data():
    path = os.path.join("data", "processed", "sulteng_scaled.csv")
    df = pd.read_csv(path)
    return df

def run_hdbscan(df, min_cluster_size=3):
    kabupaten = df["Kabupaten"]  # simpan dulu
    X = df.drop(columns=["Kabupaten"])
    model = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size)
    labels = model.fit_predict(X)
    probs = model.probabilities_
    
    df_result = pd.DataFrame(X)
    df_result["Kabupaten"] = kabupaten
    df_result["cluster"] = labels
    df_result["probability"] = probs
    return df_result, model

def save_cluster_result(df_result):
    path = os.path.join("data", "processed", "sulteng_clustered.csv")
    df_result.to_csv(path, index=False)
    print(f"Hasil clustering disimpan ke: {path}")

def summarize_clusters(df_result):
    print("\nRingkasan Jumlah Wilayah per Klaster:")
    print(df_result["cluster"].value_counts().sort_index())
    print("\nOutlier (cluster = -1):")
    print(df_result[df_result["cluster"] == -1]["Kabupaten"].values)

def main():
    df = load_scaled_data()
    df_result, model = run_hdbscan(df, min_cluster_size=3)
    save_cluster_result(df_result)
    summarize_clusters(df_result)

if __name__ == "__main__":
    main()

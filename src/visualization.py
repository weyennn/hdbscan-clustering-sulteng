import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from adjustText import adjust_text
import os

def load_clustered_data():
    path = os.path.join("data", "processed", "sulteng_clustered.csv")
    df = pd.read_csv(path)
    return df

def plot_pca_clusters(df, save_path="hasil/pca_clusters.png"):
    features = df.drop(columns=["kabupaten", "cluster", "probability"])
    pca = PCA(n_components=2)
    components = pca.fit_transform(features)

    df_plot = df.copy()
    df_plot["PC1"] = components[:, 0]
    df_plot["PC2"] = components[:, 1]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x="PC1", y="PC2",
        hue="cluster",
        data=df_plot,
        palette="Set2",
        style=df_plot["cluster"].apply(lambda x: "Outlier" if x == -1 else "Normal"),
        s=100,
        edgecolor='k'
    )

    texts = []
    for i in range(len(df_plot)):
        label = f"{df_plot['kabupaten'][i]} (C{df_plot['cluster'][i]})" if df_plot["cluster"][i] != -1 else f"{df_plot['kabupaten'][i]} (Outlier)"
        texts.append(plt.text(df_plot["PC1"][i], df_plot["PC2"][i], label, fontsize=8))

    adjust_text(texts, arrowprops=dict(arrowstyle="-", color='gray', lw=0.5))



    plt.title("Visualisasi PCA Hasil Clustering")
    plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    os.makedirs("hasil", exist_ok=True)
    plt.savefig(save_path)
    plt.show()
    print(f"Plot PCA disimpan ke: {save_path}")

def main():
    df = load_clustered_data()
    plot_pca_clusters(df)

if __name__ == "__main__":
    main()

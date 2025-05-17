import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    geo_path = os.path.join("data", "shapefile", "Sulawesi_Tengah_ADMIN_BPS.shp")
    cluster_path = os.path.join("data", "processed", "sulteng_clustered.csv")

    gdf = gpd.read_file(geo_path)
    df = pd.read_csv(cluster_path)

    # Normalisasi nama kabupaten (pastikan match)
    df["Kabupaten"] = df["Kabupaten"].str.lower()
    df["Kabupaten"] = df["Kabupaten"].replace({"tolitoli": "toli-toli"})
    gdf["Kabupaten"] = gdf["Kabupaten"].str.lower()

    # Join shapefile + data cluster
    merged = gdf.merge(df, on="Kabupaten", how="left")
    return merged

def plot_map(gdf):
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))

    # Fix sinkronisasi warna manual
    unique_clusters = sorted(gdf["cluster"].dropna().unique())
    cmap = plt.cm.get_cmap("Set2", len(unique_clusters))
    color_map = {cluster: cmap(i) for i, cluster in enumerate(unique_clusters)}
    gdf["color"] = gdf["cluster"].map(color_map)

    # Plot dengan warna manual
    gdf.plot(color=gdf["color"], linewidth=0.8, edgecolor="black", ax=ax)

    # Legend manual
    import matplotlib.patches as mpatches
    handles = []
    for cluster in unique_clusters:
        label = f"Cluster {int(cluster)}" if cluster != -1 else "Outlier"
        patch = mpatches.Patch(color=color_map[cluster], label=label)
        handles.append(patch)

    ax.legend(handles=handles, title="Klaster", loc='center left', bbox_to_anchor=(1.05, 0.5),
              fontsize=9, title_fontsize=10)

    for idx, row in gdf.iterrows():
        plt.annotate(row["Kabupaten"].title(), xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                     horizontalalignment='center', fontsize=8)

    plt.title("Peta Klaster Kabupaten/Kota di Sulawesi Tengah")
    plt.axis("off")
    os.makedirs("hasil", exist_ok=True)
    plt.savefig("hasil/peta_klaster_sulteng.png", dpi=300)
    plt.show()


def main():
    gdf = load_data()
    plot_map(gdf)


if __name__ == "__main__":
    main()



# Segmentasi Wilayah Sulawesi Tengah dengan HDBSCAN

Proyek ini bertujuan untuk mengelompokkan kabupaten/kota di Provinsi Sulawesi Tengah berdasarkan indikator sosial ekonomi dari BPS, guna memberikan dasar rekomendasi kebijakan yang lebih tepat sasaran.

## 1. Latar Belakang
Wilayah Sulawesi Tengah memiliki karakteristik sosial ekonomi yang beragam. Untuk mendukung kebijakan pembangunan yang inklusif dan berbasis data, diperlukan segmentasi wilayah secara objektif. Klasterisasi ini menggunakan pendekatan HDBSCAN agar mampu mengidentifikasi pola tanpa memaksakan jumlah klaster tetap.

## 2. Dataset
Data bersumber dari BPS (Badan Pusat Statistik) dan mencakup 13 kabupaten/kota di Sulawesi Tengah. Indikator yang digunakan:

- Umur Harapan Hidup (AHH)
- Rata-rata Lama Sekolah (RLS)
- Harapan Lama Sekolah (HLS)
- Pengeluaran Per Kapita
- Persentase Penduduk Miskin
- Gini Rasio
- Tingkat Pengangguran Terbuka (TPT)

## 3. Metodologi

- Preprocessing: normalisasi data menggunakan MinMaxScaler / StandardScaler
- Clustering: menggunakan algoritma **HDBSCAN**
- Visualisasi: PCA 2D + pemetaan hasil klaster pada shapefile
- Tools: Python (Pandas, Scikit-learn, HDBSCAN, GeoPandas, Matplotlib)

## 4. Hasil Ringkasan Per Klaster

| Cluster | AHH | RLS | HLS | Pengeluaran | % Miskin | Gini | TPT | Jumlah Wilayah | Daftar Kabupaten |
|---------|-----|-----|-----|-------------|----------|------|-----|----------------|------------------|
| 0 | ... | ... | ... | ... | ... | ... | ... | 5 | buol, tojo una-una, ... |
| 1 | ... | ... | ... | ... | ... | ... | ... | 7 | poso, morowali, sigi, ... |
| -1 | ... | ... | ... | ... | ... | ... | ... | 1 | kota palu |

> Ringkasan lengkap disimpan dalam: `data/processed/ringkasan_per_klaster.csv`

## 5. Visualisasi
- **PCA Scatter Plot**: menampilkan distribusi klaster dalam ruang 2D
- **Peta Klastering**: kabupaten/kota diwarnai berdasarkan klaster hasil HDBSCAN (disimpan di `hasil/peta_klaster_sulteng.png`)

## 6. Interpretasi dan Rekomendasi Kebijakan

### Cluster 0
Wilayah dengan capaian pembangunan rendah. Perlu penguatan pada:
- Pendidikan dasar dan vokasi
- Infrastruktur kesehatan
- Pengentasan kemiskinan

### Cluster 1
Wilayah transisi menuju maju. Potensial dikembangkan melalui:
- Dukungan UKM dan ekonomi lokal
- Digitalisasi pelayanan publik
- Penguatan SDM dan pendidikan lanjut

### Outlier (Cluster -1)
Kota Palu menunjukkan karakteristik sangat tinggi di semua indikator:
- Cocok untuk pengembangan smart city
- Perlu penanganan ketimpangan urban
- Menjadi pusat inovasi regional

## 7. Struktur Folder
```
segmentasi-daerah-sulteng/
├── data/
│   ├── raw/                      # Dataset mentah
│   ├── processed/               # Data normalisasi, clustering, ringkasan
├── src/
│   ├── preprocessing.py
│   ├── clustering_hdbscan.py
│   ├── visualization.py
│   └── mapping.py
├── notebook/
│   └── eda_sulteng.ipynb
├── hasil/
│   └── peta_klaster_sulteng.png
├── requirements.txt
└── README.md
```

## 8. Referensi
- BPS: https://bps.go.id
- Nurlina et al. (2023). *Analisis Determinan IPM di Indonesia*. Jurnal Samudra Ekonomi.
- Saputra & Muflih (2025). *Pengelompokan Wilayah Indonesia Berdasarkan Komponen IPM*. Jurnal SKANIKA.

---

> Dibuat oleh: Yayang Matira
> Proyek eksploratif berbasis data spasial dan sosial ekonomi untuk Sulawesi Tengah


# Segmentasi Wilayah Sosial Ekonomi di Sulawesi Tengah

## Latar Belakang Masalah
Kabupaten/kota di Provinsi Sulawesi Tengah memiliki karakteristik sosial ekonomi
yang beragam. Penerapan kebijakan pembangunan yang seragam berpotensi tidak
tepat sasaran karena perbedaan tingkat kesejahteraan, pendidikan, dan kondisi ekonomi
antar wilayah.

Proyek ini bertujuan untuk melakukan segmentasi kabupaten/kota di Sulawesi Tengah
berdasarkan indikator sosial ekonomi guna mendukung analisis pembangunan daerah
dan perumusan kebijakan berbasis data yang lebih terarah.

---

## Data
- **Sumber:** Badan Pusat Statistik (BPS)
- **Unit analisis:** 13 kabupaten/kota di Provinsi Sulawesi Tengah
- **Indikator utama:**
  - Umur Harapan Hidup (AHH)
  - Rata-rata Lama Sekolah (RLS)
  - Harapan Lama Sekolah (HLS)
  - Pengeluaran per Kapita
  - Persentase Penduduk Miskin
  - Gini Rasio
  - Tingkat Pengangguran Terbuka (TPT)

---

## Pendekatan Analisis

### 1. Eksplorasi dan Pra-pemrosesan Data
- Analisis distribusi indikator sosial ekonomi antar wilayah
- Normalisasi data menggunakan **StandardScaler** untuk menyetarakan skala variabel

### 2. Clustering Wilayah
- Penerapan algoritma **HDBSCAN** untuk mengelompokkan wilayah berdasarkan
  kemiripan karakteristik sosial ekonomi
- Metode ini dipilih karena:
  - Tidak memerlukan penentuan jumlah klaster di awal
  - Mampu menangani perbedaan kepadatan data
  - Dapat mengidentifikasi wilayah **outlier** secara otomatis

### 3. Visualisasi
- Proyeksi **PCA 2D** untuk membantu interpretasi hasil clustering
- Pemetaan klaster pada peta administrasi wilayah Sulawesi Tengah

---

## Hasil Segmentasi
- Kabupaten/kota di Sulawesi Tengah terbagi ke dalam beberapa klaster
  dengan karakteristik sosial ekonomi yang berbeda.
- Sebagian wilayah membentuk klaster dengan capaian pembangunan relatif rendah,
  sementara klaster lainnya menunjukkan kondisi sosial ekonomi yang lebih baik.
- **Kota Palu** teridentifikasi sebagai **outlier**, dengan nilai indikator
  yang jauh berbeda dibandingkan wilayah lainnya.

Ringkasan kuantitatif per klaster disimpan pada:
`data/processed/ringkasan_per_klaster.csv`

---

## Insight Utama
- Ketimpangan sosial ekonomi antar wilayah di Sulawesi Tengah membentuk
  pola klaster yang jelas dan tidak bersifat acak.
- Wilayah dengan karakteristik pembangunan serupa cenderung berada
  dalam klaster yang sama.
- Identifikasi outlier membantu mencegah distorsi analisis dan memberikan
  pemahaman yang lebih akurat terhadap struktur wilayah.

---

## Rekomendasi Kebijakan

### Klaster dengan Pembangunan Relatif Rendah
- Prioritas pada peningkatan pendidikan dasar dan vokasi
- Penguatan layanan kesehatan dan program pengentasan kemiskinan
- Intervensi pembangunan berbasis kebutuhan lokal

### Klaster Wilayah Transisi
- Dukungan pengembangan UMKM dan ekonomi lokal
- Digitalisasi layanan publik
- Peningkatan kualitas sumber daya manusia

### Wilayah Outlier (Kota Palu)
- Potensi pengembangan sebagai pusat pertumbuhan dan inovasi regional
- Fokus pada pengelolaan ketimpangan urban dan pembangunan berkelanjutan
- Penguatan konsep smart city dan layanan perkotaan

---

## Visualisasi
- **PCA Scatter Plot** untuk distribusi klaster dalam ruang 2D
- **Peta Klaster Wilayah** disimpan pada:
  `hasil/peta_klaster_sulteng.png`

---

## Tools & Library
- Python, Pandas, Scikit-learn
- HDBSCAN
- GeoPandas
- Matplotlib, Seaborn

---

## Struktur Proyek
```
segmentasi-daerah-sulteng/
├── data/
│   ├── raw/
│   ├── processed/
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

## Penulis

Yayang Matira | Mahasiswa Magister Ilmu Komputer | Universitas Gadjah Mada

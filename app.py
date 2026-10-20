import streamlit as st
import pandas as pd

# ==================================================
# 1. KONFIGURASI APLIKASI
# ==================================================
st.set_page_config(
    page_title="SPK SAW | Cindyani Tiwi Lestari",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# 2. DESAIN UI (High-End Dynamic Glassmorphism & Modern Styling)
# ==================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stApp {
        background: #090D16;
        background-image: 
            radial-gradient(at 0% 0%, rgba(30, 58, 138, 0.12) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(217, 119, 6, 0.08) 0px, transparent 50%);
        background-attachment: fixed;
    }

    [data-testid="stHeader"] {
        background-color: rgba(9, 13, 22, 0.85);
        backdrop-filter: blur(12px);
    }

    /* Sidebar Premium Look */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0B1120 0%, #111827 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    [data-testid="stSidebar"] * {
        color: #F3F4F6;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.1);
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: #9CA3AF;
    }

    /* Custom Radio Styling in Sidebar */
    div[data-testid="stSidebar"] div.row-widget.stRadio > div {
        background: rgba(255, 255, 255, 0.03);
        padding: 8px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .brand {
        font-size: 26px;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
        margin: 6px 0 2px 0;
    }

    .brand-subtitle {
        color: #9CA3AF;
        font-size: 12px;
        font-weight: 500;
        margin-bottom: 24px;
    }

    .page-eyebrow {
        color: #F59E0B;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .page-title {
        color: #F9FAFB;
        font-size: 34px;
        line-height: 1.2;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0 0 10px 0;
    }

    .page-description {
        color: #9CA3AF;
        font-size: 15px;
        line-height: 1.7;
        margin-bottom: 32px;
    }

    /* Hero Banner Dynamic Glow */
    .hero {
        background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 50%, #090D16 100%);
        border-radius: 24px;
        padding: 40px;
        color: white;
        margin-bottom: 28px;
        border: 1px solid rgba(245, 158, 11, 0.2);
        box-shadow: 0 20px 40px -15px rgba(15, 23, 42, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }

    .hero-label {
        color: #FBBF24;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-bottom: 14px;
    }

    .hero-title {
        color: #FFFFFF;
        font-size: 32px;
        line-height: 1.25;
        font-weight: 800;
        margin-bottom: 14px;
        letter-spacing: -0.5px;
    }

    .hero-text {
        color: #CBD5E1;
        font-size: 15px;
        line-height: 1.8;
        max-width: 780px;
    }

    .section-heading {
        color: #F3F4F6;
        font-size: 21px;
        font-weight: 750;
        margin: 32px 0 16px 0;
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Floating Cards */
    .info-card {
        background: linear-gradient(145deg, #111827 0%, #0F172A 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 24px;
        min-height: 140px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }

    .info-card:hover {
        transform: translateY(-4px);
        border-color: rgba(245, 158, 11, 0.4);
        box-shadow: 0 15px 30px -5px rgba(245, 158, 11, 0.1);
    }

    .info-label {
        color: #9CA3AF;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .info-value {
        color: #F9FAFB;
        font-size: 30px;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .info-note {
        color: #6B7280;
        font-size: 12px;
        margin-top: 8px;
    }

    /* Winner Card Elite */
    .winner-card {
        background: linear-gradient(135deg, rgba(146, 64, 14, 0.2) 0%, rgba(217, 119, 6, 0.1) 100%);
        border: 1px solid rgba(245, 158, 11, 0.5);
        border-left: 6px solid #F59E0B;
        border-radius: 20px;
        padding: 28px;
        margin: 20px 0 28px 0;
        box-shadow: 0 15px 30px -10px rgba(217, 119, 6, 0.2);
        backdrop-filter: blur(10px);
    }

    .winner-label {
        color: #FBBF24;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .winner-name {
        color: #FFFFFF;
        font-size: 28px;
        font-weight: 800;
        margin: 8px 0;
        letter-spacing: -0.5px;
    }

    .winner-score {
        color: #F59E0B;
        font-size: 19px;
        font-weight: 700;
    }

    /* Step Card */
    .step-card {
        background: linear-gradient(145deg, #111827 0%, #0F172A 100%);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 14px;
        height: 100%;
        box-shadow: 0 8px 20px -5px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .step-card:hover {
        transform: translateY(-3px);
        border-color: rgba(255, 255, 255, 0.2);
    }

    .step-number {
        color: #F59E0B;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }

    .step-title {
        color: #F9FAFB;
        font-weight: 750;
        font-size: 16px;
        margin-bottom: 6px;
    }

    .step-description {
        color: #9CA3AF;
        font-size: 13px;
        line-height: 1.6;
    }

    /* Metrics Styling */
    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #111827 0%, #0F172A 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 8px 20px -5px rgba(0, 0, 0, 0.2);
    }

    div[data-testid="stMetricLabel"] {
        color: #9CA3AF;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #F9FAFB;
        font-weight: 800;
    }

    /* Buttons */
    div.stButton > button,
    div.stDownloadButton > button {
        border-radius: 12px;
        font-weight: 700;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.25s ease;
        padding: 10px 20px;
    }

    div.stButton > button:hover,
    div.stDownloadButton > button:hover {
        border-color: #F59E0B;
        color: #F59E0B;
        transform: translateY(-2px);
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #D97706 0%, #B45309 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(217, 119, 6, 0.4);
    }

    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        color: white;
        box-shadow: 0 6px 20px rgba(217, 119, 6, 0.6);
    }

    /* Dataframe Table Customization */
    [data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6B7280;
        font-size: 12px;
        padding: 40px 0 20px 0;
        border-top: 1px solid rgba(255, 255, 255, 0.06);
        margin-top: 50px;
        font-weight: 500;
        letter-spacing: 0.5px;
    }

    #MainMenu, footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)


# ==================================================
# 3. DATA PENELITIAN
# ==================================================
data = {
    "Alternatif": ["A1", "A2", "A3", "A4", "A5", "A6"],
    "Nama Karyawan": [
        "Dewi Astuti",
        "M. Rizky Saputra",
        "Melda Fitria",
        "Ahmanuddin",
        "Darwansyah",
        "Andrian Wahyudi"
    ],
    "C1 - Disiplin": [0.75, 1.00, 0.75, 1.00, 1.00, 1.00],
    "C2 - Kualitas Pekerjaan": [0.75, 0.75, 1.00, 0.75, 1.00, 0.75],
    "C3 - Kerja Sama": [0.75, 0.75, 1.00, 0.75, 0.75, 1.00],
    "C4 - Perilaku": [1.00, 1.00, 0.75, 0.75, 1.00, 0.75],
}

df = pd.DataFrame(data)

kriteria = {
    "C1 - Disiplin": {"bobot": 0.5, "jenis": "Benefit"},
    "C2 - Kualitas Pekerjaan": {
        "bobot": 1.0, "jenis": "Benefit"
    },
    "C3 - Kerja Sama": {"bobot": 0.5, "jenis": "Benefit"},
    "C4 - Perilaku": {"bobot": 1.0, "jenis": "Benefit"},
}

kolom_kriteria = list(kriteria.keys())
bobot = [kriteria[k]["bobot"] for k in kolom_kriteria]


# ==================================================
# 4. PERHITUNGAN SAW
# ==================================================
matriks = df[kolom_kriteria].copy()
normalisasi = pd.DataFrame(index=matriks.index)

for kolom in kolom_kriteria:
    jenis = kriteria[kolom]["jenis"]

    if jenis == "Benefit":
        maksimum = matriks[kolom].max()
        normalisasi[kolom] = (
            matriks[kolom] / maksimum if maksimum != 0 else 0
        )
    else:
        minimum = matriks[kolom].min()
        normalisasi[kolom] = minimum / matriks[kolom]

df_hasil = df[["Alternatif", "Nama Karyawan"]].copy()
df_hasil["Nilai SAW"] = normalisasi.mul(bobot, axis=1).sum(axis=1)

df_hasil["Peringkat"] = (
    df_hasil["Nilai SAW"]
    .rank(method="dense", ascending=False)
    .astype(int)
)

df_hasil = df_hasil.sort_values(
    ["Peringkat", "Nama Karyawan"]
).reset_index(drop=True)

terbaik = df_hasil.iloc[0]


# ==================================================
# 5. KOMPONEN UI
# ==================================================
def judul_halaman(eyebrow, judul, deskripsi):
    st.markdown(
        f"""
        <div class="page-eyebrow">{eyebrow}</div>
        <div class="page-title">{judul}</div>
        <div class="page-description">{deskripsi}</div>
        """,
        unsafe_allow_html=True
    )


def tabel(dataframe, format_dict=None):
    tampilan = dataframe.copy()

    if format_dict:
        st.dataframe(
            tampilan.style.format(format_dict),
            hide_index=True,
            use_container_width=True
        )
    else:
        st.dataframe(
            tampilan,
            hide_index=True,
            use_container_width=True
        )


def footer():
    st.markdown(
        """
        <div class="footer">
            SISTEM PENUNJANG KEPUTUSAN · METODE SIMPLE ADDITIVE WEIGHTING
            <br>
            PT. Cindyani Tiwi Lestari
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# 6. INISIALISASI SESSION STATE HALAMAN
# ==================================================
daftar_menu = [
    "Beranda",
    "Data Alternatif",
    "Kriteria dan Bobot",
    "Matriks Keputusan",
    "Perhitungan SAW",
    "Hasil Perangkingan",
]

if "halaman_pilihan" not in st.session_state:
    st.session_state["halaman_pilihan"] = "Beranda"


# ==================================================
# 7. SIDEBAR
# ==================================================
with st.sidebar:
    st.markdown(
        """
        <div style="font-size:32px; margin-bottom: 2px;">🏆</div>
        <div class="brand">SPK SAW</div>
        <div class="brand-subtitle">
            Pemilihan Karyawan Terbaik
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Menggunakan key "halaman_pilihan" langsung agar state sinkron otomatis tanpa double-click
    halaman = st.radio(
        "MENU UTAMA",
        daftar_menu,
        key="halaman_pilihan",
        label_visibility="visible"
    )

    st.divider()

    st.markdown(
        """
        <div style="font-size:12px; line-height:2.2;">
            <b>METODE</b><br>
            Simple Additive Weighting<br><br>
            <b>JUMLAH ALTERNATIF</b><br>
            6 karyawan<br><br>
            <b>JUMLAH KRITERIA</b><br>
            4 kriteria
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# 8. BERANDA
# ==================================================
if halaman == "Beranda":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-label">Decision Support System</div>
            <div class="hero-title">
                Sistem Penunjang Keputusan<br>
                Pemilihan Karyawan Terbaik
            </div>
            <div class="hero-text">
                PT. Cindyani Tiwi Lestari<br>
                Penerapan metode Simple Additive Weighting (SAW)
                untuk membantu menentukan alternatif karyawan
                berdasarkan kriteria dan bobot penilaian.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">TOTAL ALTERNATIF</div>
                <div class="info-value">{len(df)}</div>
                <div class="info-note">Data karyawan yang dinilai</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">TOTAL KRITERIA</div>
                <div class="info-value">{len(kolom_kriteria)}</div>
                <div class="info-note">Indikator penilaian karyawan</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">TOTAL BOBOT</div>
                <div class="info-value">{sum(bobot):.2f}</div>
                <div class="info-note">Jumlah seluruh bobot kriteria</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-heading">✨ Tahapan Metode SAW</div>',
        unsafe_allow_html=True
    )

    langkah = [
        ("01", "Data alternatif", "Menentukan karyawan yang akan dinilai."),
        ("02", "Kriteria dan bobot", "Menetapkan indikator dan bobot penilaian."),
        ("03", "Matriks keputusan", "Menyusun nilai setiap alternatif."),
        ("04", "Normalisasi", "Mengubah nilai ke skala yang sebanding."),
        ("05", "Nilai preferensi", "Mengalikan nilai normalisasi dengan bobot."),
        ("06", "Perangkingan", "Mengurutkan alternatif dari nilai tertinggi."),
    ]

    for start in range(0, len(langkah), 3):
        cols = st.columns(3)

        for col, item in zip(cols, langkah[start:start + 3]):
            with col:
                st.markdown(
                    f"""
                    <div class="step-card">
                        <div class="step-number">TAHAP {item[0]}</div>
                        <div class="step-title">{item[1]}</div>
                        <div class="step-description">{item[2]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown(
        '<div class="section-heading">🏆 Ringkasan Hasil Perhitungan</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="winner-card">
            <div class="winner-label">🏆 Nilai Preferensi Tertinggi</div>
            <div class="winner-name">{terbaik["Nama Karyawan"]}</div>
            <div class="winner-score">
                Nilai SAW: {terbaik["Nilai SAW"]:.3f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Lihat Hasil Perangkingan →", type="primary"):
        st.session_state["halaman_pilihan"] = "Hasil Perangkingan"
        st.rerun()

    st.caption(
        "Sumber data: penelitian Sukiakhy, Jummi, dan Utami (2022)."
    )


# ==================================================
# 9. DATA ALTERNATIF
# ==================================================
elif halaman == "Data Alternatif":
    judul_halaman(
        "DATA MASTER",
        "Data Alternatif Karyawan",
        "Daftar karyawan yang menjadi alternatif dalam proses pengambilan keputusan."
    )

    st.metric("Jumlah Alternatif", len(df))

    tabel(df[["Alternatif", "Nama Karyawan"]])

    st.caption(
        "Data alternatif mengikuti penelitian yang dijadikan referensi."
    )


# ==================================================
# 10. KRITERIA DAN BOBOT
# ==================================================
elif halaman == "Kriteria dan Bobot":
    judul_halaman(
        "KONFIGURASI PENILAIAN",
        "Kriteria dan Bobot",
        "Kriteria yang digunakan untuk menilai setiap alternatif karyawan."
    )

    data_kriteria = pd.DataFrame([
        {
            "Kode": nama.split(" - ")[0],
            "Nama Kriteria": nama.split(" - ", 1)[1],
            "Bobot": detail["bobot"],
            "Jenis": detail["jenis"]
        }
        for nama, detail in kriteria.items()
    ])

    c1, c2 = st.columns(2)

    c1.metric("Jumlah Kriteria", len(kriteria))
    c2.metric("Total Bobot", f"{sum(bobot):.2f}")

    tabel(data_kriteria, {"Bobot": "{:.2f}"})

    st.info(
        "Benefit berarti semakin tinggi nilai kriteria, "
        "semakin baik alternatif. Seluruh kriteria pada "
        "data ini bertipe benefit."
    )


# ==================================================
# 11. MATRIKS KEPUTUSAN
# ==================================================
elif halaman == "Matriks Keputusan":
    judul_halaman(
        "TAHAP 01",
        "Matriks Keputusan",
        "Nilai awal setiap karyawan berdasarkan empat kriteria penilaian."
    )

    tabel(
        df,
        {
            "C1 - Disiplin": "{:.2f}",
            "C2 - Kualitas Pekerjaan": "{:.2f}",
            "C3 - Kerja Sama": "{:.2f}",
            "C4 - Perilaku": "{:.2f}",
        }
    )

    st.caption("X = matriks keputusan awal.")


# ==================================================
# 12. PERHITUNGAN SAW
# ==================================================
elif halaman == "Perhitungan SAW":
    judul_halaman(
        "TAHAP 02",
        "Perhitungan Metode SAW",
        "Proses normalisasi matriks dan perhitungan nilai preferensi setiap alternatif."
    )

    with st.expander("Lihat rumus normalisasi", expanded=True):
        st.latex(r"r_{ij} = \frac{x_{ij}}{\max_i(x_{ij})}")
        st.write(
            "Rumus tersebut digunakan untuk kriteria benefit. "
            "Untuk kriteria cost, rumusnya adalah nilai minimum "
            "dibagi nilai alternatif."
        )

    st.markdown(
        '<div class="section-heading">Matriks Normalisasi</div>',
        unsafe_allow_html=True
    )

    tabel(
        pd.concat(
            [df[["Alternatif", "Nama Karyawan"]], normalisasi],
            axis=1
        ),
        {kolom: "{:.3f}" for kolom in kolom_kriteria}
    )

    st.info(
        "Nilai maksimum seluruh kriteria adalah 1, sehingga "
        "matriks normalisasi sama dengan matriks keputusan."
    )

    st.divider()

    with st.expander("Lihat bobot dan rumus nilai preferensi"):
        st.latex(r"V_i = \sum_{j=1}^{n} w_j r_{ij}")

        for _, baris in df.iterrows():
            nilai = normalisasi.loc[baris.name]

            komponen = [
                f"({bobot[i]:g} × {nilai[kolom_kriteria[i]]:g})"
                for i in range(len(kolom_kriteria))
            ]

            hasil = df_hasil.loc[
                df_hasil["Alternatif"] == baris["Alternatif"],
                "Nilai SAW"
            ].iloc[0]

            st.markdown(
                f"**{baris['Alternatif']} — {baris['Nama Karyawan']}**"
            )
            st.code(f"{' + '.join(komponen)} = {hasil:.3f}")


# ==================================================
# 13. HASIL PERANGKINGAN
# ==================================================
elif halaman == "Hasil Perangkingan":
    judul_halaman(
        "HASIL AKHIR",
        "Perangkingan Karyawan",
        "Urutan alternatif berdasarkan nilai preferensi SAW dari tertinggi ke terendah."
    )

    st.markdown(
        f"""
        <div class="winner-card">
            <div class="winner-label">🏆 Karyawan dengan Nilai Tertinggi</div>
            <div class="winner-name">{terbaik["Nama Karyawan"]}</div>
            <div class="winner-score">
                {terbaik["Nilai SAW"]:.3f} poin
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-heading">Tabel Hasil Perangkingan</div>',
        unsafe_allow_html=True
    )

    tabel(
        df_hasil[
            ["Peringkat", "Alternatif", "Nama Karyawan", "Nilai SAW"]
        ],
        {"Nilai SAW": "{:.3f}"}
    )

    st.markdown(
        '<div class="section-heading">Perbandingan Nilai SAW</div>',
        unsafe_allow_html=True
    )

    grafik = (
        df_hasil.sort_values("Nilai SAW", ascending=True)
        .set_index("Nama Karyawan")[["Nilai SAW"]]
    )

    st.bar_chart(grafik, horizontal=True)

    st.download_button(
        "⬇ Unduh Hasil Perangkingan (CSV)",
        data=df_hasil.to_csv(index=False).encode("utf-8-sig"),
        file_name="hasil_perangkingan_saw.csv",
        mime="text/csv",
        type="primary"
    )

    st.caption(
        "Peringkat menggunakan metode dense ranking. "
        "Alternatif dengan nilai SAW yang sama memperoleh peringkat yang sama."
    )


# ==================================================
# 14. FOOTER
# ==================================================
footer()
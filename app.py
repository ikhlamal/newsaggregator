import streamlit as st
import pandas as pd
import os
import urllib.parse

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=300, height=400, scrolling=True)

def format_tweet(row):
    tweet_html = f'''
        <blockquote class="twitter-tweet" data-media-max-width="300" data-conversation="none">
        <a href={row['tweet_url']}></a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    '''
    return tweet_html

def main():
    st.set_page_config(layout="centered")
    csv_files = ["csv1.csv", "csv2.csv", "csv3.csv", "csv4.csv", "csv5.csv", "csv6.csv",
                "csv7.csv", "csv8.csv", "csv9.csv", "csv10.csv", "csv11.csv", "csv12.csv"]
    
    # Filter CSV files that exist
    existing_csv_files = [csv_file for csv_file in csv_files if os.path.exists(csv_file)]

    if len(existing_csv_files) == 0:
        st.error("Tidak ada file CSV yang ditemukan.")
        return

    # Menyimpan nilai current_tweet_index di session_state
    for csv_file in existing_csv_files:
        for j in range(1, 3):  # 2 pasangan CSV
            key = f'current_tweet_index{csv_file}{j}'
            if key not in st.session_state:
                st.session_state[key] = 0

    # Judul dan jumlah tweet untuk setiap pasangan CSV
    titles_and_counts = [
        ("***:red[Populer]*** \u2014 Pendukung Minta Prabowo dan Titiek Soeharto Rujuk, Ekspresi Didit Disorot (Viva)", ["csv1.csv", "csv2.csv"]),
        ("Jokowi Respons Kabar Rencana Bertemu Megawati Dijembatani Sultan DIY (CNN)", ["csv3.csv", "csv4.csv"]),
        ("Baju Hitam Menteri Jokowi dan Ahok di Hari Pencoblosan Pemilu 2024 (CNN)", ["csv5.csv", "csv6.csv"]),
        ("Jokowi Minta Dugaan Kecurangan Pemilu Dilaporkan, PDI-P: Banyak Pihak Justru Ragukan Independensi Bawaslu (Kompas)", ["csv7.csv", "csv8.csv"]),
        ("Rincian 90 Orang Pegawai KPK yang Terima Pungli Rutan (Detik)", ["csv9.csv", "csv10.csv"]),
        ("***:red[Populer]*** \u2014 Jokowi: Jangan Teriak-teriak Pemilu Curang, kalau Ada Bukti, Bawa ke Bawaslu dan MK (Kompas)", ["csv11.csv", "csv12.csv"])
    ]

    for title, csv_pair in titles_and_counts:
        with st.expander(title, expanded=False):
            num_cols = len(csv_pair)
    
            # Membagi layar menjadi baris dan kolom sesuai dengan jumlah file CSV
            cols = st.columns(num_cols)
            for j, csv_file in enumerate(csv_pair):
                with cols[j]:
                    df = pd.read_csv(csv_file)
                    if df.empty:
                        with st.container(height=650, border=True):
                            col7, col8, col9 = st.columns([1] * 3)
                            with col7:
                                if st.session_state[f'current_tweet_index{csv_file}{j+1}'] > 0:
                                    if st.button("⬅️", key=f"left{csv_file}{j+1}"):
                                        st.session_state[f'current_tweet_index{csv_file}{j+1}'] -= 1
                                else:
                                    st.button("⬅️", key=f"left{csv_file}{j+1}")
                            with col8:
                                if st.session_state[f'current_tweet_index{csv_file}{j+1}'] < len(tweets) - 1:
                                    if st.button("➡️", key=f"right{csv_file}{j+1}"):
                                        st.session_state[f'current_tweet_index{csv_file}{j+1}'] += 1
                                else:
                                    st.button("➡️", key=f"right{csv_file}{j+1}")
                            with col9:
                                if j == 0:
                                    st.write("👍:", len(df))
                                elif j == 1:
                                    st.write("👎:", len(df)) 
                            st.error(f"Tweet tidak ditemukan.")
                            continue

                    # List tweet
                    tweets = [format_tweet(row) for index, row in df.iterrows()]

                    with st.container(height=400, border=True):
                        col7, col8, col9 = st.columns([1] * 3)
                        with col7:
                            if st.session_state[f'current_tweet_index{csv_file}{j+1}'] > 0:
                                if st.button("⬅️", key=f"left{csv_file}{j+1}"):
                                    st.session_state[f'current_tweet_index{csv_file}{j+1}'] -= 1
                            else:
                                st.button("⬅️", key=f"left{csv_file}{j+1}")
                        with col8:
                            if st.session_state[f'current_tweet_index{csv_file}{j+1}'] < len(tweets) - 1:
                                if st.button("➡️", key=f"right{csv_file}{j+1}"):
                                    st.session_state[f'current_tweet_index{csv_file}{j+1}'] += 1
                            else:
                                st.button("➡️", key=f"right{csv_file}{j+1}")
                        with col9:
                            if j == 0:
                                st.write("👍:", len(df))
                            elif j == 1:
                                st.write("👎:", len(df)) 
                        # Menampilkan tweet yang baru setelah klik tombol
                        show_tweet(tweets[st.session_state[f'current_tweet_index{csv_file}{j+1}']])

if __name__ == "__main__":
    main()

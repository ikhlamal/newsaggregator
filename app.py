import streamlit as st
import pandas as pd
import os

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=350, height=405, scrolling=True)

def format_tweet(row):
    tweet_html = f'''
        <blockquote class="twitter-tweet" data-media-max-width="350">
        <a href={row['tweet_url']}></a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    '''
    return tweet_html

def main():
    st.set_page_config(layout="wide")
    csv_files = ["csv1.csv", "csv2.csv", "csv3.csv", "csv4.csv", "csv5.csv", "csv6.csv", 
                 "csv7.csv", "csv8.csv", "csv9.csv", "csv10.csv", "csv11.csv", "csv12.csv"]
    
    # Filter CSV files that exist
    existing_csv_files = [csv_file for csv_file in csv_files if os.path.exists(csv_file)]

    if len(existing_csv_files) == 0:
        st.error("Tidak ada file CSV yang ditemukan.")
        return

    # Menyimpan nilai current_tweet_index di session_state
    for i in range(len(existing_csv_files)):
        key = f'current_tweet_index{i+1}'
        if key not in st.session_state:
            st.session_state[key] = 0

    # Membagi layar menjadi dua baris dua kolom
    num_cols = 3
    col_width = 12 // num_cols
    cols = [st.columns(num_cols) for _ in range(len(existing_csv_files))]

    for i, csv_file in enumerate(existing_csv_files):
        df = pd.read_csv(csv_file)

        if df.empty:
            cols[i][0].error(f"File CSV '{csv_file}' kosong.")
            continue

        # List tweet
        tweets = [format_tweet(row) for index, row in df.iterrows()]

        with cols[i][0]:
            with st.container(height=500, border=True):
                col7, _, _, _, _, col12 = st.columns([1] * 6)
                with col7:
                    if st.session_state[f'current_tweet_index{i+1}'] > 0:
                        if st.button("⬅️", key=f"left{i+1}"):
                            st.session_state[f'current_tweet_index{i+1}'] -= 1
                with col12:
                    if st.session_state[f'current_tweet_index{i+1}'] < len(tweets) - 1:
                        if st.button("➡️", key=f"right{i+1}"):
                            st.session_state[f'current_tweet_index{i+1}'] += 1

                # Menampilkan tweet yang baru setelah klik tombol
                show_tweet(tweets[st.session_state[f'current_tweet_index{i+1}']])

if __name__ == "__main__":
    main()

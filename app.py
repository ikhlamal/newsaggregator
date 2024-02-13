import streamlit as st
import pandas as pd
import os
import urllib.parse


def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=500, height=405, scrolling=True)

# def format_tweet(row):
#     tweet_html = f'''
#         <blockquote class="twitter-tweet" data-media-max-width="500">
#         <a href={row['tweet_url']}></a></blockquote>
#         <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
#     '''
#     return tweet_html

def format_tweet(row):
    tweet_url = row['tweet_url']  # Ambil URL tweet dari DataFrame
    escaped_tweet_url = urllib.parse.quote(tweet_url, safe='')  # Escape URL tweet
    iframe_url = f"https://twitframe.com/show?url={escaped_tweet_url}"  # Buat URL untuk iframe
    
    # Buat HTML untuk iframe dengan menggunakan URL yang sudah disiapkan
    tweet_html = f'''
        <iframe border=0 frameborder=0 height=250 width=450 
        src="{iframe_url}"></iframe>
    '''
    return tweet_html

def main():
    st.set_page_config(layout="wide")
    csv_files = ["csv1.csv", "csv2.csv"]
    
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
    with st.expander("Reaksi Gibran soal Klaim Ganjar Menang Pilpres di Luar Negeri versi Exit Poll"):
        num_cols = min(len(existing_csv_files), 2)
    
        # Membagi layar menjadi dua baris dua kolom
        for i in range(0, len(existing_csv_files), num_cols):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                index = i + j
                if index < len(existing_csv_files):
                    with cols[j]:
                        csv_file = existing_csv_files[index]
                        df = pd.read_csv(csv_file)
                        if df.empty:
                            st.error(f"Tweet dari berita ke-{index+1} kosong.")
                            continue
    
                        # List tweet
                        tweets = [format_tweet(row) for index, row in df.iterrows()]
    
                        with st.container(height=550, border=True):
                            col7, _, _, _, _, col12 = st.columns([1] * 6)
                            with col7:
                                if st.session_state[f'current_tweet_index{index+1}'] > 0:
                                    if st.button("⬅️", key=f"left{index+1}"):
                                        st.session_state[f'current_tweet_index{index+1}'] -= 1
                            with col12:
                                if st.session_state[f'current_tweet_index{index+1}'] < len(tweets) - 1:
                                    if st.button("➡️", key=f"right{index+1}"):
                                        st.session_state[f'current_tweet_index{index+1}'] += 1

                            # Menampilkan tweet yang baru setelah klik tombol
                            show_tweet(tweets[st.session_state[f'current_tweet_index{index+1}']])
                            st.write("Total Tweet: ", len(df))

if __name__ == "__main__":
    main()

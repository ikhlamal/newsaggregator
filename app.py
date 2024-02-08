import streamlit as st
import pandas as pd

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
    
    # Membaca data dari 12 file CSV
    dfs = [pd.read_csv(f"csv{i}.csv") for i in range(1, 13)]
    
    # List tweet dari masing-masing CSV
    tweets = [[format_tweet(row) for index, row in df.iterrows()] for df in dfs]

    # Menyimpan nilai current_tweet_index di session_state untuk setiap file CSV
    for i in range(1, 13):
        session_key = f"current_tweet_index{i}"
        if session_key not in st.session_state:
            st.session_state[session_key] = 0

    # Membagi layar menjadi beberapa kolom sesuai dengan jumlah file CSV
    num_columns = 4  # Ubah sesuai kebutuhan
    columns = [st.columns(num_columns) for _ in range(3)]  # Membagi menjadi 3 baris

    # Menampilkan tweet dari setiap file CSV
    for i, col_group in enumerate(columns):
        for j, col in enumerate(col_group):
            with col:
                with st.container(height=500, border=True):
                    col7, col8, col9, col10, col11, col12 = st.columns(6)
                    with col7:
                        session_key_left = f"left{i * num_columns + j + 1}"
                        if st.session_state[f"current_tweet_index{i * num_columns + j + 1}"] > 0:
                            if st.button("⬅️", key=session_key_left):
                                st.session_state[f"current_tweet_index{i * num_columns + j + 1}"] -= 1
                    with col12:
                        session_key_right = f"right{i * num_columns + j + 1}"
                        if st.session_state[f"current_tweet_index{i * num_columns + j + 1}"] < len(tweets[i * num_columns + j]) - 1:
                            if st.button("➡️", key=session_key_right):
                                st.session_state[f"current_tweet_index{i * num_columns + j + 1}"] += 1

                    # Menampilkan tweet yang baru setelah klik tombol
                    show_tweet(tweets[i * num_columns + j][st.session_state[f"current_tweet_index{i * num_columns + j + 1}"]])

if __name__ == "__main__":
    main()

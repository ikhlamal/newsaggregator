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
    
    # Membaca file CSV
    dfs = [pd.read_csv(f"csv{i}.csv") for i in range(1, 13)]

    # Menyiapkan list tweet untuk setiap file CSV
    tweets = [[format_tweet(row) for index, row in df.iterrows()] for df in dfs]

    # Menyimpan nilai current_tweet_index di session_state untuk setiap file CSV
    for i in range(1, 13):
        key = f"current_tweet_index{i}"
        if key not in st.session_state:
            st.session_state[key] = 0

    # Membagi layar menjadi 4 baris 3 kolom
    for i, df_tweets in enumerate(tweets):
        if i % 3 == 0:
            row = st.columns(3)
        with row[i % 3]:
            with st.container(height=500, border=True):
                col7, col8, col9, col10, col11, col12 = st.columns(6)
                with col7:
                    if st.session_state[f"current_tweet_index{i+1}"] > 0:
                        if st.button("⬅️", key=f"left{i+1}"):
                            st.session_state[f"current_tweet_index{i+1}"] -= 1
                with col12:
                    if st.session_state[f"current_tweet_index{i+1}"] < len(df_tweets) - 1:
                        if st.button("➡️", key=f"right{i+1}"):
                            st.session_state[f"current_tweet_index{i+1}"] += 1

                # Menampilkan tweet yang baru setelah klik tombol
                show_tweet(df_tweets[st.session_state[f"current_tweet_index{i+1}"]])

if __name__ == "__main__":
    main()

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
    dfs = [pd.read_csv(f"csv{i}.csv") for i in range(1, 4)]

    # List tweet
    tweets = [[format_tweet(row) for index, row in df.iterrows()] for df in dfs]

    # Menyimpan nilai current_tweet_index di session_state
    for i in range(len(dfs)):
        key = f'current_tweet_index{i}'
        if key not in st.session_state:
            st.session_state[key] = 0

    num_cols = 3
    num_containers = len(dfs)

    # Membagi layar menjadi dua baris dua kolom
    for i in range(num_containers):
        col_index = i % num_cols
        row_index = i // num_cols
        with st.container(height=500, border=True):
            col7, _, _, _, _, col12 = st.columns([1, 1, 1, 1, 1, 7])
            with col7:
                if st.session_state[f'current_tweet_index{i}'] > 0:
                    if st.button("⬅️", key=f"left{i}"):
                        st.session_state[f'current_tweet_index{i}'] -= 1
            with col12:
                if st.session_state[f'current_tweet_index{i}'] < len(tweets[i]) - 1:
                    if st.button("➡️", key=f"right{i}"):
                        st.session_state[f'current_tweet_index{i}'] += 1

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets[i][st.session_state[f'current_tweet_index{i}']])

if __name__ == "__main__":
    main()

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
    dfs = [pd.read_csv(f"csv{i}.csv") for i in range(1, 4)]  # Load CSV files dynamically

    # List tweet
    tweets = [[format_tweet(row) for index, row in df.iterrows()] for df in dfs]

    # Menyimpan nilai current_tweet_index di session_state
    current_tweet_indexes = {}
    for i in range(len(dfs)):
        key = f'current_tweet_index{i+1}'
        if key not in st.session_state:
            st.session_state[key] = 0
        current_tweet_indexes[key] = st.session_state[key]

    # Membagi layar menjadi dua baris dua kolom
    col1, col2, col3 = st.columns(3)

    for i, (df, tweet_list) in enumerate(zip(dfs, tweets)):
        with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
            with st.container(height=500, border=True):
                col7, col8, col9, col10, col11, col12 = st.columns(6)
                with col7:
                    key_left = f"left{i+1}"
                    if current_tweet_indexes[f'current_tweet_index{i+1}'] > 0:
                        if st.button("⬅️", key=key_left):
                            current_tweet_indexes[f'current_tweet_index{i+1}'] -= 1
                with col12:
                    key_right = f"right{i+1}"
                    if current_tweet_indexes[f'current_tweet_index{i+1}'] < len(tweet_list) - 1:
                        if st.button("➡️", key=key_right):
                            current_tweet_indexes[f'current_tweet_index{i+1}'] += 1

                # Menampilkan tweet yang baru setelah klik tombol
                show_tweet(tweet_list[current_tweet_indexes[f'current_tweet_index{i+1}']])

if __name__ == "__main__":
    main()

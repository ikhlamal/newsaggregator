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
    dfs = [pd.read_csv(f"csv{i}.csv") for i in range(1, 4)]  # Load all CSV files
    tweets = [[format_tweet(row) for index, row in df.iterrows()] for df in dfs]  # List of tweets for each CSV

    # Menyimpan nilai current_tweet_index di session_state
    for i in range(1, 4):
        key = f'current_tweet_index{i}'
        if key not in st.session_state:
            st.session_state[key] = 0

    num_cols = 3  # Jumlah kolom yang tetap
    num_containers = -(-len(dfs) // num_cols)  # Pembagian bulat ke atas

    for i in range(num_containers):
        container = st.container(height=500, border=True)
        col1, col2, col3 = container.columns(3)

        with col1:
            if st.session_state[f'current_tweet_index{i+1}'] > 0:
                if st.button("⬅️", key=f"left{i+1}"):
                    st.session_state[f'current_tweet_index{i+1}'] -= 1

        with col3:
            if st.session_state[f'current_tweet_index{i+1}'] < len(tweets[i]) - 1:
                if st.button("➡️", key=f"right{i+1}"):
                    st.session_state[f'current_tweet_index{i+1}'] += 1

        # Menampilkan tweet yang baru setelah klik tombol
        show_tweet(tweets[i][st.session_state[f'current_tweet_index{i+1}']])

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=350, height=400, scrolling=True)

def format_tweet(row):
    tweet_html = f'''
        <blockquote class="twitter-tweet" data-media-max-width="350">
        <a href={row['tweet_url']}></a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    '''
    return tweet_html

def main():
    st.set_page_config(layout="wide")
    df1 = pd.read_csv("csv1.csv")
    df2 = pd.read_csv("csv2.csv")
    df3 = pd.read_csv("csv3.csv")

    # List tweet
    tweets1 = [format_tweet(row) for index, row in df1.iterrows()]
    tweets2 = [format_tweet(row) for index, row in df2.iterrows()]
    tweets3 = [format_tweet(row) for index, row in df3.iterrows()]

    # Menyimpan nilai current_tweet_index di session_state
    if 'current_tweet_index1' not in st.session_state:
        st.session_state.current_tweet_index1 = 0

    if 'current_tweet_index2' not in st.session_state:
        st.session_state.current_tweet_index2 = 0

    if 'current_tweet_index3' not in st.session_state:
        st.session_state.current_tweet_index3 = 0

    # Membagi layar menjadi dua baris dua kolom
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(height=500, border=True):
            col7, col8, col9, col10, col11, col12 = st.columns(6)
            with col7:
                if st.session_state.current_tweet_index1 > 0:
                    if st.button("⬅️", key="left1"):
                        st.session_state.current_tweet_index1 -= 1
            with col12:
                if st.session_state.current_tweet_index1 < len(tweets1) - 1:
                    if st.button("➡️", key="right1"):
                        st.session_state.current_tweet_index1 += 1

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets1[st.session_state.current_tweet_index1])

    with col2:
        with st.container(height=500, border=True):
            col7, col8, col9, col10, col11, col12 = st.columns(6)
            with col7:
                if st.session_state.current_tweet_index2 > 0:
                    if st.button("⬅️", key="left2"):
                        st.session_state.current_tweet_index2 -= 1
            with col12:
                if st.session_state.current_tweet_index2 < len(tweets2) - 1:
                    if st.button("➡️", key="right2"):
                        st.session_state.current_tweet_index2 += 1

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets2[st.session_state.current_tweet_index2])

    with col3:
        with st.container(height=500, border=True):
            col7, col8, col9, col10, col11, col12 = st.columns(6)
            with col7:
                if st.session_state.current_tweet_index3 > 0:
                    if st.button("⬅️", key="left3"):
                        st.session_state.current_tweet_index3 -= 1
            with col12:
                if st.session_state.current_tweet_index3 < len(tweets3) - 1:
                    if st.button("➡️", key="right3"):
                        st.session_state.current_tweet_index3 += 1

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets3[st.session_state.current_tweet_index3])

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=250, height=650)

def format_tweet(row):
    tweet_html = f'''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <a href={row['tweet_url']}></a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    '''
    return tweet_html

def main():
    st.set_page_config(layout="wide")
    df1 = pd.read_csv("csv1.csv")
    df2 = pd.read_csv("csv2.csv")
    df3 = pd.read_csv("csv3.csv")
    df4 = pd.read_csv("csv4.csv")

    # List tweet
    tweets1 = [format_tweet(row) for index, row in df1.iterrows()]
    tweets2 = [format_tweet(row) for index, row in df2.iterrows()]
    tweets3 = [format_tweet(row) for index, row in df3.iterrows()]
    tweets4 = [format_tweet(row) for index, row in df4.iterrows()]

    # Menyimpan nilai current_tweet_index di session_state
    if 'current_tweet_index1' not in st.session_state:
        st.session_state.current_tweet_index1 = 0

    if 'current_tweet_index2' not in st.session_state:
        st.session_state.current_tweet_index2 = 0

    if 'current_tweet_index3' not in st.session_state:
        st.session_state.current_tweet_index3 = 0

    if 'current_tweet_index4' not in st.session_state:
        st.session_state.current_tweet_index4 = 0

    # Membagi layar menjadi dua baris dua kolom
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.session_state.current_tweet_index1 > 0:
            if st.button("⬅️", key="left1"):
                st.session_state.current_tweet_index1 -= 1
    
        if st.session_state.current_tweet_index1 < len(tweets1) - 1:
            if st.button("➡️", key="right1"):
                st.session_state.current_tweet_index1 += 1
        with st.expander("", expanded=True):
            st.markdown('<style>div.Widget.row-widget.stRadio>div{flex-direction:column;}</style>',unsafe_allow_html=True)
            st.markdown(
                """<style>
                .reportview-container .main .block-container{
                    padding: 1rem;
                    border-radius: 10px;
                    border: 20px solid #008080;
                }
                </style>
                """, unsafe_allow_html=True)

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets1[st.session_state.current_tweet_index1])

    with col2:
        with st.expander("", expanded=True):
            st.markdown('<style>div.Widget.row-widget.stRadio>div{flex-direction:column;}</style>',unsafe_allow_html=True)
            st.markdown(
                """<style>
                .reportview-container .main .block-container{
                    padding: 1rem;
                    border-radius: 10px;
                    border: 20px solid #008080;
                }
                </style>
                """, unsafe_allow_html=True)
            if st.session_state.current_tweet_index2 > 0:
                if st.button("⬅️", key="left2"):
                    st.session_state.current_tweet_index2 -= 1
            if st.session_state.current_tweet_index2 < len(tweets2) - 1:
                if st.button("➡️", key="right2"):
                    st.session_state.current_tweet_index2 += 1

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets2[st.session_state.current_tweet_index2])

    with col3:
        with st.expander("", expanded=True):
            st.markdown('<style>div.Widget.row-widget.stRadio>div{flex-direction:column;}</style>',unsafe_allow_html=True)
            st.markdown(
                """<style>
                .reportview-container .main .block-container{
                    padding: 1rem;
                    border-radius: 10px;
                    border: 20px solid #008080;
                }
                </style>
                """, unsafe_allow_html=True)
            if st.session_state.current_tweet_index3 > 0:
                if st.button("⬅️", key="left3"):
                    st.session_state.current_tweet_index3 -= 1
            if st.session_state.current_tweet_index3 < len(tweets3) - 1:
                if st.button("➡️", key="right3"):
                    st.session_state.current_tweet_index3 += 1

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets3[st.session_state.current_tweet_index3])

    with col4:
        with st.expander("", expanded=True):
            st.markdown('<style>div.Widget.row-widget.stRadio>div{flex-direction:column;}</style>',unsafe_allow_html=True)
            st.markdown(
                """<style>
                .reportview-container .main .block-container{
                    padding: 1rem;
                    border-radius: 10px;
                    border: 20px solid #008080;
                }
                </style>
                """, unsafe_allow_html=True)
            if st.session_state.current_tweet_index4 > 0:
                if st.button("⬅️", key="left4"):
                    st.session_state.current_tweet_index4 -= 1
            if st.session_state.current_tweet_index4 < len(tweets4) - 1:
                if st.button("➡️", key="right4"):
                    st.session_state.current_tweet_index4 += 1

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets4[st.session_state.current_tweet_index4])

if __name__ == "__main__":
    main()

import streamlit as st

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=250, height=650)

def main():
    st.set_page_config(layout="wide")
    st.title("Aplikasi Tweet Viewer")

    # List tweet
    tweets1 = [
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 1</p>&mdash; User1 (@user1) 
        <a href="https://twitter.com/user1/status/1?ref_src=twsrc%5Etfw">
        January 1, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 2</p>&mdash; User2 (@user2) 
        <a href="https://twitter.com/user2/status/2?ref_src=twsrc%5Etfw">
        January 2, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 3</p>&mdash; User3 (@user3) 
        <a href="https://twitter.com/user3/status/3?ref_src=twsrc%5Etfw">
        January 3, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        '''
    ]

    tweets2 = [
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 1</p>&mdash; User1 (@user1) 
        <a href="https://twitter.com/user1/status/1?ref_src=twsrc%5Etfw">
        January 1, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 2</p>&mdash; User2 (@user2) 
        <a href="https://twitter.com/user2/status/2?ref_src=twsrc%5Etfw">
        January 2, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 3</p>&mdash; User3 (@user3) 
        <a href="https://twitter.com/user3/status/3?ref_src=twsrc%5Etfw">
        January 3, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        '''
    ]

    tweets3 = [
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 1</p>&mdash; User1 (@user1) 
        <a href="https://twitter.com/user1/status/1?ref_src=twsrc%5Etfw">
        January 1, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 2</p>&mdash; User2 (@user2) 
        <a href="https://twitter.com/user2/status/2?ref_src=twsrc%5Etfw">
        January 2, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 3</p>&mdash; User3 (@user3) 
        <a href="https://twitter.com/user3/status/3?ref_src=twsrc%5Etfw">
        January 3, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        '''
    ]

    tweets4 = [
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 1</p>&mdash; User1 (@user1) 
        <a href="https://twitter.com/user1/status/1?ref_src=twsrc%5Etfw">
        January 1, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 2</p>&mdash; User2 (@user2) 
        <a href="https://twitter.com/user2/status/2?ref_src=twsrc%5Etfw">
        January 2, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 3</p>&mdash; User3 (@user3) 
        <a href="https://twitter.com/user3/status/3?ref_src=twsrc%5Etfw">
        January 3, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        '''
    ]

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
        with st.expander("Tweet Viewer 1", expanded=True):
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
            if st.session_state.current_tweet_index1 > 0:
                if st.button("⬅️", key="left1"):
                    st.session_state.current_tweet_index1 -= 1
            if st.session_state.current_tweet_index1 < len(tweets1) - 1:
                if st.button("➡️", key="right1"):
                    st.session_state.current_tweet_index1 += 1

            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets1[st.session_state.current_tweet_index1])

    with col2:
        with st.expander("Tweet Viewer 2", expanded=True):
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
        with st.expander("Tweet Viewer 3", expanded=True):
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
        with st.expander("Tweet Viewer 4", expanded=True):
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

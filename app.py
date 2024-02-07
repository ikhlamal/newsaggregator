import streamlit as st

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=500, height=650)

def main():
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

    # Membagi layar menjadi dua kolom
    col1, col2 = st.columns(2)
    with col1:
        # Menyimpan nilai current_tweet_index di session_state
        if 'current_tweet_index1' not in st.session_state:
            st.session_state.current_tweet_index1 = 0
    
        # Menampilkan tweet saat ini
        with st.expander("Tweet Viewer", expanded=True):
            col1, col2, col3 = st.columns([1, 8, 1])
            if col1.button("⬅️1", key="left1") and st.session_state.current_tweet_index1 > 0:
                st.session_state.current_tweet_index1 -= 1
            elif col3.button("➡️1", key="right1") and st.session_state.current_tweet_index1 < len(tweets1) - 1:
                st.session_state.current_tweet_index1 += 1
    
            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets1[st.session_state.current_tweet_index1])
    
            # Memperbarui tombol kanan jika diperlukan
            if st.session_state.current_tweet_index1 == len(tweets1) - 1:
                col3.empty()  # Menghapus tombol kanan jika sudah mencapai tweet terakhir
            else:
                col3.button("➡️1_" + str(st.session_state.current_tweet_index1), key="right1_" + str(st.session_state.current_tweet_index1))
    with col2:
        # Menyimpan nilai current_tweet_index di session_state
        if 'current_tweet_index2' not in st.session_state:
            st.session_state.current_tweet_index2 = 0
    
        # Menampilkan tweet saat ini
        with st.expander("Tweet Viewer", expanded=True):
            col1, col2, col3 = st.columns([1, 8, 1])
            if col1.button("⬅️2", key="left2") and st.session_state.current_tweet_index2 > 0:
                st.session_state.current_tweet_index2 -= 1
            elif col3.button("➡️2", key="right2") and st.session_state.current_tweet_index2 < len(tweets2) - 1:
                st.session_state.current_tweet_index2 += 1
    
            # Menampilkan tweet yang baru setelah klik tombol
            show_tweet(tweets2[st.session_state.current_tweet_index2])
    
            # Memperbarui tombol kanan jika diperlukan
            if st.session_state.current_tweet_index2 == len(tweets2) - 1:
                col3.empty()  # Menghapus tombol kanan jika sudah mencapai tweet terakhir
            else:
                col3.button("➡️2_" + str(st.session_state.current_tweet_index2), key="right2_" + str(st.session_state.current_tweet_index2))

if __name__ == "__main__":
    main()

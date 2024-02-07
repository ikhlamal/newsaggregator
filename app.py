import streamlit as st

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=500, height=650)

def main():
    st.title("Aplikasi Tweet")

    # List tweet
    tweets = [
        '''
        <blockquote class="twitter-tweet"><p lang="in" dir="ltr">Muncul Aksi dari Caleg Gerindra Protes Guru Besar Unair Kritik Jokowi <a href="https://t.co/YJMYvUMQrh">https://t.co/YJMYvUMQrh</a></p>&mdash; CNN Indonesia (@CNNIndonesia) <a href="https://twitter.com/CNNIndonesia/status/1754454280558485924?ref_src=twsrc%5Etfw">February 5, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet"><p lang="in" dir="ltr">sekalian cebokin dah</p>&mdash; PremanTagakSurang (@akunlamakenaTD) <a href="https://twitter.com/akunlamakenaTD/status/1754459937693224989?ref_src=twsrc%5Etfw">February 5, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet"><p lang="in" dir="ltr">Muncul Aksi dari Caleg Gerindra Protes Guru Besar Unair Kritik Jokowi <a href="https://t.co/YJMYvUMQrh">https://t.co/YJMYvUMQrh</a></p>&mdash; CNN Indonesia (@CNNIndonesia) <a href="https://twitter.com/CNNIndonesia/status/1754454280558485924?ref_src=twsrc%5Etfw">February 5, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        '''
    ]

    # Menyimpan nilai current_tweet_index di session_state
    if 'current_tweet_index' not in st.session_state:
        st.session_state.current_tweet_index = 0

    # Menampilkan tweet saat ini
    st.header("Tweet")
    with st.expander("Tweet Viewer", expanded=True):
        col1, col2, col3 = st.columns([1, 8, 1])
        if col1.button("⬅️") and st.session_state.current_tweet_index > 0:
            st.session_state.current_tweet_index -= 1
        elif col3.button("➡️") and st.session_state.current_tweet_index < len(tweets) - 1:
            st.session_state.current_tweet_index += 1

        # Menampilkan tweet yang baru setelah klik tombol
        show_tweet(tweets[st.session_state.current_tweet_index])

        # Memperbarui tombol kanan jika diperlukan
        if st.session_state.current_tweet_index == len(tweets) - 1:
            col3.empty()  # Menghapus tombol kanan jika sudah mencapai tweet terakhir
        else:
            col3.button("➡️")

if __name__ == "__main__":
    main()

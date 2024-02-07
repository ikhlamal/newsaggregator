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

    # Inisialisasi index tweet saat ini
    current_tweet_index = 0

    # Menampilkan tweet saat ini
    st.header("Tweet")
    with st.expander("Tweet Viewer", expanded=True):
        col1, col2, col3 = st.columns([1, 8, 1])
        if col1.button("⬅️"):
            current_tweet_index = max(0, current_tweet_index - 1)
        if col3.button("➡️"):
            current_tweet_index = min(len(tweets) - 1, current_tweet_index + 1)

        # Memperbarui tweet yang akan ditampilkan
        show_tweet(tweets[current_tweet_index])

if __name__ == "__main__":
    main()

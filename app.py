import streamlit as st

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=500, height=400)

def main():
    st.title("Aplikasi Tweet Viewer")

    # List tweet
    tweets = [
        '''
        <blockquote class="twitter-tweet"><p lang="in" dir="ltr">Muncul Aksi dari Caleg Gerindra Protes Guru Besar Unair Kritik Jokowi <a href="https://t.co/YJMYvUMQrh">https://t.co/YJMYvUMQrh</a></p>&mdash; CNN Indonesia (@CNNIndonesia) <a href="https://twitter.com/CNNIndonesia/status/1754454280558485924?ref_src=twsrc%5Etfw">February 5, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
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

    # Inisialisasi index tweet saat ini
    current_tweet_index = 0

    # Menampilkan tweet saat ini
    st.header("Tweet")
    show_tweet(tweets[current_tweet_index])

    # Tombol untuk mengganti tweet
    col1, col2, col3 = st.columns(3)
    if col1.button("Kiri") and current_tweet_index > 0:
        current_tweet_index -= 1
    if col3.button("Kanan") and current_tweet_index < len(tweets) - 1:
        current_tweet_index += 1

    # Menampilkan tweet yang baru
    show_tweet(tweets[current_tweet_index])

if __name__ == "__main__":
    main()

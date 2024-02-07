import streamlit as st

def show_blog_post(thumbnail_url, title, source):
    st.write(f"### {title}")
    st.image(thumbnail_url, caption=title, use_column_width=True)
    st.write(f"*Sumber:* {source}")

def show_tweet(tweet_url):
    st.write(f'<blockquote class="twitter-tweet"><p lang="in" dir="ltr">Muncul Aksi dari Caleg Gerindra Protes Guru Besar Unair Kritik Jokowi <a href="https://t.co/YJMYvUMQrh">https://t.co/YJMYvUMQrh</a></p>&mdash; CNN Indonesia (@CNNIndonesia) <a href="https://twitter.com/CNNIndonesia/status/1754454280558485924?ref_src=twsrc%5Etfw">February 5, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>', unsafe_allow_html=True)

def main():
    st.title("Aplikasi Blog dan Tweet Viewer")

    # Menampilkan konten blog
    st.header("Konten Blog")
    thumbnail_url = "https://pluang-production-financial-content-input.s3.ap-southeast-1.amazonaws.com/production/2023/07/lk6kaj4tyleh4wucwar%3Aopenai.jpg"
    title = "Judul Postingan Blog"
    source = "ChatGPT"
    show_blog_post(thumbnail_url, title, source)

    # Menampilkan tweet menggunakan iframe
    st.header("Tweet")
    tweet_url = "https://twitter.com/CNNIndonesia/status/1754454280558485924"
    show_tweet(tweet_url)

if __name__ == "__main__":
    main()

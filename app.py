import streamlit as st

def show_blog_post(thumbnail_url, title, source):
    st.write(f"### {title}")
    st.image(thumbnail_url, caption=title, use_column_width=True)
    st.write(f"*Sumber:* {source}")

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=500, height=1400)

def main():
    st.title("Aplikasi Blog dan Tweet Viewer")

    # Menampilkan konten blog
    st.header("Konten Blog")
    thumbnail_url = "https://example.com/thumbnail.jpg"
    title = "Judul Postingan Blog"
    source = "www.exampleblog.com"
    show_blog_post(thumbnail_url, title, source)

    # Menampilkan tweet menggunakan HTML embed code
    st.header("Tweet")
    tweet_html = '''
    <blockquote class="twitter-tweet" data-media-max-width="1560"><p lang="in" dir="ltr">sekalian cebokin dah</p>&mdash; PremanTagakSurang (@akunlamakenaTD) <a href="https://twitter.com/akunlamakenaTD/status/1754459937693224989?ref_src=twsrc%5Etfw">February 5, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    '''
    show_tweet(tweet_html)

if __name__ == "__main__":
    main()

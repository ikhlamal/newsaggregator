import streamlit as st
import feedparser

def get_news_thumbnail(entry):
    # Coba mencari thumbnail dalam entri berita
    thumbnail_url = entry.get('media_thumbnail', [{}])[0].get('url')
    return thumbnail_url

def main():
    st.title("Google News RSS Feed")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    # Cetak hanya satu berita (entri pertama)
    entry = feed.entries[0]

    # Dapatkan URL thumbnail berita
    thumbnail_url = get_news_thumbnail(entry)

    # Tampilkan informasi berita dalam layout Streamlit
    if thumbnail_url:
        st.image(thumbnail_url, caption="Berita Terkini", use_column_width=True)

    st.header(entry.title)
    st.subheader(entry.published)

    st.write(entry.summary)

    st.text("Sumber: " + entry.source.title)

if __name__ == "__main__":
    main()

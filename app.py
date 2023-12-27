import streamlit as st
import feedparser

def main():
    st.title("Google News RSS Feed")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    # Cetak hanya satu berita (entri pertama)
    entry = feed.entries[0]

    # Mendapatkan tautan gambar dari entri berita
    image_url = entry.links[0]['href'] if 'links' in entry and entry.links else None

    # Tampilkan informasi berita dalam layout Streamlit
    if image_url:
        st.image(image_url, caption="Berita Terkini", use_column_width=True)

    st.header(entry.title)
    st.subheader(entry.published)

    st.write(entry.summary)

    st.text("Sumber: " + entry.source.title)

if __name__ == "__main__":
    main()

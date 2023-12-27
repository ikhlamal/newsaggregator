import streamlit as st
import feedparser
import requests
from bs4 import BeautifulSoup

def get_news_thumbnail(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        thumbnail_tag = soup.find('meta', property='og:image')
        thumbnail_url = thumbnail_tag.get('content') if thumbnail_tag else None
        return thumbnail_url
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    st.title("Google News RSS Feed")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    # Cetak hanya satu berita (entri pertama)
    entry = feed.entries[0]

    # Dapatkan thumbnail URL dari halaman berita
    thumbnail_url = get_news_thumbnail(entry.link)

    # Tampilkan informasi berita dalam layout Streamlit
    col1, col2 = st.columns([1, 2])

    # Kolom pertama (thumbnail)
    if thumbnail_url:
        col1.image(thumbnail_url, caption="", use_column_width=True)

    # Kolom kedua (judul, tanggal, dan link)
    with col2:
        st.markdown(f"<h2 style='text-align: left;'><a href='{entry.link}' target='_blank'>{entry.title}</a></h2>", unsafe_allow_html=True)
        st.subheader(entry.published)
        st.text("Sumber: " + entry.source.title)

if __name__ == "__main__":
    main()

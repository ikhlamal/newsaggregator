import streamlit as st
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

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

def format_time_difference(published_time):
    published_datetime = datetime.strptime(published_time, "%a, %d %b %Y %H:%M:%S %Z")
    time_difference = datetime.utcnow() - published_datetime

    if time_difference < timedelta(minutes=60):
        return f"{int(time_difference.total_seconds() / 60)} menit yang lalu"
    elif time_difference < timedelta(hours=24):
        return f"{int(time_difference.total_seconds() / 3600)} jam yang lalu"
    else:
        return f"{int(time_difference.total_seconds() / 86400)} hari yang lalu"

def main():
    st.set_page_config(layout="wide")

    st.title("Contoh Aja")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    # Cetak satu berita
    entry = feed.entries[0]

    # Dapatkan thumbnail URL dari halaman berita
    thumbnail_url = get_news_thumbnail(entry.link)

    # Cetak thumbnail dan judul berita utama
    if thumbnail_url:
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                <img src="{thumbnail_url}" alt="Thumbnail" style="max-width: 260px; max-height: 150px; margin-bottom: 10px;">
                <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{entry.link}' target='_blank'>{entry.title}</a></h4>
                <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(entry.published)}</p>
                <p style='font-size: 12px;'>Sumber: {entry.source.title}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Membuat tombol untuk memilih berita
    selected_news = st.radio("Pilih Berita:", [f"{i + 1}. Berita {i + 1}" for i in range(4)])

    # Cetak konten berita terpilih
    selected_index = int(selected_news.split(".")[0]) - 1
    selected_entry = feed.entries[selected_index]

    # Dapatkan thumbnail URL dari halaman berita terpilih
    selected_thumbnail_url = get_news_thumbnail(selected_entry.link)

    # Cetak konten berita terpilih
    if selected_thumbnail_url:
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                <img src="{selected_thumbnail_url}" alt="Thumbnail" style="max-width: 260px; max-height: 150px; margin-bottom: 10px;">
                <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{selected_entry.link}' target='_blank'>{selected_entry.title}</a></h4>
                <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(selected_entry.published)}</p>
                <p style='font-size: 12px;'>Sumber: {selected_entry.source.title}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()

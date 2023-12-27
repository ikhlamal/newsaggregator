import streamlit as st
import feedparser
import requests
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
    # Ubah waktu publikasi ke objek datetime
    published_datetime = datetime.strptime(published_time, "%a, %d %b %Y %H:%M:%S %Z")

    # Hitung perbedaan waktu antara waktu publikasi dan waktu saat ini
    time_difference = datetime.utcnow() - published_datetime

    # Ubah perbedaan waktu ke format "n jam yang lalu"
    if time_difference < timedelta(minutes=60):
        return f"{int(time_difference.total_seconds() / 60)} menit yang lalu"
    elif time_difference < timedelta(hours=24):
        return f"{int(time_difference.total_seconds() / 3600)} jam yang lalu"
    else:
        return f"{int(time_difference.total_seconds() / 86400)} hari yang lalu"

def main():
    # Set layout menjadi wide
    st.set_page_config(layout="wide")

    st.title("Google News RSS Feed")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    # Cetak satu berita
    entry = feed.entries[0]

    # Dapatkan thumbnail URL dari halaman berita
    thumbnail_url = get_news_thumbnail(entry.link)

    # Tampilkan informasi berita dalam layout Streamlit dengan 4 kolom yang sama
    cols = st.columns(4)

    for col in cols:
        if thumbnail_url:
            col.markdown(
                f"""
                <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; display: flex; align-items: center; margin-bottom: 10px;">
                    <img src="{thumbnail_url}" alt="Thumbnail" style="max-width: 80px; height: auto; margin-right: 10px;">
                    <div style="flex: 1;">
                        <h4 style='text-align: left; font-size: 8px; margin-bottom: 5px;'><a href='{entry.link}' target='_blank'>{entry.title}</a></h4>
                        <p style='text-align: left; font-size: 6px; margin-bottom: 5px;'>{format_time_difference(entry.published)}</p>
                        <p style='text-align: left; font-size: 6px;'>Sumber: {entry.source.title}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()

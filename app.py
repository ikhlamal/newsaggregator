import streamlit as st
import feedparser
from bs4 import BeautifulSoup
import requests
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

    st.title("Contoh Aja")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    # Tampilkan dropdown untuk memilih berita
    selected_news_index = st.selectbox("Pilih Berita", range(4), format_func=lambda x: f"Berita {x + 1}")

    # Dapatkan data berita yang dipilih
    if selected_news_index == 0:
        entry = feed.entries[0]  # Berita utama
    else:
        entry = feed.entries[0]  # Berita utama
        summaries = BeautifulSoup(entry.summary, 'html.parser').find_all('a')[1:4]  # Ambil 3 berita terkait ke-2 hingga ke-4
        entry = feed.entries[selected_news_index] if selected_news_index < 4 else summaries[selected_news_index - 1]

    # Dapatkan thumbnail URL dari halaman berita
    thumbnail_url = get_news_thumbnail(entry.link)

    # Tampilkan informasi berita
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

    # Tampilkan berita terkait dari summary berita utama
    if 'summary' in entry:
        summaries = BeautifulSoup(entry.summary, 'html.parser').find_all('a')[1:4]  # Ambil 3 berita terkait ke-2 hingga ke-4
        for i, summary in enumerate(summaries):
            link = summary.get('href')
            title = summary.get_text(strip=True)
            source = summary.find_next('font').get_text(strip=True)

            thumbnail_url_related = get_news_thumbnail(link)

            if thumbnail_url_related:
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                        <img src="{thumbnail_url_related}" alt="Thumbnail" style="max-width: 260px; max-height: 150px; margin-bottom: 10px;">
                        <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{link}' target='_blank'>{title}</a></h4>
                        <p style='font-size: 12px; margin-bottom: 5px;'>x jam yang lalu</p>
                        <p style='font-size: 12px; margin-bottom: 5px;'>Sumber: {source}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

if __name__ == "__main__":
    main()

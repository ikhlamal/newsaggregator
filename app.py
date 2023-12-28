import streamlit as st
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

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

def get_article_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Identifikasi tag dan kelas yang mengandung teks artikel
        article_elements = soup.find_all('div', class_='detail_body')  # Ganti dengan tag dan kelas yang sesuai

        # Gabungkan teks dari elemen-elemen tersebut
        article_text = ' '.join(element.get_text() for element in article_elements)

        return article_text
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

    # Sidebar untuk dropdown
    selected_option = st.sidebar.selectbox("Pilih Berita:", ["Berita Utama", "Berita Terkait 1", "Berita Terkait 2", "Berita Terkait 3"])

    # Tampilkan berita yang dipilih
    if 'Berita Utama' in selected_option:
        entry = feed.entries[0]
        thumbnail_url = get_news_thumbnail(entry.link)
        article_text = get_article_text(entry.link)
        if thumbnail_url:
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                    <img src="{thumbnail_url}" alt="Thumbnail" style="max-width: 600px; max-height: 400px; margin-bottom: 10px;">
                    <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{entry.link}' target='_blank'>{entry.title}</a></h4>
                    <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(entry.published)}</p>
                    <p style='font-size: 12px;'>Sumber: {entry.source.title}</p>
                    <p style='font-size: 14px;'>{article_text}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    elif 'Berita Terkait' in selected_option:
        # Ambil berita terkait yang dipilih
        entry = feed.entries[0]
        summaries = BeautifulSoup(entry.summary, 'html.parser').find_all('a')[1:4]
        selected_summary = summaries[int(selected_option[-1]) - 1]
        link = selected_summary.get('href')
        title = selected_summary.get_text(strip=True)
        source = selected_summary.find_next('font').get_text(strip=True)

        thumbnail_url_related = get_news_thumbnail(link)
        article_text_related = get_article_text(link)

        if thumbnail_url_related:
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                    <img src="{thumbnail_url_related}" alt="Thumbnail" style="max-width: 600px; max-height: 400px; margin-bottom: 10px;">
                    <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{link}' target='_blank'>{title}</a></h4>
                    <p style='font-size: 12px; margin-bottom: 5px;'>x jam yang lalu</p>
                    <p style='font-size: 12px; margin-bottom: 5px;'>Sumber: {source}</p>
                    <p style='font-size: 14px;'>{article_text_related}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()

import streamlit as st
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

import requests
from bs4 import BeautifulSoup

def get_news_thumbnail(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Coba cari thumbnail menggunakan tag 'meta'
        thumbnail_tag = soup.find('meta', property='og:image')
        if thumbnail_tag:
            return thumbnail_tag.get('content')

        # Jika tidak ditemukan, coba cari menggunakan tag dan class lain
        thumbnail_tag = soup.find('img', class_='imgfull') or soup.find('img', class_='your-other-class')
        if thumbnail_tag:
            return thumbnail_tag.get('src')

        # Tambahkan tag atau class lain yang sesuai dengan struktur website tertentu

        return None
    else:
        print(f"Error: {response.status_code}")
        return None

def get_news_list(rss_url, num_entries=10):
    feed = feedparser.parse(rss_url)
    entries = feed.entries[:num_entries]
    return entries

def display_news_sidebar(entries):
    st.sidebar.title("Pilih Berita Utama")
    selected_option = st.sidebar.radio("Berita Utama:", entries)
    return selected_option

def display_news_main(entry):
    thumbnail_url = get_news_thumbnail(entry.link)
    article_text = get_news_article(entry.link)
    if thumbnail_url:
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                <img src="{thumbnail_url}" alt="Thumbnail" style="max-width: 600px; max-height: 400px; margin-bottom: 10px;">
                <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{entry.link}' target='_blank'>{entry.title}</a></h4>
                <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(entry.published)}</p>
                <p style='font-size: 12px;'>Sumber: {entry.source.title}</p>
                <p style='font-size: 14px; margin-top: 10px;'><strong>Teks Artikel:</strong></p>
                <p style='font-size: 12px;'>{article_text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # Jika thumbnail tidak ditemukan, tampilkan berita tanpa thumbnail
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{entry.link}' target='_blank'>{entry.title}</a></h4>
                <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(entry.published)}</p>
                <p style='font-size: 12px;'>Sumber: {entry.source.title}</p>
                <p style='font-size: 14px; margin-top: 10px;'><strong>Teks Artikel:</strong></p>
                <p style='font-size: 12px;'>{article_text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

def display_related_news(entries):
    st.markdown("<h2>Berita Terkait</h2>", unsafe_allow_html=True)
    for idx, entry in enumerate(entries, start=1):
        thumbnail_url_related = get_news_thumbnail(entry.link)
        if thumbnail_url_related:
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                    <img src="{thumbnail_url_related}" alt="Thumbnail" style="max-width: 200px; max-height: 150px; margin-bottom: 10px;">
                    <h4 style='font-size: 14px; margin-bottom: 5px;'><a href='{entry.link}' target='_blank'>{entry.title}</a></h4>
                    <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(entry.published)}</p>
                    <p style='font-size: 12px;'>Sumber: {entry.source.title}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

def get_news_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Cari elemen-elemen yang berisi teks artikel dari tag <div>
        div_elements = soup.find_all('div', class_='wrap__article-detail-content post-content')
        contentx_elements = soup.find_all('div', id='cke_pastebin')
        cnn = soup.find_all('div', class_='detail-text')
        detik = soup.find_all('div', class_='detail__body')
        cnbc = soup.find_all('div', class_='detail_text')
        republika = soup.find_all('div', class_='article-content')
        liputan6 = soup.find_all('div', class_='read-page--content')
        tbnews = soup.find_all('div', class_='mt-3')
        kompas = soup.find_all('div', class_='read__content')

        # Gabungkan elemen-elemen tersebut
        all_elements = div_elements + contentx_elements + cnn + detik + cnbc + republika + liputan6 + tbnews + kompas

        # Gabungkan teks dari elemen-elemen yang telah difilter
        article_text = ' '.join(element.get_text() for element in all_elements)

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
    entries = get_news_list(rss_url)

    selected_option = display_news_sidebar(entries)
    selected_entry = next(entry for entry in entries if entry.title == selected_option)

    display_news_main(selected_entry)

    # Ambil berita terkait dari berita utama yang dipilih
    related_entries = selected_entry.entries[1:5] if len(selected_entry.entries) > 1 else []
    display_related_news(related_entries)

if __name__ == "__main__":
    main()

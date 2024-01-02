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

        thumbnail_tag = soup.find('meta', property='og:image')
        if thumbnail_tag:
            return thumbnail_tag.get('content')

        thumbnail_tag = soup.find('img', class_='imgfull') or soup.find('img', class_='your-other-class')
        if thumbnail_tag:
            return thumbnail_tag.get('src')

        return None
    else:
        print(f"Error: {response.status_code}")
        return None

def get_news_article(url, min_sentence_length=20):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        p_elements = soup.find_all('p')
        div_elements = soup.find_all('div', class_='wrap__article-detail-content post-content')
        contentx_elements = soup.find_all('div', id='cke_pastebin')
        all_elements = p_elements + div_elements + contentx_elements

        filtered_elements = [element for element in all_elements if len(element.get_text().split()) >= min_sentence_length]

        article_text = ' '.join(element.get_text() for element in filtered_elements)

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

def tampilkan_berita_terkait(berita_utama):
    st.markdown(
        f"""
        <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
            <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{berita_utama["link"]}' target='_blank'>{berita_utama["title"]}</a></h4>
            <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(berita_utama["published_time"])}</p>
            <p style='font-size: 12px;'>Sumber: {berita_utama["source_title"]}</p>
            <p style='font-size: 14px; margin-top: 10px;'><strong>Teks Artikel:</strong></p>
            <p style='font-size: 12px;'>{berita_utama["article_text"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h3>Berita Terkait:</h3>", unsafe_allow_html=True)

    # Ambil berita terkait dari sumber lain, misalnya dengan feedparser lagi
    rss_url_related = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed_related = feedparser.parse(rss_url_related)

    for entry_related in feed_related.entries:
        thumbnail_url_related = get_news_thumbnail(entry_related.link)
        article_text_related = get_news_article(entry_related.link)

        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{entry_related.link}' target='_blank'>{entry_related.title}</a></h4>
                <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(entry_related.published)}</p>
                <p style='font-size: 12px;'>Sumber: {entry_related.source.title}</p>
                <p style='font-size: 14px; margin-top: 10px;'><strong>Teks Artikel:</strong></p>
                <p style='font-size: 12px;'>{article_text_related}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

def main():
    st.set_page_config(layout="wide")
    st.title("Contoh Aja")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    list_berita_utama = []

    for entry in feed.entries:
        thumbnail_url = get_news_thumbnail(entry.link)
        article_text = get_news_article(entry.link)

        list_berita_utama.append({
            "title": entry.title,
            "link": entry.link,
            "thumbnail_url": thumbnail_url,
            "article_text": article_text,
            "published_time": entry.published,
            "source_title": entry.source.title
        })

    for berita in list_berita_utama:
        if st.button(berita["title"]):
            tampilkan_berita_terkait(berita)

if __name__ == "__main__":
    main()

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
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                    <img src="{berita['thumbnail_url']}" alt="Thumbnail" style="max-width: 600px; max-height: 400px; margin-bottom: 10px;">
                    <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{berita['link']}' target='_blank'>{berita['title']}</a></h4>
                    <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(berita['published_time'])}</p>
                    <p style='font-size: 12px;'>Sumber: {berita['source_title']}</p>
                    <p style='font-size: 14px; margin-top: 10px;'><strong>Teks Artikel:</strong></p>
                    <p style='font-size: 12px;'>{berita['article_text']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()

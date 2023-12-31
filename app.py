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
    st.title("Headline")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    # Sidebar untuk dropdown
    selected_option = st.sidebar.selectbox("Pilih Berita Utama:", [entry.title for entry in feed.entries])

    # Tampilkan berita yang dipilih
    selected_entry = next((entry for entry in feed.entries if entry.title == selected_option), None)
    if selected_entry:
        thumbnail_url = get_news_thumbnail(selected_entry.link)
        article_text = get_news_article(selected_entry.link)
        if thumbnail_url:
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                    <img src="{thumbnail_url}" alt="Thumbnail" style="max-width: 600px; max-height: 400px; margin-bottom: 10px;">
                    <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{selected_entry.link}' target='_blank'>{selected_entry.title}</a></h4>
                    <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(selected_entry.published)}</p>
                    <p style='font-size: 12px;'>Sumber: {selected_entry.source.title}</p>
                    <p style='font-size: 14px; margin-top: 10px;'><strong>Teks Artikel:</strong></p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # Jika thumbnail tidak ditemukan
            selected_entry = next((entry for entry in feed.entries if entry.title != selected_option), None)
    else:
        st.warning("Berita tidak ditemukan.")

    # Tampilkan berita terkait di bawah berita utama
    st.title("Berita terkait")
    if selected_entry:
        summaries = BeautifulSoup(selected_entry.summary, 'html.parser').find_all('a')[1:5]

        for i, summary in enumerate(summaries):
            link = summary.get('href')
            title = summary.get_text(strip=True)
            source = summary.find_next('font').get_text(strip=True)

            try:
                thumbnail_url_related = get_news_thumbnail(link)
                article_text_related = get_news_article(link)
            except requests.exceptions.SSLError as ssl_error:
                print(f"Error accessing related news {link}: {ssl_error}")
                continue  # Skip to the next iteration if an error occurs

            if thumbnail_url_related:
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                        <img src="{thumbnail_url_related}" alt="Thumbnail" style="max-width: 300px; max-height: 200px; margin-bottom: 10px;">
                        <h4 style='font-size: 14px; margin-bottom: 5px;'><a href='{link}' target='_blank'>{title}</a></h4>
                        <p style='font-size: 10px; margin-bottom: 5px;'>x jam yang lalu</p>
                        <p style='font-size: 10px; margin-bottom: 5px;'>Sumber: {source}</p>
                        <p style='font-size: 12px; margin-top: 10px;'><strong>Teks Artikel:</strong></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                # Jika thumbnail tidak ditemukan
                continue

if __name__ == "__main__":
    main()

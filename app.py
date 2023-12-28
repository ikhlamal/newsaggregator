import streamlit as st
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

def get_news_thumbnail(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Coba cari thumbnail menggunakan tag 'meta'
        thumbnail_tag = soup.find('meta', property='og:image')
        if thumbnail_tag:
            thumbnail_url = thumbnail_tag.get('content')

            # Coba ambil teks artikel
            article_content = get_news_article(url)

            return thumbnail_url, article_content

        # Jika tidak ditemukan, coba cari menggunakan tag 'img' dengan class 'imgfull'
        thumbnail_tag = soup.find('img', class_='imgfull')
        if thumbnail_tag:
            thumbnail_url = thumbnail_tag.get('src')

            # Coba ambil teks artikel
            article_content = get_news_article(url)

            return thumbnail_url, article_content

        # Tambahkan tag lain yang sesuai dengan struktur website tertentu

    else:
        print(f"Error: {response.status_code}")
        return None, None

def get_news_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Variasi tag untuk mencari teks artikel, tambahkan sesuai kebutuhan
        article_tags = ['div', 'section', 'main']

        for tag in article_tags:
            article_content = soup.find(tag)
            if article_content:
                return article_content.get_text(separator='\n')
        
        # Tambahkan tag lain yang sesuai dengan struktur website tertentu

        return None
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
    if 'Berita Utama' in selected_option and feed.entries:
        entry = feed.entries[0]
        thumbnail_url, article_content = get_news_thumbnail(entry.link)
        if thumbnail_url:
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                    <img src="{thumbnail_url}" alt="Thumbnail" style="max-width: 600px; max-height: 400px; margin-bottom: 10px;">
                    <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{entry.link}' target='_blank'>{entry.title}</a></h4>
                    <p style='font-size: 12px; margin-bottom: 5px;'>{format_time_difference(entry.published)}</p>
                    <p style='font-size: 12px;'>Sumber: {entry.source.title}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Tampilkan teks artikel
            if article_content:
                st.markdown(
                    f"""
                    <div style="margin-top: 20px;">
                        <h3>Teks Artikel:</h3>
                        <p>{article_content}</p>
                    </div>
                    """
                )
    elif 'Berita Terkait' in selected_option and len(feed.entries) > 1:
        # Ambil berita terkait yang dipilih
        entry = feed.entries[0]
        summaries = BeautifulSoup(entry.summary, 'html.parser').find_all('a')[1:4]
        selected_summary = summaries[int(selected_option[-1]) - 1] if len(summaries) >= int(selected_option[-1]) else None

        if selected_summary:
            link = selected_summary.get('href')
            title = selected_summary.get_text(strip=True)
            source = selected_summary.find_next('font').get_text(strip=True)

            thumbnail_url_related, article_content_related = get_news_thumbnail(link)

            if thumbnail_url_related:
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; text-align: left; margin-bottom: 10px;">
                        <img src="{thumbnail_url_related}" alt="Thumbnail" style="max-width: 600px; max-height: 400px; margin-bottom: 10px;">
                        <h4 style='font-size: 16px; margin-bottom: 5px;'><a href='{link}' target='_blank'>{title}</a></h4>
                        <p style='font-size: 12px; margin-bottom: 5px;'>x jam yang lalu</p>
                        <p style='font-size: 12px; margin-bottom: 5px;'>Sumber: {source}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Tampilkan teks artikel
                if article_content_related:
                    st.markdown(
                        f"""
                        <div style="margin-top: 20px;">
                            <h3>Teks Artikel:</h3>
                            <p>{article_content_related}</p>
                        </div>
                        """
                    )
            else:
                st.warning("Thumbnail berita terkait tidak dapat ditemukan.")
        else:
            st.warning("Berita terkait tidak ditemukan.")

if __name__ == "__main__":
    main()

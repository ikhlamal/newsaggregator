def main():
    st.set_page_config(layout="wide")
    st.title("Headline")

    rss_url = 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtbGtHZ0pKUkNnQVAB?hl=id&gl=ID&ceid=ID%3Aid&oc=11'
    feed = feedparser.parse(rss_url)

    # Membuat daftar judul berita utama yang memiliki thumbnail
    news_with_thumbnail = [entry.title for entry in feed.entries if get_news_thumbnail(entry.link)]

    # Sidebar untuk dropdown hanya menampilkan berita utama dengan thumbnail
    selected_option = st.sidebar.selectbox("Pilih Berita Utama:", news_with_thumbnail)

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
            st.warning("Berita tidak memiliki thumbnail.")

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

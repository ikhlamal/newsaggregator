import streamlit as st

def blog_post(thumbnail_url, title, source):
    st.markdown(f"### {title}")
    st.image(thumbnail_url, width=200)
    st.write(f"Source: {source}")

def twitter_tweet(tweet_url):
    st.markdown(f'<iframe src="{tweet_url}" width="500" height="300" frameborder="0"></iframe>', unsafe_allow_html=True)

def main():
    st.title("Tampilan Blog dan Tweet")

    # Blog Post
    st.sidebar.markdown("### Blog Post")
    blog_thumbnail_url = st.sidebar.text_input("Thumbnail URL:", "https://pluang-production-financial-content-input.s3.ap-southeast-1.amazonaws.com/production/2023/07/lk6kaj4tyleh4wucwar%3Aopenai.jpg")
    blog_title = st.sidebar.text_input("Title:", "AI Advancements in 2023")
    blog_source = st.sidebar.text_input("Source:", "ChatGPT")
    if st.sidebar.button("Publish Blog Post"):
        blog_post(blog_thumbnail_url, blog_title, blog_source)

    # Twitter Tweet
    st.sidebar.markdown("### Twitter Tweet")
    tweet_url = st.sidebar.text_input("Tweet URL:", "https://twitter.com/CNNIndonesia/status/1754454280558485924")
    if st.sidebar.button("Publish Tweet"):
        twitter_tweet(tweet_url)

if __name__ == "__main__":
    main()

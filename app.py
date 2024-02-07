import streamlit as st

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=500, height=400)

def main():
    st.title("Aplikasi Tweet Viewer")

    # List tweet untuk kelompok 1
    tweets_group_1 = [
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 1A</p>&mdash; User1 (@user1) 
        <a href="https://twitter.com/user1/status/1?ref_src=twsrc%5Etfw">
        January 1, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 2A</p>&mdash; User2 (@user2) 
        <a href="https://twitter.com/user2/status/2?ref_src=twsrc%5Etfw">
        January 2, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 3A</p>&mdash; User3 (@user3) 
        <a href="https://twitter.com/user3/status/3?ref_src=twsrc%5Etfw">
        January 3, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        '''
    ]

    # List tweet untuk kelompok 2
    tweets_group_2 = [
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 1B</p>&mdash; User4 (@user4) 
        <a href="https://twitter.com/user4/status/4?ref_src=twsrc%5Etfw">
        January 4, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 2B</p>&mdash; User5 (@user5) 
        <a href="https://twitter.com/user5/status/5?ref_src=twsrc%5Etfw">
        January 5, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ''',
        '''
        <blockquote class="twitter-tweet" data-media-max-width="560">
        <p lang="in" dir="ltr">Tweet 3B</p>&mdash; User6 (@user6) 
        <a href="https://twitter.com/user6/status/6?ref_src=twsrc%5Etfw">
        January 6, 2024</a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        '''
    ]

    # Inisialisasi index tweet saat ini untuk masing-masing kelompok
    current_tweet_index_group_1 = 0
    current_tweet_index_group_2 = 0

    # Menampilkan tweet untuk kelompok 1
    st.header("Kelompok 1")
    with st.expander("Tweet Viewer 1", expanded=True):
        col1_1, col2_1, col3_1 = st.columns([1, 8, 1])
        if col1_1.button("⬅️") and current_tweet_index_group_1 > 0:
            current_tweet_index_group_1 -= 1
        elif col3_1.button("➡️") and current_tweet_index_group_1 < len(tweets_group_1) - 1:
            current_tweet_index_group_1 += 1
        show_tweet(tweets_group_1[current_tweet_index_group_1])

    # Menampilkan tweet untuk kelompok 2
    st.header("Kelompok 2")
    with st.expander("Tweet Viewer 2", expanded=True):
        col1_2, col2_2, col3_2 = st.columns([1, 8, 1])
        if col1_2.button("⬅️") and current_tweet_index_group_2 > 0:
            current_tweet_index_group_2 -= 1
        elif col3_2.button("➡️") and current_tweet_index_group_2 < len(tweets_group_2) - 1:
            current_tweet_index_group_2 += 1
        show_tweet(tweets_group_2[current_tweet_index_group_2])

if __name__ == "__main__":
    main()

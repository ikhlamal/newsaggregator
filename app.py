import streamlit as st

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=500, height=400)

def main():
    st.title("Aplikasi Tweet Viewer")

    # List tweet
    tweets_group = [
        [ # Kelompok 1
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 1</p>&mdash; User1 (@user1) 
            <a href="https://twitter.com/user1/status/1?ref_src=twsrc%5Etfw">
            January 1, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            ''',
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 2</p>&mdash; User2 (@user2) 
            <a href="https://twitter.com/user2/status/2?ref_src=twsrc%5Etfw">
            January 2, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            ''',
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 3</p>&mdash; User3 (@user3) 
            <a href="https://twitter.com/user3/status/3?ref_src=twsrc%5Etfw">
            January 3, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            '''
        ],
        [ # Kelompok 2
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 4</p>&mdash; User4 (@user4) 
            <a href="https://twitter.com/user4/status/4?ref_src=twsrc%5Etfw">
            January 4, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            ''',
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 5</p>&mdash; User5 (@user5) 
            <a href="https://twitter.com/user5/status/5?ref_src=twsrc%5Etfw">
            January 5, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            ''',
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 6</p>&mdash; User6 (@user6) 
            <a href="https://twitter.com/user6/status/6?ref_src=twsrc%5Etfw">
            January 6, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            '''
        ],
        [ # Kelompok 3
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 7</p>&mdash; User7 (@user7) 
            <a href="https://twitter.com/user7/status/7?ref_src=twsrc%5Etfw">
            January 7, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            ''',
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 8</p>&mdash; User8 (@user8) 
            <a href="https://twitter.com/user8/status/8?ref_src=twsrc%5Etfw">
            January 8, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            ''',
            '''
            <blockquote class="twitter-tweet" data-media-max-width="560">
            <p lang="in" dir="ltr">Tweet 9</p>&mdash; User9 (@user9) 
            <a href="https://twitter.com/user9/status/9?ref_src=twsrc%5Etfw">
            January 9, 2024</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            '''
        ]
    ]

    # Menampilkan kelompok tweet
    st.header("Tweet")
    col1, col2, col3 = st.columns(3)
    for tweets in tweets_group:
        for tweet in tweets:
            with col1:
                show_tweet(tweet)
                col1.empty()

if __name__ == "__main__":
    main()

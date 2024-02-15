# import streamlit as st
# import pandas as pd
# import os
# import urllib.parse


# def show_tweet(tweet_html):
#     st.components.v1.html(tweet_html, width=300, height=550, scrolling=True)

# def format_tweet(row):
#     tweet_html = f'''
#         <blockquote class="twitter-tweet" data-media-max-width="300">
#         <a href={row['tweet_url']}></a></blockquote>
#         <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
#     '''
#     return tweet_html

# def main():
#     st.set_page_config(layout="centered")
#     csv_files = ["csv1.csv", "csv2.csv"]
    
#     # Filter CSV files that exist
#     existing_csv_files = [csv_file for csv_file in csv_files if os.path.exists(csv_file)]

#     if len(existing_csv_files) == 0:
#         st.error("Tidak ada file CSV yang ditemukan.")
#         return

#     # Menyimpan nilai current_tweet_index di session_state
#     for i in range(len(existing_csv_files)):
#         key = f'current_tweet_index{i+1}'
#         if key not in st.session_state:
#             st.session_state[key] = 0
#     with st.expander("***:red[Populer]*** \u2014 Pendukung Minta Prabowo dan Titiek Soeharto Rujuk, Ekspresi Didit Disorot", expanded=False):
        # num_cols = min(len(existing_csv_files), 2)
    
        # # Membagi layar menjadi dua baris dua kolom
        # for i in range(0, len(existing_csv_files), num_cols):
        #     cols = st.columns(num_cols)
        #     for j in range(num_cols):
        #         index = i + j
        #         if index < len(existing_csv_files):
        #             with cols[j]:
        #                 csv_file = existing_csv_files[index]
#                         df = pd.read_csv(csv_file)
#                         if df.empty:
#                             st.error(f"Tweet dari berita ke-{index+1} kosong.")
#                             continue
    
#                         # List tweet
#                         tweets = [format_tweet(row) for index, row in df.iterrows()]
    
#                         with st.container(height=650, border=True):
#                             col7, col8, col9 = st.columns([1] * 3)
#                             with col7:
#                                 if st.session_state[f'current_tweet_index{index+1}'] > 0:
#                                     if st.button("⬅️", key=f"left{index+1}"):
#                                         st.session_state[f'current_tweet_index{index+1}'] -= 1
#                                 else:
#                                     st.button("⬅️", key=f"left{index+1}")
#                             with col8:
#                                 if st.session_state[f'current_tweet_index{index+1}'] < len(tweets) - 1:
#                                     if st.button("➡️", key=f"right{index+1}"):
#                                         st.session_state[f'current_tweet_index{index+1}'] += 1
#                                 else:
#                                      st.button("➡️", key=f"right{index+1}")
#                             with col9:
#                                 if index == 0:
#                                     st.write("🙂:", len(df))
#                                 elif index == 1:
#                                     st.write("😡:", len(df)) 
#                             # Menampilkan tweet yang baru setelah klik tombol
#                             show_tweet(tweets[st.session_state[f'current_tweet_index{index+1}']])

# if __name__ == "__main__":
#     main()

import streamlit as st
import pandas as pd
import os
import urllib.parse

def show_tweet(tweet_html):
    st.components.v1.html(tweet_html, width=300, height=550, scrolling=True)

def format_tweet(row):
    tweet_html = f'''
        <blockquote class="twitter-tweet" data-media-max-width="300">
        <a href={row['tweet_url']}></a></blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    '''
    return tweet_html

def main():
    st.set_page_config(layout="centered")
    csv_files = ["csv1.csv", "csv2.csv", "csv3.csv", "csv4.csv", "csv5.csv", "csv6.csv"]
    
    # Filter CSV files that exist
    existing_csv_files = [csv_file for csv_file in csv_files if os.path.exists(csv_file)]

    if len(existing_csv_files) == 0:
        st.error("Tidak ada file CSV yang ditemukan.")
        return

    # Menyimpan nilai current_tweet_index di session_state
    for i in range(len(existing_csv_files)):
        key = f'current_tweet_index{i+1}'
        if key not in st.session_state:
            st.session_state[key] = 0

    # Judul dan jumlah tweet untuk setiap pasangan CSV
    titles_and_counts = [
        ("***:red[Populer]*** \u2014 Pendukung Minta Prabowo dan Titiek Soeharto Rujuk, Ekspresi Didit Disorot", ["csv1.csv", "csv2.csv"]),
        ("***:red[Populer]*** \u2014 Judul CSV3", ["csv3.csv", "csv4.csv"]),
        ("***:red[Populer]*** \u2014 Judul CSV3", ["csv5.csv", "csv6.csv"]) # Ganti judul dan nama file sesuai dengan kebutuhan Anda
    ]

    for title, csv_pair in titles_and_counts:
        with st.expander(title, expanded=False):
            num_cols = len(csv_pair)
    
            # Membagi layar menjadi baris dan kolom sesuai dengan jumlah file CSV
            cols = st.columns(num_cols)
            for j, csv_file in enumerate(csv_pair):
                with cols[j]:
                    df = pd.read_csv(csv_file)
                    if df.empty:
                        st.error(f"Tweet dari file {csv_file} kosong.")
                        continue

                    # List tweet
                    tweets = [format_tweet(row) for index, row in df.iterrows()]

                    with st.container(height=650, border=True):
                        col7, col8, col9 = st.columns([1] * 3)
                        with col7:
                            if st.session_state[f'current_tweet_index{j+1}'] > 0:
                                if st.button("⬅️", key=f"left{j+1}"):
                                    st.session_state[f'current_tweet_index{j+1}'] -= 1
                            else:
                                st.button("⬅️", key=f"left{j+1}")
                        with col8:
                            if st.session_state[f'current_tweet_index{j+1}'] < len(tweets) - 1:
                                if st.button("➡️", key=f"right{j+1}"):
                                    st.session_state[f'current_tweet_index{j+1}'] += 1
                            else:
                                st.button("➡️", key=f"right{j+1}")
                        with col9:
                                if j == 0:
                                    st.write("🙂:", len(df))
                                elif j == 1:
                                    st.write("😡:", len(df)) 
                        # Menampilkan tweet yang baru setelah klik tombol
                        show_tweet(tweets[st.session_state[f'current_tweet_index{j+1}']])

if __name__ == "__main__":
    main()


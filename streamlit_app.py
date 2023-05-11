import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/irchamali.svg?logo=github&style=social)](https://github.com/irchamali)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('img/tiunusia.png'))

st.header('Teknik Informatika')

st.info('Program Studi Teknik Informatika Universitas Nahdlatul Ulama Indonesia (TI UNUSIA) menyelenggarakan pengajaran di kampus A Jakarta dan kampus B Bogor. Tersedia sejumlah beasiswa yang bisa diakses seperti beasiswa influencer, prestasi, NU leader future, hingga KIP Kuliah dari pemerintah.')

icon_size = 20

# st_button('linkedin', 'https://www.linkedin.com/in/ircham-ali/', 'Follow me on LinkedIn', icon_size)
st_button('youtube', 'https://youtu.be/zKZt0GUluaI', 'Podcast x UnusiaTv', icon_size)
st_button('youtube', 'https://www.youtube.com/@unusialabs', 'YouTube Channel', icon_size)
st_button('medium', 'https://pmb.unusia.ac.id/', 'Yuk Join TI UNUSIA!', icon_size)
st_button('facebook', 'https://facebook.com/teknikinformatikaunusia/', 'Facebook Laman', icon_size)
st_button('instagram', 'https://instagram.com/teknikinformatikaunusia/', 'Liat Instagram', icon_size)
st_button('github', 'https://github.com/unusialabs/', 'Repo GitHub', icon_size)
st_button('twitter', 'https://twitter.com/ti_unusia/', 'Baca Twitter', icon_size)

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

st_button('web', 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQlPrhccpFftRaI1ynIWWkSqmMaC3BBgLSE38Tf1Y9VPemebzOEpPFYmm6BINDdu52HZHe9LHUAx_TN/pubhtml?gid=1583299384&single=true', 'Publikasi Mahasiswa TI', icon_size)
st_button('youtube', 'https://youtu.be/zKZt0GUluaI', 'Podcast x UnusiaTv', icon_size)
st_button('pmb', 'https://pmb.unusia.ac.id/', 'Yuk Join TI UNUSIA !', icon_size)
st_button('web2', 'https://ti.unusia.ac.id/', 'Web Resmi TI UNUSIA', icon_size)
st_button('youtube', 'https://www.youtube.com/@unusialabs', 'YouTube Channel', icon_size)
st_button('facebook', 'https://facebook.com/teknikinformatikaunusia/', 'Facebook Laman', icon_size)
st_button('instagram', 'https://instagram.com/teknikinformatikaunusia/', 'Liat Instagram', icon_size)
st_button('github', 'https://github.com/unusialabs/', 'Repo GitHub', icon_size)
st_button('twitter', 'https://twitter.com/ti_unusia/', 'Baca Twitter', icon_size)

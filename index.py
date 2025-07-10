import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🎬 Daftar Film Pilihan dengan Card")

films = [
    {"title": "The Shawshank Redemption", "year": 1994, "genre": "Drama",
     "desc": "Dua pria menjalin persahabatan di penjara.",
     "banner": "https://images-na.ssl-images-amazon.com/images/I/51NiGlapXlL._AC_.jpg"},
    {"title": "The Godfather", "year": 1972, "genre": "Crime",
     "desc": "Kisah keluarga mafia di Amerika.",
     "banner": "https://play-lh.googleusercontent.com/g9HZL3xpscEkEqDhbjMBHJP10CChWfOChNWWtqBJ0tKHxDBar__FSCmaMqq0HH7E_F4-OjvGauwVUYcVUQ"},
    {"title": "Inception", "year": 2010, "genre": "Sci-Fi",
     "desc": "Penjelajahan dunia mimpi oleh pencuri profesional.",
     "banner": "https://m.media-amazon.com/images/M/MV5BMjExMjkwNTQ0Nl5BMl5BanBnXkFtZTcwNTY0OTk1Mw@@._V1_.jpg"},
    {"title": "Parasite", "year": 2019, "genre": "Thriller",
     "desc": "Keluarga miskin menyusup ke rumah orang kaya.",
     "banner": "https://cdn.rri.co.id/berita/Kendari/o/1734761587860-Parasite/2q3w46pkbqr038l.jpeg"},
    {"title": "Interstellar", "year": 2014, "genre": "Sci-Fi",
     "desc": "Perjalanan ruang angkasa mencari planet baru.",
     "banner": "https://m.media-amazon.com/images/I/91UMpWgj05L._UF894,1000_QL80_.jpg"},
]

df = pd.DataFrame(films)

search = st.text_input("🔍 Cari film berdasarkan judul")
genre_filter = st.multiselect(
    "Filter genre", options=df['genre'].unique(), default=df['genre'].unique()
)

filtered = df[
    df['title'].str.contains(search, case=False) &
    df['genre'].isin(genre_filter)
]

for _, film in filtered.iterrows():
    with st.container():
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(film['banner'], use_container_width=True)
        with cols[1]:
            st.markdown(f"### **{film['title']} ({film['year']})**")
            st.caption(f"Genre: {film['genre']}")
            st.write(film['desc'])
        st.markdown("---")

import pandas as pd
import streamlit as st

# Carregando o DataFrame
df = pd.read_csv("genshin_characters_v1.csv")
regions = ["Mondstadt", "Inazuma", "Liyue", "Sumeru", "Fontaine", "Natlan", "Snezhnaya"]

# Função para listar personagens por região
def characters_per_region(region):
    region_cont = 0
    characters = []

    for i in range(94):
        result = df.at[i, 'region']
        if result == region:
            characters.append(df.at[i, 'character_name'])
            region_cont += 1

    return characters, region_cont

# Função para traduzir a arma
def traduzir_arma(arma):
    armas = {
        "espada": "Sword",
        "lança": "Polearm",
        "lanca": "Polearm",
        "arco": "Bow",
        "catalisador": "Catalyst",
        "espadão": "Claymore",
        "espadao": "Claymore"
    }
    return armas.get(arma.lower().strip(), arma.capitalize())


# Função para contar personagens por classificação de estrelas
def star_rating():
    four_stars = 0
    five_stars = 0
    for i in range(94):
        result = df.at[i, 'star_rarity']
        if result == 4:
            four_stars += 1
        else:
            five_stars += 1
    return four_stars, five_stars

# Função para verificar personagens por visão
def check_vision(vision):
    characters = []
    for i in range(94):
        result = df.at[i, 'vision']
        if result == vision.capitalize():
            characters.append(df.at[i, 'character_name'])
    return characters

# Função para verificar personagens por tipo de arma
def check_weapon(weapon):
    characters = []
    for i in range(94):
        result = df.at[i, 'weapon_type']
        if result == weapon.capitalize():
            characters.append(df.at[i, 'character_name'])
    return characters

# Função para verificar personagens por visão e arma
def check_weapon_vision(vision, weapon):
    characters = []
    translated_weapon = traduzir_arma(weapon)  # Traduzindo a arma corretamente
    for i in range(94):
        result_vision = df.at[i, 'vision']
        result_weapon = df.at[i, 'weapon_type']
        if result_vision == vision.capitalize() and result_weapon == translated_weapon:
            characters.append(df.at[i, 'character_name'])
    return characters


# Interface do Streamlit
st.title("App de Personagens do Genshin Impact")

# Menu de opções
menu = ["Personagens por Região", "Classificação por Estrelas", "Verificar por Visão e Arma", "Verificar por Arma", "Verificar por Visão", "Sair"]
choice = st.sidebar.selectbox("Menu", menu)

# Funcionalidades com base na escolha do usuário
if choice == "Personagens por Região":
    region = st.selectbox("Escolha uma região", regions)
    characters, count = characters_per_region(region)
    st.write(f"Existem {count} personagens em {region}:")
    st.write(characters)

elif choice == "Classificação por Estrelas":
    four_stars, five_stars = star_rating()
    st.write(f"Existem {four_stars} personagens com 4 estrelas.")
    st.write(f"Existem {five_stars} personagens com 5 estrelas.")

elif choice == "Verificar por Visão e Arma":
    vision = st.text_input("Digite o elemento (Visão)")
    weapon = st.text_input("Digite a arma")
    if st.button("Verificar"):
        characters = check_weapon_vision(vision, weapon)  # Verifica com arma traduzida
        if characters:
            st.write(f"Personagens com a visão {vision.capitalize()} e arma {traduzir_arma(weapon)}:")
            st.write(characters)
        else:
            st.write(f"Nenhum personagem encontrado com a visão {vision.capitalize()} e arma {traduzir_arma(weapon)}.")

elif choice == "Verificar por Arma":
    weapon = st.text_input("Digite a arma")
    if st.button("Verificar"):
        translated_weapon = traduzir_arma(weapon)  # Traduzindo a arma corretamente
        characters = check_weapon(translated_weapon)
        if characters:
            st.write(f"Personagens com a arma {translated_weapon}:")
            st.write(characters)
        else:
            st.write(f"Nenhum personagem encontrado com a arma {translated_weapon}.")

elif choice == "Verificar por Visão":
    vision = st.text_input("Digite a visão (Elemento)")
    if st.button("Verificar"):
        characters = check_vision(vision)
        st.write(characters)

elif choice == "Sair":
    st.write("Programa encerrado.")

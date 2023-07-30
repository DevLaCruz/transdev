import streamlit as st
from streamlit_ace import st_ace
import openai
import json
from utils import programming_languages, output_results, define_prompt, request, action_details, model_details



# Leer el archivo de configuración
with open("config.json") as config_file:
    config = json.load(config_file)

st.write(' ## Hola, soy Transveloper')
st.write('\n')
st.write(' ## Puedo traducir tu codigo a otros lenguajes, corregirlo o explicarlo usando GPT')
_, psw_col2, _ = st.columns([1,2,1])
OPENAI_API_KEY = config["api_key"]
debug_mode = config["debug_mode"]
max_items = config["max_items"]

_, col2, col3, _ = st.columns(4)
model = col2.selectbox(
    'Selecciona el Modelo a usar',
    ('GPT-3.5', 'GPT-4 (próximamente)'))

action = col3.selectbox(
    'Operación',
    ('Explicar', 'Traducir', 'Corregir'))

st.write('\n')
st.write('\n')

input_language = st.selectbox(
    'Entrada',
    programming_languages)

code_content = st_ace(
    placeholder="Ingresa tu código",
    language=input_language,
    theme='dracula',
    auto_update=True,
    value = "")

output_langague = st.selectbox(
    'Salida',
    options=output_results[action])

if st.button('Ejecutar'):
    openai.api_key = OPENAI_API_KEY
    prompt = define_prompt(action, input_language, code_content, output_langague)
    r = request(model_details[model], prompt)

    if action == 'Explicar':
        st.text_area(r)
    else:
        output_content = st_ace(
            value = r,
            language=output_langague,
            theme='dracula',
            readonly=True)
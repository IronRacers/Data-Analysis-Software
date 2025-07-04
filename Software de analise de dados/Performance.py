# PROJECT BY JOÃO VITOR RODRIGUES
# python -m streamlit run "C:\Users\João Vitor\Desktop\Joao Vitor Rodrigues\FACULDADE\Iron Races\Software de analise de dados\Performance.py" streamlit run Performance.py
#  ----------------------------------------------------------------------------------------------------------------------#
# LIBRARY IMPORT
# ----------------------------------------------------------------------------------------------------------------------#
import subprocess
import streamlit as st  # Streamlit library
import pandas as pd  # Pandas library is used for exporting Excel data.
from streamlit_option_menu import option_menu
from datetime import date, time
import os
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# SETUP PAGE OF STREAMLIT
# ----------------------------------------------------------------------------------------------------------------------#
st.set_page_config(
    page_title="Data Analysis - Formula Studant",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# Initialization ST.SESSION STATE
# ----------------------------------------------------------------------------------------------------------------------#
if 'selected_drivers' not in st.session_state:
    st.session_state['selected_drivers'] = ["Jenifer"]

if "Goal" not in st.session_state:
    st.session_state["Goal"] = ""

if "Planing" not in st.session_state or not isinstance(st.session_state["Planing"], pd.DataFrame):
    st.session_state["Planing"] = pd.DataFrame({
        "Description": [""],
        "Time": [""],
        "Responsible": [""],
        "Done": [False]  # <- nova coluna de checkbox
    })

if "Local" not in st.session_state:
    st.session_state["Local"] = ""
if "temp_local" not in st.session_state:
    st.session_state["temp_local"] = st.session_state["Local"]

if "general_report" not in st.session_state:
    st.session_state["general_report"] = ""

if "start_time" not in st.session_state:
    st.session_state["start_time"] = time(9, 0)
if "end_time" not in st.session_state:
    st.session_state["end_time"] = time(17, 0)
if "temp_start_time" not in st.session_state:
    st.session_state["temp_start_time"] = st.session_state["start_time"]
if "temp_end_time" not in st.session_state:
    st.session_state["temp_end_time"] = st.session_state["end_time"]
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# Update ST.SESSION STATE with value
# ----------------------------------------------------------------------------------------------------------------------#


def atualizar_goal():
    st.session_state["Goal"] = st.session_state["temp_goal"]


def atualizar_local():
    st.session_state["Local"] = st.session_state["temp_local"]


def atualizar_start_time():
    st.session_state["start_time"] = st.session_state["temp_start_time"]


def atualizar_end_time():
    st.session_state["end_time"] = st.session_state["temp_end_time"]


st.title("Software Data Analysis")
st.divider()

Colune1, Colune2 = st.columns([1, 2.5])

with Colune1:

    st.text_input(
        "Test goal:",
        key="temp_goal",
        value=st.session_state["Goal"],
        on_change=atualizar_goal
    )

    # Campo de texto para o local
    st.text_input(
        "Test location:",
        key="temp_local",
        value=st.session_state["Local"],
        on_change=atualizar_local
    )

    # ----------------------------------------------------------------------------------------------------------------------#
    # SELECTED OF THE DRIVERS
    # ----------------------------------------------------------------------------------------------------------------------#
    DriverList = ["Jenifer", "Muniz", "Rafael"]  # List of drivers
    st.session_state.selected_drivers = selected_drivers = st.multiselect(
        'Select the drivers:', DriverList, key='season_drivers', max_selections=6, default=st.session_state.selected_drivers)
    # Initializing lists to store data for the selected drivers
    results = {}

    # ----------------------------------------------------------------------------------------------------------------------#
    # SELECT DATE (DIA/MÊS/ANO)
    # ----------------------------------------------------------------------------------------------------------------------#
    # Inicializa a data, se necessário
    if "session_date" not in st.session_state:
        st.session_state["session_date"] = date.today()

    # Date input com valor inicial e salvando no session_state
    selected_date = st.date_input(
        "Select the date:",
        value=st.session_state["session_date"],
        key="date_picker"
    )

    # Atualiza session_state se houver mudança
    if selected_date != st.session_state["session_date"]:
        st.session_state["session_date"] = selected_date

     # Campos: Horário de início e término em duas colunas
    col1, col2 = st.columns(2)

    with col1:
        st.time_input(
            "Start time:",
            key="temp_start_time",
            value=st.session_state["temp_start_time"],
            on_change=atualizar_start_time
        )

    with col2:
        st.time_input(
            "End time:",
            key="temp_end_time",
            value=st.session_state["temp_end_time"],
            on_change=atualizar_end_time
        )

with Colune2:
    st.text("Test Planing:")
    # Sempre use retorno direto
    df_editado = st.data_editor(
        st.session_state["Planing"],
        num_rows="dynamic",
        use_container_width=True
    )

    # Botão que apenas sinaliza o salvamento no próximo rerun
    if st.button("💾 Confirm planing"):
        st.session_state["Planing_pending_save"] = df_editado
        st.rerun()()

    # Verifica se há alterações pendentes e atualiza
    if "Planing_pending_save" in st.session_state:
        st.session_state["Planing"] = st.session_state.pop(
            "Planing_pending_save")
        st.success("✅ Planning saved successfully!")

st.divider()
# Campo de texto ajustado para parecer mais limpo


def atualizar_relatorio():
    st.session_state["general_report"] = st.session_state["temp_relatorio"]


st.text_area(
    "General Reports:",
    key="temp_relatorio",
    value=st.session_state["general_report"],
    height=120,
    placeholder="Write...",
    on_change=atualizar_relatorio
)

st.divider()


uploaded_files = st.file_uploader(
    "Select log",
    accept_multiple_files=True
)

if uploaded_files:
    if "arquivos_carregados" not in st.session_state:
        st.session_state["arquivos_carregados"] = {}

    for file in uploaded_files:
        try:
            conteudo = file.read().decode("utf-8")
        except:
            conteudo = "<Erro ao ler arquivo como texto>"
        st.session_state["arquivos_carregados"][file.name] = conteudo

    st.success("Files loaded and saved successfully!")

st.markdown("### 📂 Uploaded files")

if "arquivos_carregados" in st.session_state and st.session_state["arquivos_carregados"]:
    arquivos = list(st.session_state["arquivos_carregados"].keys())

    for nome in arquivos:
        col1, col2, col3 = st.columns([0.05, 0.8, 0.15])

        with col1:
            st.markdown("📄")
        with col2:
            with st.expander(nome):
                st.text_area(
                    f"Conteúdo de {nome}", st.session_state["arquivos_carregados"][nome], height=200)
        with col3:
            if st.button(f"❌ Remover", key=f"remover_{nome}"):
                del st.session_state["arquivos_carregados"][nome]
                st.rerun()
else:
    st.info("No files uploaded yet.")


# # ----------------------------------------------------------------------------------------------------------------------#
# # UPLOAD FILE
# # ----------------------------------------------------------------------------------------------------------------------#
# if st.session_state.uploaded_file is None:  # Check if a file has been selected
#     uploaded_file = st.file_uploader(
#         "Choose a file of day test")  # Select the file
#     st.session_state.uploaded_file = uploaded_file  # Save the selected file
# # ----------------------------------------------------------------------------------------------------------------------#

# # ----------------------------------------------------------------------------------------------------------------------#
# # IMPORTING DATA OF EXCEL
# # ----------------------------------------------------------------------------------------------------------------------#
# if st.session_state['uploaded_file'] is not None:  # If the workbook is selected
#     with pd.ExcelFile(st.session_state['uploaded_file']) as xlsx:
#         st.session_state.Setup = df_Setup = pd.read_excel(
#             xlsx, "Setup")  # Import setup data
#         st.session_state.Tires = df_Tires = pd.read_excel(
#             # Import tires data, header works in multiindex
#             xlsx, "Tires", header=[0, 1, 2])
#         st.session_state.General_Information = df_Information = pd.read_excel(
#             xlsx, "GenaralInformation")
#         st.session_state.Timing = df_Timing = pd.read_excel(
#             xlsx, "Timing")  # Import timing data
# # ----------------------------------------------------------------------------------------------------------------------#

#     # ----------------------------------------------------------------------------------------------------------------------#
#     # SELECTED OF THE DRIVERS
#     # ----------------------------------------------------------------------------------------------------------------------#
#     DriverList = ["Jenifer", "Muniz", "Rafael"]  # List of drivers
#     st.session_state.selected_drivers = selected_drivers = st.multiselect(
#         'Select the drivers:', DriverList, key='season_drivers', max_selections=2, default=st.session_state.selected_drivers)
#     # Initializing lists to store data for the selected drivers
#     results = {}

#     # Creating columns for each driver
#     cols = st.columns(len(selected_drivers))

#     for i, driver in enumerate(selected_drivers):

#         with cols[i]:  # Using the context of the corresponding column
#             # Filtering data for the selected driver
#             Index = df_Information[df_Information['Piloto']
#                                    == driver].index.tolist()

#             if not Index:  # If the driver is not found
#                 st.write(f"The driver {
#                     driver} is not here, select another driver")
#                 continue

#             # Obtaining the laps associated with the driver
#             Lap = df_Timing.loc[Index, 'Lap'].tolist()
#             TagList = df_Timing.loc[Index, 'Tag'].tolist()
#             Time = df_Timing.loc[Index, 'Stopwatch'].tolist()
#             Feedback = df_Timing.loc[Index, 'Feedback'].tolist()

#             # Styling the DataFrame for each driver
#             df_result = pd.DataFrame({
#                 'Lap': Lap,
#                 'Lap time (s)': Time,
#                 'Feedback': Feedback,
#             })

#             # Applying style
#             styled_df = df_result.style \
#                 .format({'Lap time (s)': '{:.2f}'}) \
#                 .background_gradient(subset=['Lap time (s)'], cmap='Oranges')

#             # Converting the styled DataFrame to HTML and displaying
#             html = styled_df.to_html()
#             # Driver title
#             st.markdown(f"<h3>{driver}</h3>", unsafe_allow_html=True)
#             st.markdown(html, unsafe_allow_html=True)

#             # ----------------------------------------------------------------------------------------------------------------------#
#             # SELECTED OF THE LAP FOR EACH DRIVER
#             # ----------------------------------------------------------------------------------------------------------------------#
#             # Configurando a volta selecionada previamente, se disponível
#             if f'selected_lap_{driver}' in st.session_state:
#                 initial_lap = st.session_state[f'selected_lap_{driver}']
#             else:
#                 initial_lap = Lap[0]  # ou outro valor padrão desejado
#             selected_lap = st.session_state[f'selected_lap_{driver}'] = st.selectbox(
#                 f'Select the lap for {driver}:', Lap, index=Lap.index(initial_lap), key=f'season_lap_{driver}')

#             # Filtering the tag based on the selected lap
#             Tag = []
#             Tag = TagList[Lap.index(selected_lap)]
#             # Storing the tag in the session

#             st.session_state[f'Tag_{driver}'] = Tag

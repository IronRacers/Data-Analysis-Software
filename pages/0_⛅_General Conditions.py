#  ----------------------------------------------------------------------------------------------------------------------#
# LIBRARY IMPORT
# ----------------------------------------------------------------------------------------------------------------------#

# Import library
import streamlit as st  # Streamlit library
import pandas as pd  # Pandas library is used of export excel data.
from streamlit_option_menu import option_menu
from PIL import Image
# ----------------------------------------------------------------------------------------------------------------------#


#  ----------------------------------------------------------------------------------------------------------------------#
# Setup setting
# ----------------------------------------------------------------------------------------------------------------------#
st.title("General Conditions")
# Created mult tabs
tabs = st.tabs(["Weight Information", "External Temperatures"])

with tabs[0]:  # Weight Information – entrada manual com imagens
    Imagem_Car = Image.open('./Images/CarroBranco.png')
    Imagem_Drive = Image.open('./Images/PilotoBranca.png')
    Imagem_Fuel = Image.open('./Images/combustivelBranco.png')

    # Inicializa dicionário para armazenar os dados
    if "driver_data" not in st.session_state:
        st.session_state["driver_data"] = {}

    for i, driver in enumerate(st.session_state.selected_drivers):
        if i >= 1:
            st.divider()

        st.markdown(f"### 👤 Driver: {driver}")
        Colune1, Colune2, Colune3 = st.columns(3)

        with Colune1:
            Col1a, Col1b = st.columns([0.7, 0.3])
            with Col1a:
                car_weight = st.number_input(
                    f"Car (Kg) – {driver}",
                    min_value=0.0,
                    step=0.5,
                    value=st.session_state["driver_data"].get(
                        driver, {}).get("Car (Kg)", 0.0),
                    key=f"car_{driver}"
                )
            with Col1b:
                st.image(Imagem_Car, use_container_width=False, width=60)

        with Colune2:
            Col2a, Col2b = st.columns([0.7, 0.3])
            with Col2a:
                driver_weight = st.number_input(
                    f"Driver (Kg) – {driver}",
                    min_value=0.0,
                    step=0.5,
                    value=st.session_state["driver_data"].get(
                        driver, {}).get("Driver (Kg)", 0.0),
                    key=f"driver_{driver}"
                )
            with Col2b:
                st.image(Imagem_Drive, use_container_width=False, width=50)

        with Colune3:
            Col3a, Col3b = st.columns([0.7, 0.3])
            with Col3a:
                fuel = st.number_input(
                    f"Fuel (L) – {driver}",
                    min_value=0.0,
                    step=0.5,
                    value=st.session_state["driver_data"].get(
                        driver, {}).get("Fuel (L)", 0.0),
                    key=f"fuel_{driver}"
                )
            with Col3b:
                st.image(Imagem_Fuel, use_container_width=False, width=50)

        # ✅ Atualiza os dados no session_state com os valores atuais
        st.session_state["driver_data"][driver] = {
            "Car (Kg)": car_weight,
            "Driver (Kg)": driver_weight,
            "Fuel (L)": fuel
        }


with tabs[1]:  # External Temperatures – entrada manual com imagens
    Imagem_Track = Image.open('./Images/PistaBranca.png')
    Imagem_AirTemp = Image.open('./Images/TemperaturaBranca.png')

    # Inicializa dicionário para armazenar os dados
    if "external_temps" not in st.session_state:
        st.session_state["external_temps"] = {}

    for i, driver in enumerate(st.session_state.selected_drivers):
        if i >= 1:
            st.divider()

        st.markdown(f"### 👤 Drive: {driver}")
        Colune1, Colune2 = st.columns(2)

        with Colune1:
            Col1a, Col1b = st.columns([0.7, 0.3])
            with Col1a:
                track_temp = st.number_input(
                    f"Track temperature (℃) – {driver}",
                    min_value=-10.0,
                    max_value=100.0,
                    step=0.5,
                    value=st.session_state["external_temps"].get(
                        driver, {}).get("Track (℃)", 0.0),
                    key=f"track_temp_{driver}"
                )
            with Col1b:
                st.image(Imagem_Track, use_container_width=False, width=50)

        with Colune2:
            Col2a, Col2b = st.columns([0.7, 0.3])
            with Col2a:
                air_temp = st.number_input(
                    f"Air temperature (℃) – {driver}",
                    min_value=-10.0,
                    max_value=100.0,
                    step=0.5,
                    value=st.session_state["external_temps"].get(
                        driver, {}).get("Air (℃)", 0.0),
                    key=f"air_temp_{driver}"
                )
            with Col2b:
                st.image(Imagem_AirTemp, use_container_width=False, width=50)

        # ✅ Salva os dados no session_state
        st.session_state["external_temps"][driver] = {
            "Track (℃)": track_temp,
            "Air (℃)": air_temp
        }


# if st.session_state.uploaded_file is None:  # If the workbook is not selected
#     st.write('Seleted the WorkBook')

# if st.session_state['uploaded_file'] is not None:  # If the workbook is selected
#     st.divider()
#     Imagem_Car = Image.open('./Images/CarroBranco.png')
#     Imagem_Drive = Image.open('./Images/PilotoBranca.png')
#     Imagem_Fuel = Image.open('./Images/combustivelBranco.png')
#     Imagem_AirTemp = Image.open('./Images/TemperaturaBranca.png')
#     Imagem_Track = Image.open('./Images/PistaBranca.png')

#     # Created mult tabs
#     tabs = st.tabs(["Weight Information", "External Temperatures"])
#     with tabs[0]:  # If Weight Information
#         for i, driver in enumerate(st.session_state.selected_drivers):
#             if i >= 1:
#                 st.divider()
#             Colune1, Colune2, Colune3 = st.columns(3)

#             with Colune1:
#                 Tag = st.session_state.get(f'Tag_{driver}')

#                 Colune11, Colune12 = st.columns(2)
#                 with Colune11:
#                     st.markdown(
#                         f"""
#                                     <div style="
#                                         display: inline-block;
#                                         padding: 8px 20px;
#                                         margin-top: 0px;
#                                         background-color: #666262;
#                                         border-radius: 4px;
#                                         box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);                                    font-size: 16px;
#                                         color: #fcfcfc;
#                                         text-align: center;
#                                     ">
#                                         Drive: {
#                             st.session_state['General_Information'].loc[Tag - 1, ('Piloto')]}
#                                     </div>
#                                     """,
#                         unsafe_allow_html=True
#                     )
#                     st.write("  ")
#                     st.markdown(
#                         '<div style="margin-top: 21px;"></div>', unsafe_allow_html=True)

#                     st.markdown(
#                         f"""
#                                 <div style="
#                                     display: inline-block;
#                                     padding: 8px 20px;
#                                     margin-top: 0px;
#                                     background-color: #666262;
#                                     border-radius: 4px;
#                                     box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#                                     font-size: 16px;
#                                     color: #fcfcfc;
#                                     text-align: center;
#                                 ">
#                                     Car (Kg): {st.session_state['General_Information'].loc[Tag - 1, ('Peso carro')]}

#                                 </div>
#                                 """,
#                         unsafe_allow_html=True
#                     )
#                     with Colune12:
#                         st.write("  ")
#                         st.write("  ")
#                         st.write("  ")
#                         st.write("  ")
#                         st.image(
#                             Imagem_Car, use_column_width=False, width=70)

#             with Colune2:
#                 Colune11, Colune12 = st.columns(2)
#                 with Colune11:
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")

#                     st.markdown(
#                         f"""
#                                     <div style="
#                                         display: inline-block;
#                                         padding: 8px 20px;
#                                         margin-top: 0px;
#                                         background-color: #666262;
#                                         border-radius: 4px;
#                                         box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#                                         font-size: 16px;
#                                         color: #fcfcfc;
#                                         text-align: center;
#                                     ">
#                                         Drive (Kg): {st.session_state['General_Information'].loc[Tag - 1, ('Peso piloto')]}
#                                     </div>
#                                     """,
#                         unsafe_allow_html=True
#                     )
#                 with Colune12:
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.image(Imagem_Drive, use_column_width=False, width=50)

#             with Colune3:
#                 Colune11, Colune12 = st.columns(2)
#                 with Colune11:
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.markdown(
#                         f"""
#                                     <div style="
#                                         display: inline-block;
#                                         padding: 8px 20px;
#                                         margin-top: 0px;
#                                         background-color: #666262;
#                                         border-radius: 4px;
#                                         box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#                                         font-size: 16px;
#                                         color: #fcfcfc;
#                                         text-align: center;
#                                     ">
#                                         Fuel (L): {st.session_state['General_Information'].loc[Tag -
#                                                                                                1, ('Qnt. Comb')]}
#                                     </div>
#                                     """,
#                         unsafe_allow_html=True
#                     )

#                 with Colune12:
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.write("  ")
#                     st.image(Imagem_Fuel, use_column_width=False, width=50)
#     with tabs[1]:  # If General Information
#         Colune1, Colune2 = st.columns(2)
#         for i, driver in enumerate(st.session_state.selected_drivers):
#             if i >= 1:
#                 st.divider()
#             Colune1, Colune2 = st.columns(2)
#             Tag = st.session_state.get(f'Tag_{driver}')

#             with Colune1:
#                 Colune11, Colune12 = st.columns(2)
#                 with Colune11:
#                     st.markdown(
#                         f"""
#                                     <div style="
#                                         display: inline-block;
#                                         padding: 8px 20px;
#                                         margin-top: 0px;
#                                         background-color: #666262;
#                                         border-radius: 4px;
#                                         box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);                                    font-size: 16px;
#                                         color: #fcfcfc;
#                                         text-align: center;
#                                     ">
#                                         Drive: {
#                             st.session_state['General_Information'].loc[Tag - 1, ('Piloto')]}
#                                     </div>
#                                     """,
#                         unsafe_allow_html=True
#                     )
#                     st.write("  ")
#                     st.markdown(
#                         '<div style="margin-top: 21px;"></div>', unsafe_allow_html=True)
#                     st.markdown(
#                         f"""
#                                 <div style="
#                                     display: inline-block;
#                                     padding: 8px 20px;
#                                     margin-top: 0px;
#                                     background-color: #666262;
#                                     border-radius: 4px;
#                                     box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#                                     font-size: 16px;
#                                     color: #fcfcfc;
#                                     text-align: center;
#                                 ">
#                                     Track temperature (℃): {st.session_state['General_Information'].loc[Tag - 1, ('Temp. Pista')]}
#                                 </div>
#                                 """,
#                         unsafe_allow_html=True
#                     )
#             with Colune12:
#                 st.markdown(
#                     '<div style="margin-top: 75px;"></div>', unsafe_allow_html=True)
#                 st.image(Imagem_Track, use_column_width=False, width=50)

#             with Colune2:
#                 Colune11, Colune12 = st.columns(2)
#                 with Colune11:
#                     st.markdown(
#                         '<div style="margin-top: 79px;"></div>', unsafe_allow_html=True)
#                     st.markdown(
#                         f"""
#                                     <div style="
#                                         display: inline-block;
#                                         padding: 8px 20px;
#                                         margin-top: 0px;
#                                         background-color: #666262;
#                                         border-radius: 4px;
#                                         box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#                                         font-size: 16px;
#                                         color: #fcfcfc;
#                                         text-align: center;
#                                     ">
#                                         Air temperature (℃): {st.session_state['General_Information'].loc[Tag - 1, ('Temp. Ar')]}
#                                     </div>
#                                     """,
#                         unsafe_allow_html=True
#                     )
#                 with Colune12:
#                     st.markdown(
#                         '<div style="margin-top: 75px;"></div>', unsafe_allow_html=True)
#                     st.image(Imagem_AirTemp,
#                              use_column_width=False, width=50)

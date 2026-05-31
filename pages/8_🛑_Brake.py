#  ----------------------------------------------------------------------------------------------------------------------#
# LIBRARY IMPORT
# ----------------------------------------------------------------------------------------------------------------------#
import math

import pandas as pd  # Pandas library is used for exporting Excel data.
import plotly.graph_objects as go
import streamlit as st  # Streamlit library

# ----------------------------------------------------------------------------------------------------------------------#

G = 9.80665


def area_from_diameter_mm(diameter_mm):
    diameter_m = diameter_mm / 1000
    return math.pi * (diameter_m / 2) ** 2


def safe_divide(numerator, denominator):
    if denominator == 0:
        return 0
    return numerator / denominator


def status_from_margin(margin, tolerance=0):
    if margin >= tolerance:
        return "Aprovado"
    if margin >= -5:
        return "Atencao"
    return "Reprovado"


def style_validation_table(row):
    status = row.get("Status", "")
    if status == "Aprovado":
        return ["background-color: #173d2a; color: #d9ffe7"] * len(row)
    if status == "Atencao":
        return ["background-color: #4a3716; color: #fff0c2"] * len(row)
    if status == "Reprovado":
        return ["background-color: #4a1f1f; color: #ffd9d9"] * len(row)
    return [""] * len(row)


st.title("Brake")
st.caption("Validacao de projeto do sistema de freios - Formula SAE Iron Racers")
st.divider()

tabs = st.tabs([
    "Projeto teorico",
    "Validacao",
    "Ensaio em pista",
    "Analise de log",
])

with tabs[0]:
    st.subheader("Dados do veiculo")

    col_vehicle, col_hydraulic, col_thermal = st.columns(3)

    with col_vehicle:
        mass_kg = st.number_input("Massa com piloto (kg)", min_value=100.0, max_value=600.0, value=300.0, step=5.0)
        static_front_pct = st.slider("Distribuicao estatica dianteira (%)", 35.0, 65.0, 48.0, 0.5)
        wheelbase_m = st.number_input("Entre-eixos (m)", min_value=1.0, max_value=2.5, value=1.56, step=0.01)
        cg_height_m = st.number_input("Altura do CG (m)", min_value=0.10, max_value=0.80, value=0.30, step=0.01)
        tire_radius_m = st.number_input("Raio dinamico do pneu (m)", min_value=0.10, max_value=0.40, value=0.23, step=0.005)
        tire_mu = st.number_input("Coeficiente pneu/pista", min_value=0.40, max_value=2.50, value=1.35, step=0.05)

    with col_hydraulic:
        validation_pedal_force_n = st.number_input("Forca de pedal para validar (N)", min_value=50.0, max_value=2500.0, value=600.0, step=25.0)
        pedal_force_limit_n = st.number_input("Limite de esforco do piloto (N)", min_value=50.0, max_value=2500.0, value=900.0, step=25.0)
        pedal_ratio = st.number_input("Relacao do pedal", min_value=1.0, max_value=10.0, value=4.5, step=0.1)
        hydraulic_front_pct = st.slider("Bias hidraulico dianteiro (%)", 40.0, 80.0, 60.0, 0.5)
        master_front_mm = st.number_input("Cilindro mestre dianteiro (mm)", min_value=8.0, max_value=30.0, value=15.875, step=0.125)
        master_rear_mm = st.number_input("Cilindro mestre traseiro (mm)", min_value=8.0, max_value=30.0, value=15.875, step=0.125)

    with col_thermal:
        target_decel_g = st.number_input("Desaceleracao alvo (g)", min_value=0.20, max_value=2.50, value=1.20, step=0.05)
        bias_tolerance_pct = st.number_input("Tolerancia de bias ideal (p.p.)", min_value=1.0, max_value=20.0, value=7.0, step=0.5)
        test_speed_kmh = st.number_input("Velocidade do ensaio termico (km/h)", min_value=10.0, max_value=140.0, value=60.0, step=5.0)
        repeated_stops = st.number_input("Frenagens consecutivas", min_value=1, max_value=30, value=5, step=1)
        start_temp_c = st.number_input("Temperatura inicial do disco (C)", min_value=0.0, max_value=300.0, value=40.0, step=5.0)
        max_rotor_temp_c = st.number_input("Temperatura limite do disco (C)", min_value=100.0, max_value=900.0, value=450.0, step=10.0)

    st.subheader("Componentes de freio")
    front_col, rear_col, material_col = st.columns(3)

    with front_col:
        front_pistons = st.number_input("Pistoes por pinca dianteira", min_value=1, max_value=8, value=2, step=1)
        front_piston_mm = st.number_input("Diametro pistao dianteiro (mm)", min_value=10.0, max_value=60.0, value=25.0, step=0.5)
        front_rotor_radius_m = st.number_input("Raio efetivo disco dianteiro (m)", min_value=0.03, max_value=0.18, value=0.080, step=0.005)
        front_rotor_mass_kg = st.number_input("Massa do disco dianteiro (kg)", min_value=0.1, max_value=5.0, value=0.75, step=0.05)

    with rear_col:
        rear_pistons = st.number_input("Pistoes por pinca traseira", min_value=1, max_value=8, value=2, step=1)
        rear_piston_mm = st.number_input("Diametro pistao traseiro (mm)", min_value=10.0, max_value=60.0, value=22.0, step=0.5)
        rear_rotor_radius_m = st.number_input("Raio efetivo disco traseiro (m)", min_value=0.03, max_value=0.18, value=0.075, step=0.005)
        rear_rotor_mass_kg = st.number_input("Massa do disco traseiro (kg)", min_value=0.1, max_value=5.0, value=0.65, step=0.05)

    with material_col:
        pad_mu = st.number_input("Coeficiente pastilha/disco", min_value=0.10, max_value=0.90, value=0.42, step=0.01)
        caliper_clamp_factor = st.selectbox(
            "Modelo de forca da pinca",
            options=[2.0, 1.0],
            format_func=lambda value: "Pinca fixa/oposta (2x area)" if value == 2.0 else "Area efetiva ja corrigida (1x area)",
        )
        rotor_specific_heat = st.number_input("Calor especifico do disco (J/kg.C)", min_value=200.0, max_value=900.0, value=460.0, step=10.0)

    weight_n = mass_kg * G
    target_decel_ms2 = target_decel_g * G
    target_force_n = mass_kg * target_decel_ms2
    static_front_load_n = weight_n * static_front_pct / 100
    static_rear_load_n = weight_n - static_front_load_n
    load_transfer_n = mass_kg * target_decel_ms2 * cg_height_m / wheelbase_m
    dynamic_front_load_n = static_front_load_n + load_transfer_n
    dynamic_rear_load_n = max(static_rear_load_n - load_transfer_n, 0)
    ideal_front_bias_pct = safe_divide(dynamic_front_load_n, weight_n) * 100

    master_front_area_m2 = area_from_diameter_mm(master_front_mm)
    master_rear_area_m2 = area_from_diameter_mm(master_rear_mm)
    front_piston_area_m2 = front_pistons * area_from_diameter_mm(front_piston_mm)
    rear_piston_area_m2 = rear_pistons * area_from_diameter_mm(rear_piston_mm)

    pedal_output_n = validation_pedal_force_n * pedal_ratio
    front_master_force_n = pedal_output_n * hydraulic_front_pct / 100
    rear_master_force_n = pedal_output_n * (100 - hydraulic_front_pct) / 100
    front_pressure_pa = safe_divide(front_master_force_n, master_front_area_m2)
    rear_pressure_pa = safe_divide(rear_master_force_n, master_rear_area_m2)

    front_torque_wheel_nm = front_pressure_pa * front_piston_area_m2 * caliper_clamp_factor * pad_mu * front_rotor_radius_m
    rear_torque_wheel_nm = rear_pressure_pa * rear_piston_area_m2 * caliper_clamp_factor * pad_mu * rear_rotor_radius_m
    front_brake_force_n = 2 * safe_divide(front_torque_wheel_nm, tire_radius_m)
    rear_brake_force_n = 2 * safe_divide(rear_torque_wheel_nm, tire_radius_m)
    total_brake_force_n = front_brake_force_n + rear_brake_force_n
    achievable_decel_g = safe_divide(total_brake_force_n, weight_n)
    brake_force_front_pct = safe_divide(front_brake_force_n, total_brake_force_n) * 100

    front_grip_n = tire_mu * dynamic_front_load_n
    rear_grip_n = tire_mu * dynamic_rear_load_n
    front_lock_margin_pct = (safe_divide(front_brake_force_n, front_grip_n) - 1) * 100
    rear_lock_margin_pct = (safe_divide(rear_brake_force_n, rear_grip_n) - 1) * 100
    target_capacity_margin_pct = (safe_divide(achievable_decel_g, target_decel_g) - 1) * 100
    bias_error_pct = brake_force_front_pct - ideal_front_bias_pct
    needed_pedal_force_n = safe_divide(validation_pedal_force_n * target_decel_g, achievable_decel_g)

    speed_ms = test_speed_kmh / 3.6
    energy_stop_j = 0.5 * mass_kg * speed_ms ** 2
    front_energy_j = energy_stop_j * brake_force_front_pct / 100 * repeated_stops / 2
    rear_energy_j = energy_stop_j * (100 - brake_force_front_pct) / 100 * repeated_stops / 2
    front_delta_temp_c = safe_divide(front_energy_j, front_rotor_mass_kg * rotor_specific_heat)
    rear_delta_temp_c = safe_divide(rear_energy_j, rear_rotor_mass_kg * rotor_specific_heat)
    front_final_temp_c = start_temp_c + front_delta_temp_c
    rear_final_temp_c = start_temp_c + rear_delta_temp_c

    metrics_col_1, metrics_col_2, metrics_col_3, metrics_col_4 = st.columns(4)
    metrics_col_1.metric("Desaceleracao teorica", f"{achievable_decel_g:.2f} g")
    metrics_col_2.metric("Bias de forca dianteiro", f"{brake_force_front_pct:.1f}%")
    metrics_col_3.metric("Bias ideal no alvo", f"{ideal_front_bias_pct:.1f}%")
    metrics_col_4.metric("Pedal p/ alvo", f"{needed_pedal_force_n:.0f} N")

with tabs[1]:
    st.subheader("Resumo de aprovacao")
    st.caption("Use os limites abaixo como pre-validacao de engenharia e ajuste-os conforme o regulamento e o plano de testes vigente da equipe.")

    validation_rows = [
        {
            "Criterio": "Capacidade de desaceleracao",
            "Resultado": f"{achievable_decel_g:.2f} g",
            "Meta": f">= {target_decel_g:.2f} g",
            "Margem": f"{target_capacity_margin_pct:.1f}%",
            "Status": status_from_margin(target_capacity_margin_pct),
        },
        {
            "Criterio": "Capacidade de travar eixo dianteiro",
            "Resultado": f"{front_brake_force_n:.0f} N",
            "Meta": f">= {front_grip_n:.0f} N",
            "Margem": f"{front_lock_margin_pct:.1f}%",
            "Status": status_from_margin(front_lock_margin_pct),
        },
        {
            "Criterio": "Capacidade de travar eixo traseiro",
            "Resultado": f"{rear_brake_force_n:.0f} N",
            "Meta": f">= {rear_grip_n:.0f} N",
            "Margem": f"{rear_lock_margin_pct:.1f}%",
            "Status": status_from_margin(rear_lock_margin_pct),
        },
        {
            "Criterio": "Bias proximo do ideal dinamico",
            "Resultado": f"{brake_force_front_pct:.1f}%",
            "Meta": f"{ideal_front_bias_pct:.1f}% +/- {bias_tolerance_pct:.1f} p.p.",
            "Margem": f"{abs(bias_error_pct):.1f} p.p.",
            "Status": "Aprovado" if abs(bias_error_pct) <= bias_tolerance_pct else "Atencao",
        },
        {
            "Criterio": "Esforco de pedal para a meta",
            "Resultado": f"{needed_pedal_force_n:.0f} N",
            "Meta": f"<= {pedal_force_limit_n:.0f} N",
            "Margem": f"{pedal_force_limit_n - needed_pedal_force_n:.0f} N",
            "Status": "Aprovado" if needed_pedal_force_n <= pedal_force_limit_n else "Reprovado",
        },
        {
            "Criterio": "Temperatura disco dianteiro",
            "Resultado": f"{front_final_temp_c:.0f} C",
            "Meta": f"<= {max_rotor_temp_c:.0f} C",
            "Margem": f"{max_rotor_temp_c - front_final_temp_c:.0f} C",
            "Status": "Aprovado" if front_final_temp_c <= max_rotor_temp_c else "Reprovado",
        },
        {
            "Criterio": "Temperatura disco traseiro",
            "Resultado": f"{rear_final_temp_c:.0f} C",
            "Meta": f"<= {max_rotor_temp_c:.0f} C",
            "Margem": f"{max_rotor_temp_c - rear_final_temp_c:.0f} C",
            "Status": "Aprovado" if rear_final_temp_c <= max_rotor_temp_c else "Reprovado",
        },
    ]

    validation_df = pd.DataFrame(validation_rows)
    approved_count = (validation_df["Status"] == "Aprovado").sum()
    approval_score = approved_count / len(validation_df)

    score_col, chart_col = st.columns([1, 2])

    with score_col:
        st.metric("Score de validacao", f"{approval_score * 100:.0f}%")
        st.progress(approval_score)
        if approval_score == 1:
            st.success("Projeto aprovado nos criterios configurados.")
        elif approval_score >= 0.7:
            st.warning("Projeto proximo do alvo. Revise os criterios em atencao.")
        else:
            st.error("Projeto precisa de revisao antes do teste dinamico.")

    with chart_col:
        fig = go.Figure()
        fig.add_bar(name="Forca de freio", x=["Dianteiro", "Traseiro"], y=[front_brake_force_n, rear_brake_force_n])
        fig.add_bar(name="Grip no alvo", x=["Dianteiro", "Traseiro"], y=[front_grip_n, rear_grip_n])
        fig.update_layout(
            barmode="group",
            yaxis_title="Forca por eixo (N)",
            margin=dict(l=10, r=10, t=30, b=10),
            height=330,
        )
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(validation_df.style.apply(style_validation_table, axis=1), use_container_width=True, hide_index=True)

    report_df = pd.DataFrame({
        "Parametro": [
            "Massa com piloto (kg)",
            "Desaceleracao alvo (g)",
            "Desaceleracao teorica (g)",
            "Bias hidraulico dianteiro (%)",
            "Bias de forca dianteiro (%)",
            "Bias ideal dinamico (%)",
            "Forca de pedal usada (N)",
            "Forca de pedal necessaria (N)",
            "Pressao dianteira (bar)",
            "Pressao traseira (bar)",
            "Temperatura final dianteira (C)",
            "Temperatura final traseira (C)",
            "Score de validacao (%)",
        ],
        "Valor": [
            mass_kg,
            target_decel_g,
            round(achievable_decel_g, 3),
            hydraulic_front_pct,
            round(brake_force_front_pct, 2),
            round(ideal_front_bias_pct, 2),
            validation_pedal_force_n,
            round(needed_pedal_force_n, 1),
            round(front_pressure_pa / 100000, 1),
            round(rear_pressure_pa / 100000, 1),
            round(front_final_temp_c, 1),
            round(rear_final_temp_c, 1),
            round(approval_score * 100, 1),
        ],
    })

    csv_data = pd.concat([report_df, validation_df], axis=0).to_csv(index=False).encode("utf-8")
    st.download_button(
        "Baixar relatorio de validacao",
        data=csv_data,
        file_name="brake_validation_iron_racers.csv",
        mime="text/csv",
    )

with tabs[2]:
    st.subheader("Roteiro de validacao em pista")

    if "brake_validation_plan" not in st.session_state:
        st.session_state["brake_validation_plan"] = pd.DataFrame([
            {
                "Etapa": "Inspecao estatica",
                "Criterio": "Sem vazamentos, linhas fixadas, pedal firme e retorno livre",
                "Responsavel": "",
                "OK": False,
                "Observacoes": "",
            },
            {
                "Etapa": "Sangria e pressao",
                "Criterio": "Pedal consistente em tres acionamentos consecutivos",
                "Responsavel": "",
                "OK": False,
                "Observacoes": "",
            },
            {
                "Etapa": "Burnish das pastilhas",
                "Criterio": "Assentamento feito sem fading ou vibracao anormal",
                "Responsavel": "",
                "OK": False,
                "Observacoes": "",
            },
            {
                "Etapa": "Frenagem reta",
                "Criterio": "Carro mantem trajetoria e atinge a desaceleracao alvo",
                "Responsavel": "",
                "OK": False,
                "Observacoes": "",
            },
            {
                "Etapa": "Travamento das quatro rodas",
                "Criterio": "Sistema consegue travar as quatro rodas em piso seco e reto",
                "Responsavel": "",
                "OK": False,
                "Observacoes": "",
            },
            {
                "Etapa": "Repetibilidade termica",
                "Criterio": "Temperaturas abaixo do limite apos a sequencia definida",
                "Responsavel": "",
                "OK": False,
                "Observacoes": "",
            },
            {
                "Etapa": "Pos-inspecao",
                "Criterio": "Sem vazamentos, folgas, trincas, empeno ou perda de curso",
                "Responsavel": "",
                "OK": False,
                "Observacoes": "",
            },
        ])

    edited_plan = st.data_editor(
        st.session_state["brake_validation_plan"],
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
    )
    st.session_state["brake_validation_plan"] = edited_plan

    completed_steps = edited_plan["OK"].sum() if "OK" in edited_plan else 0
    total_steps = len(edited_plan)
    st.metric("Etapas concluidas", f"{completed_steps}/{total_steps}")
    st.progress(safe_divide(completed_steps, total_steps))

    st.text_area(
        "Conclusao do engenheiro de freios",
        key="brake_engineer_conclusion",
        height=140,
        placeholder="Registre decisoes, alteracoes de bias, troca de pastilha/disco, ocorrencias de fading e proximos testes.",
    )

with tabs[3]:
    st.subheader("Analise rapida de log de frenagem")
    st.caption("Carregue um CSV do teste e selecione as colunas de tempo, velocidade e/ou aceleracao longitudinal.")

    with st.expander("Como deve ser o log de freio", expanded=True):
        st.markdown(
            """
            Para validar o freio com dados reais, o arquivo deve estar em CSV e precisa ter pelo menos uma destas combinacoes:

            - `Time` + `Speed`
            - `Time` + `AccLongitudinal`

            O ideal para a Iron Racers e registrar `Time`, `Speed`, `AccLongitudinal`, pressao de freio dianteira/traseira e, quando possivel, temperatura dos discos. A pagina consegue calcular o pico de desaceleracao usando velocidade ou aceleracao longitudinal.
            """
        )

        log_example = pd.DataFrame({
            "Time": [0.00, 0.02, 0.04, 0.06, 0.08],
            "Speed": [62.1, 61.8, 61.2, 60.1, 58.7],
            "AccLongitudinal": [0.02, -0.15, -0.42, -0.85, -1.10],
            "BrakePressureFront": [0, 5, 18, 35, 48],
            "BrakePressureRear": [0, 3, 12, 24, 31],
        })
        st.dataframe(log_example, use_container_width=True, hide_index=True)

        st.markdown(
            """
            Unidades recomendadas:

            - `Time`: segundos
            - `Speed`: km/h ou m/s
            - `AccLongitudinal`: `g` ou `m/s2`
            - `BrakePressureFront` e `BrakePressureRear`: bar, psi ou a unidade usada pelo sensor

            Durante o teste, faca a frenagem em linha reta, em local fechado e seguro, partindo de uma velocidade definida, por exemplo 60 km/h. Depois exporte o trecho do teste em CSV e carregue aqui para comparar o pico medido com a meta teorica.
            """
        )

    brake_log = st.file_uploader("CSV do ensaio de freio", type=["csv"], key="brake_log_upload")

    if brake_log is not None:
        csv_separator = st.selectbox(
            "Separador do CSV",
            options=[",", ";", "\t"],
            format_func=lambda value: "Virgula (,)" if value == "," else "Ponto e virgula (;)" if value == ";" else "Tabulacao",
        )
        log_df = pd.read_csv(brake_log, sep=csv_separator)
        st.dataframe(log_df.head(20), use_container_width=True)

        columns = list(log_df.columns)
        time_col = st.selectbox("Coluna de tempo", columns)
        speed_col = st.selectbox("Coluna de velocidade", ["Nenhuma"] + columns)
        accel_col = st.selectbox("Coluna de aceleracao longitudinal", ["Nenhuma"] + columns)
        speed_unit = st.selectbox("Unidade da velocidade", ["km/h", "m/s"]) if speed_col != "Nenhuma" else "km/h"
        accel_unit = st.selectbox("Unidade da aceleracao", ["g", "m/s2"]) if accel_col != "Nenhuma" else "g"

        measured_decel_g = None
        braking_df = pd.DataFrame()

        if accel_col != "Nenhuma":
            accel_series = pd.to_numeric(log_df[accel_col], errors="coerce")
            accel_g = accel_series / G if accel_unit == "m/s2" else accel_series
            measured_decel_g = abs(accel_g.min())
            braking_df = log_df[accel_g < -0.20]

        elif speed_col != "Nenhuma":
            time_series = pd.to_numeric(log_df[time_col], errors="coerce")
            speed_series = pd.to_numeric(log_df[speed_col], errors="coerce")
            speed_ms_series = speed_series / 3.6 if speed_unit == "km/h" else speed_series
            accel_ms2 = speed_ms_series.diff() / time_series.diff()
            accel_g = accel_ms2 / G
            measured_decel_g = abs(accel_g.min())
            braking_df = log_df[accel_g < -0.20]

        if measured_decel_g is not None:
            log_col_1, log_col_2, log_col_3 = st.columns(3)
            log_col_1.metric("Pico medido", f"{measured_decel_g:.2f} g")
            log_col_2.metric("Meta teorica", f"{target_decel_g:.2f} g")
            log_col_3.metric("Amostras em frenagem", len(braking_df))

            if measured_decel_g >= target_decel_g:
                st.success("O log atingiu a meta de desaceleracao configurada.")
            else:
                st.warning("O log ainda nao atingiu a meta configurada.")
        else:
            st.info("Selecione velocidade ou aceleracao longitudinal para calcular a desaceleracao medida.")
    else:
        st.info("Nenhum log carregado para esta pagina.")

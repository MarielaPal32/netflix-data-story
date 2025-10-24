import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Netflix Data Story", page_icon="🎬", layout="wide")

# --- SIDEBAR DE NAVEGACIÓN ---
st.sidebar.title("🎬 Habia una vez... Netflix")
st.sidebar.markdown("Navega entre las distintas secciones desde la barra lateral")

menu = st.sidebar.radio(
    "Navegación",
    ["🏠 Inicio", "🧹 Limpieza y Transformación", "📊 Visualizaciones"]
)

# --- CARGA DE DATOS ---
@st.cache_data
def load_data():
    df = pd.read_csv("C:/Users/palmi/Desktop/proyecto_mod_1/notebooks/netflix_titles_clean.csv")
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    return df

df = load_data()

# ============================================================
# 🏠 SECCIÓN 1: INICIO
# ============================================================
if menu == "🏠 Inicio":
    st.title("🎬 Netflix: La evolución del entretenimiento global")

    st.markdown("""
    ### *“Los datos también cuentan historias... solo hay que saber verlas.”* 🍿  

    Esta aplicación explora el catálogo de **Netflix** desde una perspectiva de datos.
    A continuacion, descubriremos cómo la plataforma ha transformado
    la diversion mundial y qué tendencias se esconden detrás de su expansión global.
    """)

    st.divider()

    # --- OBJETIVOS ---
    st.header("🎯 Objetivos del proyecto")

    st.markdown("""
    **Objetivo general:**  
    Analizar el catálogo de Netflix de manera visual e interactiva para identificar patrones, tendencias y transformaciones en la industria del entretenimiento.

    **Objetivos específicos:**
    - 📊 Explorar datos para comprender su diversidad y distribución.  
    - 🎥 Identificar directores, actores y países con mayor presencia en la plataforma.  
    - 📈 Analizar la evolución temporal del contenido disponible.  
    - 🌐 Examinar cómo Netflix refleja y moldea las tendencias culturales.  
    """)

    st.divider()

    st.header("🧭 Estructura del proyecto")
    st.markdown("""
    La aplicación está organizada en tres secciones principales:

    1. 🏠 **Inicio** – Introducción, objetivos y descripción general.  
    2. 🧹 **Limpieza y Transformación** – Proceso de preparación y exploración del dataset.  
    3. 📊 **Visualizaciones** – Análisis visual, storytelling y conclusiones finales.  
    """)

# ============================================================
# 🧹 SECCIÓN 2: LIMPIEZA Y TRANSFORMACIÓN
# ============================================================
elif menu == "🧹 Limpieza y Transformación":
    st.title("🧹 Limpieza y Transformación del Dataset")

    st.markdown("""
    En esta sección se detalla el proceso de **limpieza, estandarización y preparación de datos** que permitió transformar el dataset original de Netflix en una versión adecuada para el análisis exploratorio y las visualizaciones.
    """)

    st.divider()

    st.subheader("📂 Vista previa del dataset limpio")
    st.dataframe(df.head())

    st.markdown("""
    ---
    ## ✨ Transformaciones aplicadas
    """)

    # --- 1. Reemplazo de valores nulos ---
    st.markdown("""
    ### 🔧 Reemplazo de valores nulos en columnas clave
    **Qué se hizo:**  
    En las columnas `director`, `cast` y `country`, muchos registros aparecían vacíos o con valores nulos.  
    Se reemplazaron por el texto `"Unknown"`.

    **Por qué:**  
    - Evita errores en los conteos y agrupaciones.  
    - Permite incluir esos registros en los gráficos sin perder información.  
    - Mantiene la consistencia del dataset, ya que los valores nulos pueden distorsionar los análisis.

    """)

    # --- 2. Eliminación de filas incompletas ---
    st.markdown("""
    ### 🗑️ Eliminación de registros con datos críticos faltantes
    **Qué se hizo:**  
    Se eliminaron filas con información faltante en columnas esenciales como `date_added` (fecha de incorporación).

    **Por qué:**  
    - Esta columna es necesaria para analizar la evolución temporal y las características del contenido.  
    - Mantener filas incompletas podía generar visualizaciones inexactas o confusas.  
    """)

    # --- 3. Conversión de fechas ---
    st.markdown("""
    ### ⏰ Conversión de fechas y creación de columna “year_added”
    **Qué se hizo:**  
    La columna `date_added` fue transformada al formato de fecha (`datetime`) y se creó una nueva columna `year_added` con el año de incorporación a Netflix.

    **Por qué:**  
    - Facilita el análisis temporal y la creación de gráficos de evolución.  
    - Permite detectar patrones de crecimiento o reducción del catálogo a lo largo de los años.
    """)

    # --- 4. Renombrado de columnas ---
    st.markdown("""
    ### 🏷️ Renombrado de columnas para mayor claridad
    **Qué se hizo:**  
    La columna `listed_in`, que contenía los géneros del contenido, fue renombrada como `genre`.

    **Por qué:**  
    - Mejora la legibilidad del dataset.  
    - Hace que el código sea más intuitivo y fácil de interpretar al crear visualizaciones.  
    """)

    # --- 5. Limpieza de texto ---
    st.markdown("""
    ### ✂️ Limpieza de texto en campos de tipo cadena
    **Qué se hizo:**  
    Se aplicó una limpieza básica a las columnas de texto (`title`, `cast`, `country`, `genre`) para eliminar espacios extra y caracteres no deseados.

    **Por qué:**  
    - Garantiza uniformidad al contar valores únicos o agrupar por categorías.  
    - Evita que `"India"` e `" India"` se consideren países distintos, por ejemplo.
    """)

    st.markdown("""
    ---
    ✅ **Resumen:**  
    Gracias a estos pasos, el dataset quedó preparado para un análisis visual confiable.  
    La limpieza no solo mejora la calidad de los datos, sino también **la precisión de las conclusiones** que se pueden obtener a partir de ellos.
    """)

# ============================================================
# 📊 SECCIÓN 3: VISUALIZACIONES
# ============================================================
elif menu == "📊 Visualizaciones":
    st.title("📊 Análisis Visual y Conclusion Final")
    st.markdown("""
    A continuación, exploramos los patrones y tendencias del catálogo de Netflix.  
    """)

    st.markdown("---")
    st.subheader("Hechemos un vistazo a estas graficas")

    col1, col2 = st.columns(2)
    with col1:
        top_directores = (
            df[df['director'] != 'Unknown']['director']
            .value_counts()
            .head()
            .reset_index()
        )
        top_directores.columns = ['Director', 'Cantidad de Títulos']
        fig_directores = px.bar(
            top_directores,
            x='Director',
            y='Cantidad de Títulos',
            color='Cantidad de Títulos',
            color_continuous_scale="reds",
            title="🎬 Top 5 directores con más títulos en Netflix",
        )
        st.plotly_chart(fig_directores, use_container_width=True)
        st.markdown("""**Observaciones:**  
        Directores como *Raúl Campos y Jan Suter* dominan la producción dentro de categorías específicas, 
        como los especiales de comedia.""")

    with col2:
        cast_explode = df['cast'].dropna().str.split(',').explode().str.strip()
        top_cast = cast_explode.value_counts().head().reset_index()
        top_cast.columns = ['Actor/Actriz', 'Cantidad de Títulos']
        fig_cast = px.bar(
            top_cast,
            x='Actor/Actriz',
            y='Cantidad de Títulos',
            color='Cantidad de Títulos',
            color_continuous_scale="reds",
            title="🎭 Top 5 actores y actrices más presentes en Netflix",
        )
        st.plotly_chart(fig_cast, use_container_width=True)

        st.markdown("""**Observaciones:**  
        *David Attenborough* destaca por su presencia en documentales, mientras que *Anupam Kher* y *Naseeruddin Shah* 
        son figuras recurrentes en el cine indio disponible en la plataforma.""")

    col1, col2 = st.columns(2)
    with col1:
        conteo_tipo = df["type"].value_counts().reset_index()
        fig1 = px.pie(
            conteo_tipo,
            names="type",
            values="count",
            title="📺 Distribución de Películas vs Series",
            color_discrete_sequence=["#E50914", "#221f1f"]
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("""**Observaciones:**  
        Aunque las películas constituyen la mayoría del contenido (**70% aprox.**), las series han crecido de forma constante.""")

    with col2:
        paises = df["country"].dropna().str.split(",").explode().str.strip().value_counts().head(10)
        fig2 = px.bar(
            paises,
            x=paises.index,
            y=paises.values,
            title="🌍 Top 10 Países Productores",
            color=paises.values,
            color_continuous_scale="reds"
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("""**Observaciones:**  
        Estados Unidos lidera la producción de contenido con más de **3,793 títulos**, seguido de India y Reino Unido.""")

    evolucion = df.groupby("year_added").size().reset_index(name="Cantidad")
    fig3 = px.line(
        evolucion,
        x="year_added",
        y="Cantidad",
        markers=True,
        title="📈 Evolución del catálogo a lo largo del tiempo",
        line_shape="spline",
        color_discrete_sequence=["#E50914"]
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("""**Observaciones:**  
    Netflix experimentó un **crecimiento exponencial** a partir de 2013, llegando a su **pico maximo en el 2019**, pero luego tuvo una **fuerte caida** en cuestion de titulos, posiblemente por la pandemia COVID-19 y la incorporacion de nuevas plataformas de streaming.""")

    st.markdown("---")
    st.subheader("🎯 Conclusiones finales")
    st.markdown("""
    ### *“Más allá de pelis y series... una historia sobre cómo miramos el mundo.”*  

    Netflix cambió la forma en que consumimos películas y series, y con ello también **la forma en que entendemos la cultura**.  
    Los datos reflejan:
    - 🎬 Directores y actores prolíficos que consolidan su presencia global.  
    - 📈 Crecimiento del catálogo y expansión de historias diversas.  
    - 🌍 Democratización del entretenimiento y difusión cultural.  
    - 🎭 Un espejo de nuestras preferencias y del mundo que queremos ver.  
    En definitiva, este análisis no trata solo de números o gráficos, sino de una pregunta más profunda: **¿Qué nos dicen nuestras elecciones sobre quiénes somos y qué queremos ver del mundo?**
                
    💬 *Netflix no solo distribuye contenido: moldea la cultura global del entretenimiento. En sus datos, podemos leer las historias que elegimos contar y las que todavía están por contarse.* 🎥
    """)

# ============================================================
# 🎬 FIN DEL APP
# ============================================================

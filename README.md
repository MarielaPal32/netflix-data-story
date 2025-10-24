🎬 Habia una vez... Netflix
“Los datos también cuentan historias... solo hay que saber verlas.” 🍿

Una aplicación interactiva creada con Streamlit, Pandas y Plotly que explora el catálogo global de Netflix, revelando tendencias sobre directores, actores, países productores y la evolución del contenido a lo largo del tiempo.

📖 Descripción general

Netflix Data Story busca convertir datos en narrativas visuales.
A través de gráficos y observaciones, la app invita a descubrir cómo Netflix ha transformado el entretenimiento mundial, y qué patrones esconden los datos detrás de su catálogo.

🔍 Lo que podrás explorar:

🎬 Directores con más títulos

🎭 Actores y actrices más recurrentes

📺 Distribución entre películas y series

🌍 Países líderes en producción de contenido

📈 Evolución del catálogo a lo largo del tiempo

La aplicación está organizada en diferentes secciones accesibles desde el menú lateral:

- 🏠 *Home*: Introducción, contexto y objetivos.
- 🧹 *Limpieza y preparación*: Explicación del proceso de depuración y transformación de datos.
- 🎨 *Visualizaciones*: Gráficos interactivos sobre tendencias clave del catálogo.

🎯 Objetivos

Objetivo general

Analizar el catálogo de Netflix a través de un enfoque visual e interactivo, con el fin de identificar patrones, tendencias y transformaciones en la industria del entretenimiento global.

Objetivos específicos

📊 Explorar los datos del catálogo para comprender la diversidad y distribución de su contenido.

🎥 Identificar los directores, actores y países con mayor presencia en la plataforma.

📈 Visualizar la evolución temporal del contenido, observando crecimientos o caídas en distintos periodos.

🌐 Analizar cómo Netflix refleja y moldea las tendencias culturales globales a través de su catálogo.

💡 Fomentar el pensamiento analítico y la alfabetización en datos mediante la visualización interactiva.

🧩 Tecnologías utilizadas

Tecnología	Descripción
Streamlit	Framework para crear aplicaciones web interactivas en Python.
Pandas	Manejo y limpieza de datos.
Plotly Express	Creación de visualizaciones dinámicas e interactivas.

⚙️ Instalación y ejecución

1️⃣ Clonar el repositorio
git clone COMPLETAR: git clone https://github.com/MarielaPal32/netflix-data-story.git
cd netflix-data-story

2️⃣ Crear un entorno virtual (opcional pero recomendado)

python -m venv venv
source venv/bin/activate     # En macOS/Linux
venv\Scripts\activate        # En Windows (si no funciona, cambiar las barras a esta posicion: / )

3️⃣ Instalar las dependencias

pip install -r requirements.txt
pip install streamlit pandas plotly
pip freeze > requirements.txt

4️⃣ Añadir el dataset

Coloca el archivo netflix_titles_clean.csv en la raíz del proyecto.
Puedes obtenerlo a partir del dataset original de Kaggle:
🔗 Netflix Movies and TV Shows Dataset

5️⃣ Ejecutar la aplicación

streamlit run app.py
Luego abre el enlace local que aparece en tu terminal (por defecto, http://localhost:8501).

📊 Visualizaciones incluidas

🎬 Top 5 Directores con más títulos
Muestra los cineastas más productivos dentro del catálogo.

🎭 Top 5 Actores y Actrices más recurrentes
Analiza la presencia de los intérpretes más frecuentes en Netflix.

📺 Distribución de películas vs series
Observa qué tipo de contenido domina la plataforma.

🌍 Top 10 países productores
Identifica qué regiones contribuyen más al catálogo global.

📈 Evolución del catálogo a lo largo del tiempo
Muestra el crecimiento del contenido disponible en Netflix por año.

💡 Conclusiones destacadas

📈 El análisis de datos muestra cómo Netflix refleja, adapta y amplifica las tendencias culturales globales.

📁 Estructura del proyecto
📂 netflix-data-story/
app.py                    # Código principal de la aplicación
netflix_titles_clean.csv   # Dataset limpio
requirements.txt           # Dependencias del proyecto
README.md                  # Documentación

🧑‍💻 Autor

Mariela Palmieri
📧 mariela-palmieri@bootcamp-upgrade.hub

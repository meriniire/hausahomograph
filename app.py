import streamlit as st

# Hausa homograph data
homograph_data = {
    "gari": {
        "meanings": [
            {"phonology": "gāri", "meaning": "town", "example": "Garin ya yi kyau."},
            {"phonology": "gàrī", "meaning": "cooked rice", "example": "Nayi gari."},
        ],
        "syntactic_insight": "Context helps to distinguish meanings."
    },
    "kasa": {
        "meanings": [
            {"phonology": "kásà", "meaning": "earth/soil", "example": "Kasan nan yana da kyau."},
            {"phonology": "kàsa", "meaning": "to fall", "example": "Ya kasa tsayawa."},
        ],
        "syntactic_insight": "Tonal variations clarify usage."
    },
    "hawa": {
        "meanings": [
            {"phonology": "hāwa", "meaning": "to rise", "example": "Hawan jijiya."},
            {"phonology": "hàwa", "meaning": "to fly", "example": "Hawawa suna sararin sama."},
        ],
        "syntactic_insight": "Contextual clues are essential."
    },
    "baki": {
        "meanings": [
            {"phonology": "bāki", "meaning": "mouth", "example": "Bakin yana da kyau."},
            {"phonology": "bàki", "meaning": "guest", "example": "Bakin ya zo."},
        ],
        "syntactic_insight": "Context is key for meaning."
    },
    "daka": {
        "meanings": [
            {"phonology": "dàkà", "meaning": "to beat", "example": "Ya daka karnin."},
            {"phonology": "dáka", "meaning": "to cook", "example": "Daka abinci."},
        ],
        "syntactic_insight": "Usage context is crucial."
    },
    "taka": {
        "meanings": [
            {"phonology": "tàkà", "meaning": "to step", "example": "Takan yana da kyau."},
            {"phonology": "taka", "meaning": "to be quiet", "example": "Taka shuru."},
        ],
        "syntactic_insight": "Tonal differences matter."
    },
    "raki": {
        "meanings": [
            {"phonology": "rākī", "meaning": "to hold", "example": "Rakin ya rike."},
            {"phonology": "raki", "meaning": "to carry", "example": "Raki kaya."},
        ],
        "syntactic_insight": "Context clarifies meaning."
    },
    "saka": {
        "meanings": [
            {"phonology": "sàká", "meaning": "to place", "example": "Saka a wajen."},
            {"phonology": "saka", "meaning": "to put on", "example": "Saka hula."},
        ],
        "syntactic_insight": "Contextual clues are important."
    },
    "fara": {
        "meanings": [
            {"phonology": "fàrà", "meaning": "to start", "example": "Fara aiki."},
            {"phonology": "fara", "meaning": "to bloom", "example": "Faran itace."},
        ],
        "syntactic_insight": "Usage context is key."
    },
    "bawa": {
        "meanings": [
            {"phonology": "bàwà", "meaning": "to serve", "example": "Bawa abinci."},
            {"phonology": "bawa", "meaning": "to give", "example": "Bawa kyauta."},
        ],
        "syntactic_insight": "Context distinguishes meanings."
    },
    "kawa": {
        "meanings": [
            {"phonology": "kàwà", "meaning": "to follow", "example": "Kawa wajen."},
            {"phonology": "kawa", "meaning": "to be equal", "example": "Kawa da juna."},
        ],
        "syntactic_insight": "Context is crucial."
    },
    "zama": {
        "meanings": [
            {"phonology": "zàma", "meaning": "to sit", "example": "Zama a gida."},
            {"phonology": "zama", "meaning": "to become", "example": "Zama shugaban."},
        ],
        "syntactic_insight": "Tonal context is key."
    },
    "kasa": {
        "meanings": [
            {"phonology": "kásà", "meaning": "to support", "example": "Kasa ginin."},
            {"phonology": "kàsa", "meaning": "to fall down", "example": "Kasa daga sama."},
        ],
        "syntactic_insight": "Context clarifies usage."
    },
    "fiki": {
        "meanings": [
            {"phonology": "fìkì", "meaning": "to grow", "example": "Fiki itace."},
            {"phonology": "fiki", "meaning": "to rise", "example": "Fiki da kyau."},
        ],
        "syntactic_insight": "Context is essential."
    },
    "sana": {
        "meanings": [
            {"phonology": "sànà", "meaning": "to work", "example": "Sana da kyau."},
            {"phonology": "sana", "meaning": "to create", "example": "Sana sabuwar hanya."},
        ],
        "syntactic_insight": "Context is key."
    },
    "zaki": {
        "meanings": [
            {"phonology": "zàkì", "meaning": "lion", "example": "Zakin yana da karfi."},
            {"phonology": "zaki", "meaning": "to joke", "example": "Zaki da ni."},
        ],
        "syntactic_insight": "Contextual clues matter."
    },
    "dari": {
        "meanings": [
            {"phonology": "dàrí", "meaning": "to count", "example": "Dari a jiya."},
            {"phonology": "dari", "meaning": "to laugh", "example": "Dari a gidan."},
        ],
        "syntactic_insight": "Tonal distinctions are important."
    },
}

# Custom page configuration for professional appearance
st.set_page_config(
    page_title="Hausa Homographic Words Analysis",
    page_icon="🗣️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
custom_css = """
<style>
    /* Background and font */
    .reportview-container {
        background: #f1f5f8;
        color: #1b262c;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        padding: 2rem 1rem;
    }
    /* Main title style */
    .css-1v3fvcr h1 {
        font-size: 3.2rem;
        font-weight: 900;
        color: #0d3b66;
        text-align: center;
        margin-bottom: 0.3rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    /* Subtitle text style */
    .css-1d391kg p {
        font-size: 1.2rem;
        font-weight: 600;
        color: #3282b8;
        text-align: center;
        margin-bottom: 2.5rem;
    }
    /* Input text label & box styling */
    .stTextInput>label {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0d3b66;
        margin-bottom: 0.3rem;
    }
    .stTextInput>div>input {
        border: 2.5px solid #3282b8;
        border-radius: 0.5rem;
        padding: 12px 18px;
        font-size: 1.1rem;
        color: #1b262c;
        outline-offset: 0px;
        transition: border-color 0.3s ease;
    }
    .stTextInput>div>input:focus {
        border-color: #56c596;
        box-shadow: 0 0 10px #56c596aa;
    }
    /* Button styling */
    div.stButton > button {
        background: #3282b8;
        color: #f1faee;
        font-size: 1.2rem;
        font-weight: 900;
        padding: 12px 50px;
        margin-top: 1.5rem;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        display: block;
        margin-left: auto;
        margin-right: auto;
        letter-spacing: 2px;
        text-transform: uppercase;
        box-shadow: 0 6px 12px rgb(50 130 184 / 0.5);
    }
    div.stButton > button:hover {
        background: #56c596;
        box-shadow: 0 8px 14px rgb(86 197 150 / 0.7);
        color: #0d3b66;
    }
    /* Section headers */
    .css-zt5ig7 h2 {
        font-size: 1.8rem;
        font-weight: 800;
        color: #3282b8;
        margin-top: 3rem;
        border-bottom: 3px solid #56c596;
        padding-bottom: 5px;
    }
    /* Meaning cards container */
    .meaning-card {
        background: #f5f9fb;
        border-radius: 10px;
        padding: 18px 25px;
        box-shadow: 0 2px 8px rgb(86 197 150 / 0.2);
        margin-bottom: 1.5rem;
        color: #1b262c;
        font-size: 1.05rem;
        line-height: 1.5;
    }
    .meaning-card .phonology {
        font-weight: 700;
        color: #3282b8;
        margin-bottom: 5px;
    }
    .meaning-card .meaning {
        font-style: italic;
        margin-bottom: 8px;
    }
    .meaning-card .example {
        color: #52796f;
        font-size: 1rem;
    }
    /* Error and info messages */
    .stError {
        border-left: 6px solid #e63946 !important;
        background-color: #fbb1b1 !important;
        color: #67000d !important;
        font-weight: 700;
        padding: 1rem;
        border-radius: 6px;
    }
    .stInfo {
        border-left: 6px solid #3282b8 !important;
        background-color: #bbe1fa !important;
        color: #0d3b66 !important;
        font-weight: 700;
        padding: 1rem;
        border-radius: 6px;
    }
    /* Hide Streamlit default footer */
    footer {
        visibility: hidden;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Render your app using your original code IDs and logic intact
st.title("Hausa Homographic Words Analysis")
st.write("""
This app explores Hausa homographic words, highlighting their phonological variations, tonal distinctions, and contextual usage.
""")

word = st.text_input("Enter a Hausa homographic word (isolated):").strip().lower()

if st.button("Start Analysis"):
    if word:
        if word in homograph_data:
            data = homograph_data[word]
            st.subheader(f"Analysis of '{word}'")
            st.markdown("### Phonological Variations, Meanings & Example Usage")
            for entry in data["meanings"]:
                st.markdown(
                    f"""<div class="meaning-card">
                         <p class="phonology">Phonology: {entry['phonology']}</p>
                         <p class="meaning">Meaning: {entry['meaning']}</p>
                         <p class="example">Example: {entry['example']}</p>
                       </div>""", unsafe_allow_html=True)
            st.markdown("### Syntactic and Contextual Insights")
            st.write(data["syntactic_insight"])
        else:
            st.error("Please try another Hausa homograph.")
    else:
        st.info("Please enter a Hausa homographic word above to start analysis.")

st.markdown("---")
st.write("""
### Objectives Covered:
1. Identify and categorize homographic Hausa words by phonological variations.
2. Examine tonal roles in distinguishing meanings of homographs.
3. Analyze syntactic/contextual factors aiding disambiguation.
""")
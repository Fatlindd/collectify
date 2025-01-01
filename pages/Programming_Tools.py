import streamlit as st

# Custom CSS for styling cards
st.markdown("""
    <style>
    .card {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #f8f9fa;
        padding: 15px;
        margin: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        text-align: center;
    }
    .card img {
        width: 60px;
        height: 60px;
        margin-bottom: 10px;
    }
    .card-title {
        font-size: 16px;
        font-weight: bold;
        color: #333;
        margin: 5px 0;
    }
    .card-description {
        font-size: 14px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Programming Tools")
st.divider()

# Create three columns
col1, col2, col3 = st.columns(3)

# Card 1: VSCode
with col1:
    st.markdown("""
        <div class="card">
            <img src="https://code.visualstudio.com/assets/images/code-stable.png" alt="VSCode Logo">
            <p class="card-title">Visual Studio Code</p>
            <p class="card-description">A powerful editor used to write and debug code for various programming languages.</p>
        </div>
    """, unsafe_allow_html=True)

# Card 2: PyCharm (Updated Image URL)
with col2:
    st.markdown("""
        <div class="card">
            <img src="https://resources.jetbrains.com/storage/products/company/brand/logos/PyCharm_icon.png" alt="PyCharm Logo">
            <p class="card-title">PyCharm</p>
            <p class="card-description">An IDE for Python development, providing intelligent code assistance and debugging tools.</p>
        </div>
    """, unsafe_allow_html=True)

# Card 3: Jupyter
with col3:
    st.markdown("""
        <div class="card">
            <img src="https://jupyter.org/assets/homepage/main-logo.svg" alt="Jupyter Logo">
            <p class="card-title">Jupyter Notebook</p>
            <p class="card-description">An open-source tool for interactive coding, data visualization, and exploratory analysis.</p>
        </div>
    """, unsafe_allow_html=True)

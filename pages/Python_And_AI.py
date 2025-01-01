import streamlit as st

st.set_page_config(layout="wide")

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
        height: 300px;
        position: relative;
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
        margin-bottom: 30px;
    }
    .card-footer {
        position: absolute;
        bottom: 10px;
        font-size: 14px;
        color: #777;
        width: 100%;
        text-align: center;
    }
    .card-button {
        background-color: #5484AB; /* New color */
        color: white;
        padding: 12px 24px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        font-size: 16px; /* Increased font size */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .card-button:hover {
        background-color: #78a9d0; /* Darker shade on hover */
    }
    </style>
""", unsafe_allow_html=True)

st.title("Python And AI")
st.divider()

# List of extensions with descriptions and Chrome Web Store links
frontend_tools = [
    {
        "name": "Copycoder.ai",
        "description": "CopyCoder.ai is an AI tool that helps developers generate and optimize code snippets, improving coding efficiency and productivity. Watch this: https://www.youtube.com/watch?v=PE_D-O2PUwQ",
        "logo_url": "https://miro.medium.com/v2/resize:fit:1000/0*cOqooDOsnb8jDm2G.png",
        "store_link": "https://copycoder.ai/"
    },
    {
        "name": "urlparse",
        "description": "The urlparse function from Python's urllib.parse module breaks down a URL into its components (scheme, netloc, path, etc.) for easy analysis.",
        "logo_url": "https://miro.medium.com/v2/resize:fit:1000/0*cOqooDOsnb8jDm2G.png",
        "store_link": "https://pypi.org/project/urlparse4/"
    },
    {
        "name": "dotenv",
        "description": "The load_dotenv function from the dotenv library loads environment variables from a .env file into Python's os.environ for secure configuration management.",
        "logo_url": "https://miro.medium.com/v2/resize:fit:1000/0*cOqooDOsnb8jDm2G.png",
        "store_link": "https://pypi.org/project/python-dotenv/"
    }
]

# Search functionality
search_query = st.text_input("Search:", "")

# Filter FrontEnd Tools based on the search query
filtered_python_tool = [
    ext for ext in frontend_tools if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display extensions in a grid of three cards per row
for i in range(0, len(filtered_python_tool), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_python_tool[i:i+3]):
        with col:
            st.markdown(f"""
                <div class="card">
                    <img src="{ext['logo_url']}" alt="{ext['name']} Logo">
                    <p class="card-title">{ext['name']}</p>
                    <p class="card-description">{ext['description']}</p>
                    <a href="{ext['store_link']}" target="_blank">
                        <button class="card-button">Visit Website</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

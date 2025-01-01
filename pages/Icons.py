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
        background-color: #15B392; /* New color */
        color: white;
        padding: 12px 24px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        font-size: 16px; /* Increased font size */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .card-button:hover {
        background-color: #54C392; /* Darker shade on hover */
    }
    </style>
""", unsafe_allow_html=True)

st.title("Icon Websites")
st.divider()

# List of extensions with descriptions and Chrome Web Store links
frontend_tools = [
    {
        "name": "Shape So",
        "description": "Shape.so offers over 36,600 fully customizable icons and illustrations, designed to enhance design workflows with extensive customization options.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://shape.so/"
    },
]

# Search functionality
search_query = st.text_input("Search Icon Website:", "")

# Filter FrontEnd Tools based on the search query
filtered_icon_website = [
    ext for ext in frontend_tools if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display extensions in a grid of three cards per row
for i in range(0, len(filtered_icon_website), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_icon_website[i:i+3]):
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

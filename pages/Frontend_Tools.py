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
        height: auto;
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
        background-color: #4CC9FE; /* New color */
        color: white;
        padding: 12px 24px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        font-size: 16px; /* Increased font size */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .card-button:hover {
        background-color: #00a7ee; /* Darker shade on hover */
    }
    </style>
""", unsafe_allow_html=True)

st.title("FrontEnd Tools")
st.divider()

# List of extensions with descriptions and Chrome Web Store links
frontend_tools = [
    {
        "name": "Dribbble.com",
        "description": "Dribbble is a creative community and platform where designers share their work, showcase portfolios, and collaborate on design projects.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://dribbble.com"
    },
    {
        "name": "CSS Loaders",
        "description": "This website provides customizable CSS loader animations for enhancing website user interfaces and experiences.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://css-loaders.com/"
    },
    {
        "name": "SVG Backgrounds",
        "description": "This website offers a collection of customizable SVG backgrounds for enhancing web design aesthetics and creativity.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://www.svgbackgrounds.com/"
    },
    {
        "name": "Free CSS",
        "description": "This website provides free CSS templates, resources, and tools for web developers to streamline design projects.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://www.free-css.com/"
    },
    {
        "name": "Monster Eléctrico",
        "description": "This CodePen showcases a creative and interactive web design or functionality, ideal for inspiration and learning.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://codepen.io/becod/pen/VwdjRxY"
    },
    {
        "name": "Font Awesome",
        "description": "This website offers a comprehensive collection of scalable vector icons for enhancing web and app designs.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://fontawesome.com/icons"
    },
    {
        "name": "Placeholder",
        "description": "This website generates customizable placeholder images of specified sizes, useful for web and app design mockups.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://via.placeholder.com/1200x400"
    },
    {
        "name": "Openui",
        "description": "This website provides AI-powered tools for designing and prototyping user interfaces, enhancing web and app development.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://openui.fly.dev/ai/new"
    },
    {
        "name": "Iconscout",
        "description": "Iconscout offers a vast library of high-quality icons, illustrations, and design assets for web and app development.",
        "logo_url": "https://cdni.iconscout.com/illustration/premium/thumb/astronautenlandung-auf-dem-mond-6129606-5036997.png",
        "store_link": "https://iconscout.com/"
    }
]

# Search functionality
search_query = st.text_input("Search FrontEnd Tool:", "")

# Filter FrontEnd Tools based on the search query
filtered_frontend_tools = [
    ext for ext in frontend_tools if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display extensions in a grid of three cards per row
for i in range(0, len(filtered_frontend_tools), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_frontend_tools[i:i+3]):
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

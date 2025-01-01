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

st.title("Useful Websites")
st.divider()

# List of extensions with descriptions and Chrome Web Store links
frontend_tools = [
    {
        "name": "Storia AI",
        "description": "Storia.ai is an AI-powered platform that transforms text into engaging visual stories, enhancing content presentation.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://storia.ai"
    },
    {
        "name": "Undetectable.ai",
        "description": "Undetectable.ai is a tool that transforms AI-generated text into human-like content, bypassing AI detection systems.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://undetectable.ai/"
    },
    {
        "name": "Kickresume.com",
        "description": "Kickresume is a platform offering tools to create professional resumes, cover letters, and portfolios, enhancing job application success.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.kickresume.com/en/"
    },
    {
        "name": "Tineye.com",
        "description": "TinEye is an image search and recognition platform that helps users find image sources, duplicates, and usage online.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://tineye.com/"
    },
    {
        "name": "Devdocs.io",
        "description": "DevDocs is an extensive API documentation aggregator providing fast, offline access to programming languages and frameworks for developers.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://devdocs.io/"
    },
    {
        "name": "Deskin.io",
        "description": "Deskin.io is a platform that allows businesses to create and manage their own AI-powered customer support agents for better service.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.deskin.io/"
    },
    {
        "name": "Explorer.globe.engineer",
        "description": "Explorer.globe.engineer is a mapping platform that visualizes global data, offering interactive tools for exploring geographical and environmental information.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://explorer.globe.engineer/"
    },
    {
        "name": "Backgroundchecks.org",
        "description": "JustDeleteMe is a website that provides direct links and guides for deleting accounts from various online services and platforms.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://backgroundchecks.org/justdeleteme/"
    },
    {
        "name": "Yeschat.ai",
        "description": "YesChat.ai is an AI-powered platform that enables businesses to engage with customers through automated, conversational chatbots on websites and apps.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.yeschat.ai/"
    },
    {
        "name": "Filecr.com",
        "description": "FileCR is a website offering free downloads of cracked software, tools, and applications for Windows and macOS.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://filecr.com"
    },
    {
        "name": "Brandmark.io",
        "description": "Brandmark.io is a platform that uses AI to create custom logos and brand identities for businesses and startups.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://brandmark.io/"
    },
    {
        "name": "Carcarekiosk.com",
        "description": "CarCareKiosk provides instructional videos for car maintenance and repair, offering step-by-step guides to help vehicle owners perform basic tasks.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.carcarekiosk.com/videos"
    },
    {
        "name": "Simplepdf.com",
        "description": "SimplePDF is an online tool that allows users to easily edit, annotate, and modify PDF documents directly in their browser.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://simplepdf.com/editor"
    },
    {
        "name": "Localsend.org",
        "description": "LocalSend is an open-source platform that allows users to securely send files directly between devices without the need for an internet connection.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://localsend.org/"
    },
    {
        "name": "Theresanaiforthat.com",
        "description": "There's an AI for That is a website that showcases various AI tools and applications across different industries and use cases.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://theresanaiforthat.com/"
    },
    {
        "name": "Mrfreetools.com",
        "description": "MrFreeTools offers a collection of free online tools for various tasks, including text editing, image manipulation, and file conversion.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://mrfreetools.com/tools/"
    },
    {
        "name": "FutureTools.com",
        "description": "FutureTools is a platform that curates and showcases innovative AI tools and technologies, helping users discover new solutions for various tasks.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.futuretools.io/"
    }
]

# Search functionality
search_query = st.text_input("Search Useful Website:", "")

# Filter FrontEnd Tools based on the search query
filtered_useful_website = [
    ext for ext in frontend_tools if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display extensions in a grid of three cards per row
for i in range(0, len(filtered_useful_website), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_useful_website[i:i+3]):
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

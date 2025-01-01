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
        background-color: #00D8FE; /* New color */
        color: white;
        padding: 12px 24px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        font-size: 16px; /* Increased font size */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .card-button:hover {
        background-color: #68e8ff; /* Darker shade on hover */
    }
    </style>
""", unsafe_allow_html=True)

st.title("React")
st.divider()

# List of extensions with descriptions and Chrome Web Store links
frontend_tools = [
    {
        "name": "Temgen.app",
        "description": "Temgen.app is a tool that uses AI to help users quickly generate and customize website templates for various needs.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://temgen.app/"
    },
    {
        "name": "Bolt.new",
        "description": "Bolt.new is a simple, fast platform for creating new projects or files with a single click, streamlining workflow.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://bolt.new/"
    },
    {
        "name": "v0.dev",
        "description": "V0.dev is a platform that helps developers quickly build and deploy applications with minimal code, focusing on simplicity and speed.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://v0.dev/"
    },
    {
        "name": "ui.shadcn.com",
        "description": "ShadCN UI is a customizable UI component library for React, built using Radix UI and Tailwind CSS, enabling seamless design integration.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://ui.shadcn.com/"
    },
    {
        "name": "magicui.design",
        "description": "Magic UI Design is a tool offering customizable CSS-based UI components and effects, ideal for creating visually engaging web designs efficiently.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://magicui.design/"
    },
    {
        "name": "ui.aceternity.com",
        "description": "Aeternity UI provides a collection of customizable React components for building modern, scalable web applications with a focus on usability and design consistency.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://ui.aceternity.com/"
    },
    {
        "name": "hyperui.dev",
        "description": "HyperUI is a collection of free, open-source UI components built with Tailwind CSS, designed for fast, customizable web development.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://www.hyperui.dev/"
    },
    {
        "name": "uiverse.io",
        "description": "Uiverse is a platform offering a wide range of free, customizable UI components and design assets, aimed at enhancing web development and user interfaces.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://uiverse.io/"
    },
    {
        "name": "swiperjs.com",
        "description": "Swiper is a modern, touch-enabled slider library for creating responsive and interactive carousels, with support for mobile and desktop interfaces.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://swiperjs.com/"
    },
    {
        "name": "embla-carousel.com",
        "description": "Embla Carousel is a lightweight, customizable, and touch-friendly JavaScript library for building smooth and responsive carousels with advanced features.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://www.embla-carousel.com/"
    },
    {
        "name": "ui.mantine.dev",
        "description": "Mantine UI is a fully-featured React component library offering customizable, accessible, and responsive components for building modern web applications.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://ui.mantine.dev/"
    },
    {
        "name": "floating-ui.com",
        "description": "Floating UI is a library for creating customizable and accessible floating elements like tooltips, popovers, and dropdowns, with support for dynamic positioning.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://floating-ui.com/docs/getting-started"
    },
    {
        "name": "hover.dev",
        "description": "Hover is a design tool for creating interactive, motion-based UI components, enabling developers to easily add animations and transitions to web projects.",
        "logo_url": "https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png",
        "store_link": "https://www.hover.dev/"
    }
]

# Search functionality
search_query = st.text_input("Search:", "")

# Filter FrontEnd Tools based on the search query
filtered_react_tool = [
    ext for ext in frontend_tools if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display extensions in a grid of three cards per row
for i in range(0, len(filtered_react_tool), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_react_tool[i:i+3]):
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

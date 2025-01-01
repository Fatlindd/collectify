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
        background-color: #EE4E4E; /* New color */
        color: white;
        padding: 12px 24px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        font-size: 16px; /* Increased font size */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .card-button:hover {
        background-color: #FF6969; /* Darker shade on hover */
    }
    </style>
""", unsafe_allow_html=True)

st.title("Youtube Tutorials")
st.divider()

# List of extensions with descriptions and Chrome Web Store links
video_tutorials = [
    {
        "name": "Python Tutorial",
        "description": "Build a SaaS App with Django, Stripe, Neon PostgreSQL, TailwindCSS, GitHub Actions",
        "logo_url": "https://static.vecteezy.com/system/resources/previews/018/930/575/non_2x/youtube-logo-youtube-icon-transparent-free-png.png",
        "store_link": "https://www.youtube.com/watch?v=WbNNESIxJnY&t=499s"
    },
    {
        "name": "Python Django 7 Hour Course",
        "description": "Build a discord-like application with Python Django",
        "logo_url": "https://static.vecteezy.com/system/resources/previews/018/930/575/non_2x/youtube-logo-youtube-icon-transparent-free-png.png",
        "store_link": "https://www.youtube.com/watch?v=PtQiiknWUcI"
    },
    {
        "name": "Django REST API",
        "description": "Build a Django Rest API with the Django Rest Framework. Complete Tutorial.",
        "logo_url": "https://static.vecteezy.com/system/resources/previews/018/930/575/non_2x/youtube-logo-youtube-icon-transparent-free-png.png",
        "store_link": "https://www.youtube.com/watch?v=c708Nf0cHrs"
    },
    {
        "name": "Python & DRF",
        "description": "Building API's with Python & Django REST Framework",
        "logo_url": "https://static.vecteezy.com/system/resources/previews/018/930/575/non_2x/youtube-logo-youtube-icon-transparent-free-png.png",
        "store_link": "https://www.youtube.com/watch?v=c0x_AaPjNCY"
    },
    {
        "name": "Django, Django Rest Framework & Next.js",
        "description": "Building Full-Stack Airbnb Clone Tutorial: Django, Django Rest Framework & Next.js | With real-time chat",
        "logo_url": "https://static.vecteezy.com/system/resources/previews/018/930/575/non_2x/youtube-logo-youtube-icon-transparent-free-png.png",
        "store_link": "https://www.youtube.com/watch?v=psB9vBxPqvE"
    },
    {
        "name": "Motivational Video",
        "description": "Disappear And Come Back Unrecognizable (7 Rules To Change Your Life)",
        "logo_url": "https://static.vecteezy.com/system/resources/previews/018/930/575/non_2x/youtube-logo-youtube-icon-transparent-free-png.png",
        "store_link": "https://www.youtube.com/watch?v=bcQY9UvfMF4"
    },
    {
        "name": "Motivational Video",
        "description": "David Goggins - How To Break Free From Your Old Self",
        "logo_url": "https://static.vecteezy.com/system/resources/previews/018/930/575/non_2x/youtube-logo-youtube-icon-transparent-free-png.png",
        "store_link": "https://www.youtube.com/watch?v=ngvOyccUzzY"
    },
    {
        "name": "Motivational Video",
        "description": "Jordan Peterson: Fix Yourself Before It's Too Late",
        "logo_url": "https://static.vecteezy.com/system/resources/previews/018/930/575/non_2x/youtube-logo-youtube-icon-transparent-free-png.png",
        "store_link": "https://www.youtube.com/watch?v=MVGJeGWZoy4"
    }
]

# Search functionality
search_query = st.text_input("Search Youtube Tutorial:", "")

# Filter video tutorials based on the search query
filtered_video_tutorials = [
    ext for ext in video_tutorials if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display extensions in a grid of three cards per row
for i in range(0, len(filtered_video_tutorials), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_video_tutorials[i:i+3]):
        with col:
            st.markdown(f"""
                <div class="card">
                    <img src="{ext['logo_url']}" alt="{ext['name']} Logo">
                    <p class="card-title">{ext['name']}</p>
                    <p class="card-description">{ext['description']}</p>
                    <a href="{ext['store_link']}" target="_blank">
                        <button class="card-button">Watch Now</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

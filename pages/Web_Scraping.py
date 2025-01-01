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
        background-color: #213555; /* New color */
        color: white;
        padding: 12px 24px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        font-size: 16px; /* Increased font size */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .card-button:hover {
        background-color: #3E5879; /* Darker shade on hover */
    }
    </style>
""", unsafe_allow_html=True)

st.title("WebScraping")
st.divider()

# List of extensions with descriptions and Chrome Web Store links
chrome_extensions = [
    {
        "name": "httpbin.org/ip",
        "description": "This is a simple API endpoint that returns the IP address of the client making the request, useful for testing and debugging network connections.",
        "logo_url": "https://www.scraping-bot.io/static/scraping-bot-bot.webp",
        "store_link": "https://httpbin.org/ip"
    },
    {
        "name": "free-proxy-list.net/",
        "description": "Free Proxy List provides a regularly updated collection of free proxy servers, including details on their anonymity level, country, and type, for use in web scraping and browsing.",
        "logo_url": "https://www.scraping-bot.io/static/scraping-bot-bot.webp",
        "store_link": "https://free-proxy-list.net/"
    },
    {
        "name": "proxyaz.com",
        "description": "ProxyAZ's order page allows users to purchase private proxies with customizable options, including location, quantity, and type, for secure and reliable usage.",
        "logo_url": "https://www.scraping-bot.io/static/scraping-bot-bot.webp",
        "store_link": "https://proxyaz.com/order"
    },
    {
        "name": "useragentstring.com",
        "description": "UserAgentString.com provides detailed information about user-agent strings, allowing users to identify or analyze browser, operating system, and device data for web applications or testing.",
        "logo_url": "https://www.scraping-bot.io/static/scraping-bot-bot.webp",
        "store_link": "https://useragentstring.com/#google_vignette"
    },
    {
        "name": "github.com/TheSpeedX/PROXY-List",
        "description": "TheSpeedX/PROXY-List on GitHub offers a repository of free, frequently updated proxy lists for various use cases like web scraping, testing, and anonymity.",
        "logo_url": "https://www.scraping-bot.io/static/scraping-bot-bot.webp",
        "store_link": "https://github.com/TheSpeedX/PROXY-List"
    },
    {
        "name": "fake_useragent",
        "description": "The fake_useragent library generates random user-agent strings in Python, helping simulate real browsers for web scraping and testing.",
        "logo_url": "https://www.scraping-bot.io/static/scraping-bot-bot.webp",
        "store_link": "https://pypi.org/project/fake-useragent/"
    },
    {
        "name": "undetected_chromedriver",
        "description": "The undetected_chromedriver library helps bypass bot detection systems by providing a patched version of ChromeDriver, ideal for stealthy web scraping or automation.",
        "logo_url": "https://www.scraping-bot.io/static/scraping-bot-bot.webp",
        "store_link": "https://pypi.org/project/undetected-chromedriver/"
    },
    {
        "name": "pyautogui",
        "description": "The pyautogui library automates keyboard and mouse interactions in Python, enabling tasks like clicking, typing, or taking screenshots programmatically.",
        "logo_url": "https://www.scraping-bot.io/static/scraping-bot-bot.webp",
        "store_link": "https://pypi.org/project/PyAutoGUI/"
    }
]

# Search functionality
search_query = st.text_input("Search:", "")

# Filter chrome extensions based on the search query
filtered_web_scraping = [
    ext for ext in chrome_extensions if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display extensions in a grid of three cards per row
for i in range(0, len(filtered_web_scraping), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_web_scraping[i:i+3]):
        with col:
            st.markdown(f"""
                <div class="card">
                    <img src="{ext['logo_url']}" alt="{ext['name']} Logo">
                    <p class="card-title">{ext['name']}</p>
                    <p class="card-description">{ext['description']}</p>
                    <a href="{ext['store_link']}" target="_blank">
                        <button class="card-button">Add to Chrome</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

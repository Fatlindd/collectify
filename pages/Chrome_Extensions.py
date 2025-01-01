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
        background-color: #DE8F5F; /* New color */
        color: white;
        padding: 12px 24px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        font-size: 16px; /* Increased font size */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .card-button:hover {
        background-color: #DEAA79; /* Darker shade on hover */
    }
    </style>
""", unsafe_allow_html=True)

st.title("Chrome Extensions")
st.divider()

# List of extensions with descriptions and Chrome Web Store links
chrome_extensions = [
    {
        "name": "Affilitizer",
        "description": "Highlights advertisers with affiliate programs within Google Search result pages and address bar.",
        "logo_url": "https://9d10a6ed95d88764e5656da465593d47.cdn.bubble.io/f1717409482454x201249152933705060/logo-dark.svg",
        "store_link": "https://chromewebstore.google.com/detail/affilitizer/oiclkoiceoklnignlihmpciebcppgbcm?hl=en"
    },
    {
        "name": "Authenticator",
        "description": "Generates two-factor authentication codes in your browser for enhanced account security.",
        "logo_url": "https://lh3.googleusercontent.com/LEgohRXYMasRoU-SXiJrkH_LsMMMgpKERWbOCpofID-cbbtKm4DjovRnDo2eiyvWBGcOUSjvQmBPOGKJW7g8y1aJCw=s120",
        "store_link": "https://chromewebstore.google.com/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai?hl=en"
    },
    {
        "name": "Captcha Solver: Auto Recognition and Bypass",
        "description": "Automatically solves CAPTCHAs found on any webpage, saving time and frustration.",
        "logo_url": "https://lh3.googleusercontent.com/HIvvq8CkMPPro7oXQsFBGPN1UL1L3HBkDl4afDm3MpnsqIEDnpxflg1l8vSzK0sD3RUQ1yWC2c47AXaxzt1WQzBV0g=s120",
        "store_link": "https://chromewebstore.google.com/detail/captcha-solver-auto-recog/ifibfemgeogfhoebkmokieepdoobkbpo?hl=en"
    },
    {
        "name": "ColorPick Eyedropper",
        "description": "Zoomed eyedropper & color chooser tool to select color values from webpages and more.",
        "logo_url": "https://lh3.googleusercontent.com/AMn3fHR239GKDCbY0qffgLBZVq1NxYUZ66AhU9AJfgKVlpfzu8-L9C3njXq9TtlMDTRmHshBw0HPAkPQdEjd0Ci1hQ=s120",
        "store_link": "https://chromewebstore.google.com/detail/colorpick-eyedropper/ohcpnigalekghcmgcdcenkpelffpdolg?hl=en"
    },
    {
        "name": "CSSViewer",
        "description": "Simple CSS property viewer for inspecting the CSS styles of any webpage element.",
        "logo_url": "https://lh3.googleusercontent.com/pbKrxHFkRZ1A_cPo-c8V0SVJ3snNEKf4-UvW-jAiv4q8pP0UHXE2NltPuC8nkazexSjdBXZrC1xLnoO6lqbKmDXO=s120",
        "store_link": "https://chromewebstore.google.com/detail/cssviewer/ggfgijbpiheegefliciemofobhmofgce?hl=en"
    },
    {
        "name": "Dark Reader",
        "description": "Applies dark mode to every website, reducing eye strain, especially for night browsing.",
        "logo_url": "https://lh3.googleusercontent.com/T66wTLk-gpBBGsMm0SDJJ3VaI8YM0Utr8NaGCSANmXOfb84K-9GmyXORLKoslfxtasKtQ4spDCdq_zlp_t3QQ6SI0A=s120",
        "store_link": "https://chromewebstore.google.com/detail/dark-reader/eimadpbcbfnmbkopoojfekhnkhdbieeh?hl=en"
    },
    {
        "name": "Get cookies.txt LOCALLY",
        "description": "Fetch cookies.txt locally, ensuring information is never sent outside with open-source security.",
        "logo_url": "https://lh3.googleusercontent.com/Cb-E_Q7BvT3KL7Zhwae-ZOvXq7gYmMb47t2NI8CPVNN6wxP9xPMy-l1pdrdfYg-VwLneBC97JJLXG3YkZH-vwd0WUw=s120",
        "store_link": "https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc?hl=en"
    },
    {
        "name": "GoFullPage - Full Page Screen Capture",
        "description": "Capture a screenshot of your current page entirely, without requiring extra permissions.",
        "logo_url": "https://lh3.googleusercontent.com/xkq24Y-hSgJHCOs7hskeMNfZatMQYRmybkMY8gGrzHTYVJiQR_2un6xgg9cXY93ShVNU5LdC7n5fddtbQxeNIV0hma8=s120",
        "store_link": "https://chromewebstore.google.com/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl?hl=en"
    },
    {
        "name": "Link Grabber",
        "description": "Easy extractor for hyperlinks on any HTML page, simplifying link collection for browsing.",
        "logo_url": "https://lh3.googleusercontent.com/rCYlsOOK8Jp19uNxe673VCj_pyQnxI_d93rhq86-DrwjOgmPIGHVJE9TyrWvCbqnm70hJK8NzmaOox4n3jq3xCQoag=s120",
        "store_link": "https://chromewebstore.google.com/detail/link-grabber/caodelkhipncidmoebgbbeemedohcdma?hl=en"
    },
    {
        "name": "Mobile simulator - responsive testing tool",
        "description": "Smartphone and tablet simulator for testing mobile-responsive websites on a computer.",
        "logo_url": "https://lh3.googleusercontent.com/AdZGgDWDCE3zyp1t_rJo1VT_9ge6l7QeFftWKrr2opJc4IgOmbQY82_4s44rGpHqZjw6ALtEsjlY8Sv1nERN-nAJEA=s120",
        "store_link": "https://chromewebstore.google.com/detail/mobile-simulator-responsi/ckejmhbmlajgoklhgbapkiccekfoccmk?hl=en"
    },
    {
        "name": "NordVPN - VPN proxy for privacy and security",
        "description": "Connect to the fastest VPN, hiding your IP, blocking ads, and securing your online activities.",
        "logo_url": "https://lh3.googleusercontent.com/fxIPBOBd5X56jsxoxNMcb6BtVFb0KvUzw-zu3x-fBFR8mQWtSWSpreUie-ekpfmm9E_KtoKUNkRsDyUXKxoutxx2Ig=s120",
        "store_link": "https://chromewebstore.google.com/detail/nordvpn-vpn-proxy-for-pri/fjoaledfpmneenckfbpdfhkmimnjocfa?hl=en"
    },
    {
        "name": "Oxylabs Proxy Extension",
        "description": "Manages proxy connections for enhanced web scraping and browsing security.",
        "logo_url": "https://lh3.googleusercontent.com/1zSSSauBHq2lWaMwbuaqE56R4N_WauV9pTsgbelmPcl1tGuCTI2q5GTmIo90AWA18PjHIEMpmv6p0pEv-u1L3h1D0g=s120",
        "store_link": "https://chromewebstore.google.com/detail/oxylabs-proxy-extension/infajoaodhhdogakhloedbppcbeajhoo?hl=en"
    },
    {
        "name": "Random User-Agent (Switcher)",
        "description": "Automatically switches user agents at specified intervals, hiding your real browser identity.",
        "logo_url": "https://lh3.googleusercontent.com/AU61vjsscq3ZEhUWYYjFxYYFg0kn4jl6O0H-EAvVPkN0ODkAASBjQZ-Q42Qeu2u-rT16OlqdwzOnJ73aK8lOe1siNsc=s120",
        "store_link": "https://chromewebstore.google.com/detail/random-user-agent-switche/einpaelgookohagofgnnkcfjbkkgepnp?hl=en"
    },
    {
        "name": "React Developer Tools",
        "description": "Adds React debugging tools to Chrome Developer Tools, improving development and debugging experience.",
        "logo_url": "https://lh3.googleusercontent.com/TNijZW_Gp9MZ3eqXkve0YWDEiHV-a2IpSpD6IJzrV3Y76GJcLEyzX2regTLemXzBHbHVqkKuxnnWDT34Cp4sNh-Y=s120",
        "store_link": "https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en"
    },
    {
        "name": "SelectorGadget",
        "description": "Powerful CSS Selector generation tool, simplifying web scraping and DOM manipulation tasks.",
        "logo_url": "https://lh3.googleusercontent.com/KgM6zxhwYCf-5njZWJPtrmF4DCWJx6EzzHcSNMgoFmIIezyb4VY55ibfK9bRMA23ItntbuYOH-d0zflZ54yr0A4Oqg=s120",
        "store_link": "https://chromewebstore.google.com/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=en"
    },
    {
        "name": "SelectorsHub - XPath Helper",
        "description": "Helps generate, write, and verify XPath & CSS selectors for easier web scraping.",
        "logo_url": "https://store-images.s-microsoft.com/image/apps.53791.c99d91ea-7a1f-44f0-ac5c-e991463dbdd9.dfdc8dd3-3f15-47c6-9c2f-c4df34b19884.41768f36-fca1-4170-a3a7-7652d8c3eb06",
        "store_link": "https://chromewebstore.google.com/detail/selectorshub-xpath-helper/ndgimibanhlabgdgjcpbbndiehljcpfh?hl=en"
    },
    {
        "name": "VisBug",
        "description": "Open source browser design tools for fast UI prototyping and layout adjustments.",
        "logo_url": "https://lh3.googleusercontent.com/uuSgZ6PkjJksEGebBy_Tz3I5bkPQmEygwMTzoZS7T1262Q9iZHDyWuh1-3gAb2L8mlx6zDccBelZpIRnij6-UypGSTc=s120",
        "store_link": "https://chromewebstore.google.com/detail/visbug/cdockenadnadldjbbgcallicgledbeoc?hl=en"
    },
    {
        "name": "Wappalyzer - Technology profiler",
        "description": "Identifies web technologies used by a website, including frameworks, CMS, and more.",
        "logo_url": "https://lh3.googleusercontent.com/Ha_EGIePt_To3ErkPwaLigbdQbiTaJpWneU7Z3iNFspWfRoEEPH4tp61DC_nyXqrAaDfpdXdVg0lfKq_0d9PnnqiDpw=s120",
        "store_link": "https://chromewebstore.google.com/detail/wappalyzer-technology-pro/gppongmhjkpfnbhagpmjfkannfbllamg?hl=en"
    },
    {
        "name": "Web Developer",
        "description": "Adds a toolbar button for various web development tools and utilities for easier debugging.",
        "logo_url": "https://lh3.googleusercontent.com/H662aZCLuvojQ3u36n76zhnyo1b_y2ef7OanOaeRowoU1hR1EMbKlnPslBiAknJzRplXmjq-OXeIgtV95i-BDE-BXw=s120",
        "store_link": "https://chromewebstore.google.com/detail/web-developer/bfbameneiokkgbdmiekhjnmfkcnldhhm?hl=en"
    },
]

# Search functionality
search_query = st.text_input("Search Chrome Extension:", "")

# Filter chrome extensions based on the search query
filtered_chrome_extensions = [
    ext for ext in chrome_extensions if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display extensions in a grid of three cards per row
for i in range(0, len(filtered_chrome_extensions), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_chrome_extensions[i:i+3]):
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

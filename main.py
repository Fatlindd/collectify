import streamlit as st
from streamlit_option_menu import option_menu

# Import the resources dynamically based on selected menu
from Resources import home, Api_Free, Chrome_Extensions, Frontend_Tools, Icons_Website, Python_And_AI, React, Django, VSCode_Extensions, Web_Scraping, style, Useful_Websites, Programming_Tools, Youtube_Tutorials, Web_Design, Artificial_Intelligence, Chatgpt_prompts

# Set Streamlit layout to wide mode
st.set_page_config(page_title="Useful Tools", page_icon=":zap:", layout="wide")

# Define a dictionary to map menu items to their corresponding modules
PAGE_MODULES = {
    "Home": home,
    "Free API": Api_Free,
    "Chrome Extensions": Chrome_Extensions,
    "FrontEnd Tools": Frontend_Tools,
    "Icons Website": Icons_Website,
    "Python_And_AI": Python_And_AI,
    "React": React,
    "Django": Django,
    "VSCode Extensions": VSCode_Extensions,
    "Web Scraping": Web_Scraping,
    "Useful Websites": Useful_Websites,
    "Programming Tools": Programming_Tools,
    "Youtube Tutorials": Youtube_Tutorials,
    "Artificial Intelligence": Artificial_Intelligence,
    "Web Design": Web_Design,
    "ChatGPT Prompts": Chatgpt_prompts
}

# 1. Sidebar menu with all the required items
with st.sidebar:
    selected = option_menu(
        "Useful Tools",
        list(PAGE_MODULES.keys()),  # Dynamically use the keys of the PAGE_MODULES dict
        icons=[
            "house", "cloud", "puzzle", "tools", "palette", "terminal", 
            "code-slash", "server", "link", "plug", "search", "gear", "youtube", "robot", "brush", "chat-dots"
        ],
        menu_icon="cast",
        default_index=0
    )

# Helper function to display tools (used for Free API, Chrome Extensions, etc.)
def display_tools(page_module, tools_list, custom_css):
    # Inject custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    if page_module == Chatgpt_prompts:
        for tool in tools_list:
            st.write("📌 " + tool['used'])
            st.code(tool['description'])
            st.divider()
            # print(tool['used'])
        return

    # Filter tools based on the search term
    filtered_tools = [
        tool for tool in tools_list
        if search_term.lower() in tool['name'].lower() or search_term.lower() in tool['description'].lower()
    ]

    # Use Streamlit columns with adjusted ratios
    columns = st.columns([1, 1, 1])  # Three equal-width columns
    for idx, tool in enumerate(filtered_tools):
        col = columns[idx % 3]  # Cycle through columns
        with col:
            st.markdown(f"""
                <div class="card">
                    <img src="{tool['logo_url']}" alt="{tool['name']} logo">
                    <div class="card-title">{tool['name']}</div>
                    <div class="card-description">{tool['description']}</div>
                    <div class="card-footer">
                        <a href="{tool['store_link']}" target="_blank">
                            <button class="card-button">{tool['button_name']}</button>
                        </a>
                    </div>
                </div>
            """, unsafe_allow_html=True)


# Display content based on the selected menu item
if selected in PAGE_MODULES:
    page = PAGE_MODULES[selected]
    st.title(page.title)
    st.markdown(page.content)
    st.divider()

    if selected != "Home" and selected != "ChatGPT Prompts":
        # Global search input outside of specific page logic
        search_term = st.text_input("Search:", "")

    # Call the display_tools function for the selected page
    if selected == "Free API":
        display_tools(Api_Free, Api_Free.FREE_API_TOOLS, style.STYLE_CSS)
    elif selected == "Chrome Extensions":
        display_tools(Chrome_Extensions, Chrome_Extensions.CHROME_EXTENSIONS, style.STYLE_CSS)
    elif selected == "FrontEnd Tools":
        display_tools(Frontend_Tools, Frontend_Tools.FRONTEND_TOOLS, style.STYLE_CSS)
    elif selected == "Python_And_AI":
        display_tools(Python_And_AI, Python_And_AI.PYTHON_TOOLS, style.STYLE_CSS)
    elif selected == "Icons Website":
        display_tools(Icons_Website, Icons_Website.ICONS_WEBSITE_TOOLS, style.STYLE_CSS)
    elif selected == "React":
        display_tools(React, React.REACT_TOOLS, style.STYLE_CSS)
    elif selected == 'Django':
        display_tools(Django, Django.DJANGO_TOOLS, style.STYLE_CSS)
    elif selected == 'VSCode Extensions':
        display_tools(VSCode_Extensions, VSCode_Extensions.VSCODE_EXTENSIONS, style.STYLE_CSS)
    elif selected == 'Web Scraping':
        display_tools(Web_Scraping, Web_Scraping.WEB_SCRAPING, style.STYLE_CSS)
    elif selected == 'Useful Websites':
        display_tools(Useful_Websites, Useful_Websites.USEFUL_WEBSITE, style.STYLE_CSS)
    elif selected == 'Programmin Tools':
        display_tools(Programming_Tools, Programming_Tools.PROGRAMMING_TOOLS, style.STYLE_CSS)
    elif selected == 'Youtube Tutorials':
        display_tools(Youtube_Tutorials, Youtube_Tutorials.YOUTUBE_TUTORIALS, style.STYLE_CSS)
    elif selected == 'Web Design':
        display_tools(Web_Design, Web_Design.WEB_DESIGN, style.STYLE_CSS)
    elif selected == 'Artificial Intelligence':
        display_tools(Artificial_Intelligence, Artificial_Intelligence.ARTIFICIAL_INTELLIGENCE, style.STYLE_CSS)
    elif selected == 'ChatGPT Prompts':
        display_tools(Chatgpt_prompts, Chatgpt_prompts.CHATGPT_PROMPTS, style.STYLE_CSS)



        
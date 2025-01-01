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
    </style>
""", unsafe_allow_html=True)

st.title("VSCode Extensions")
st.divider()

# List of extensions with details and 15-word descriptions
vscode_extensions = [
    {
        "name": "BlackBox AI",
        "description": "AI-powered code assistant for generating and understanding code snippets, improving coding efficiency.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://i.imgur.com/0pTWrWy.png"
    },
    {
        "name": "Black Formatter",
        "description": "Python code formatter that ensures compliance with PEP 8, enhancing code readability and consistency.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://ms-python.gallerycdn.vsassets.io/extensions/ms-python/black-formatter/2024.5.13171011/1731408245754/Microsoft.VisualStudio.Services.Icons.Default"
    },
    {
        "name": "Codeium",
        "description": "AI autocomplete extension that boosts productivity by suggesting code snippets and speeding up coding.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEJZaFKWfF1ZpO2Jm_fNn5W24XvJkoTBercg&s"
    },
    {
        "name": "Beautiful Dracula",
        "description": "A visually appealing dark theme for code editors, promoting comfort and reducing eye strain.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://nguyenhoanglam.gallerycdn.vsassets.io/extensions/nguyenhoanglam/beautiful-dracula/0.1.4/1681012898346/Microsoft.VisualStudio.Services.Icons.Default"
    },
    {
        "name": "Error Lens",
        "description": "Highlights errors and warnings directly in the editor to enhance debugging and reduce development time.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://usernamehw.gallerycdn.vsassets.io/extensions/usernamehw/errorlens/3.22.0/1734686649548/Microsoft.VisualStudio.Services.Icons.Default"
    },
    {
        "name": "Excel Viewer",
        "description": "View and edit Excel files seamlessly within Visual Studio Code for better productivity and convenience.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://grapecity.gallerycdn.vsassets.io/extensions/grapecity/gc-excelviewer/4.2.62/1724856331929/Microsoft.VisualStudio.Services.Icons.Default"
    },
    {
        "name": "Live Server",
        "description": "Launches a local development server with live reload to test web pages in real-time.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://proclass.jp/blog/wp-content/uploads/2024/08/icon.png"
    },
    {
        "name": "Material Icon Theme",
        "description": "A comprehensive set of icons for project files, providing better visual structure and navigation.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/main/logo.png"
    },
    # Additional Extensions
    {
        "name": "Prettier",
        "description": "An opinionated code formatter supporting various languages, ensuring consistent style across projects and teams.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://prettier.io/icon.png"
    },
    {
        "name": "Quokka.js",
        "description": "Real-time JavaScript and TypeScript execution playground inside Visual Studio Code with live feedback.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://wallabyjs.gallerycdn.vsassets.io/extensions/wallabyjs/quokka-vscode/1.0.681/1734992484850/Microsoft.VisualStudio.Services.Icons.Default"
    },
    {
        "name": "Rainbow CSV",
        "description": "Formats CSV files with color coding to improve readability and help identify data patterns easily.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://mechatroner.gallerycdn.vsassets.io/extensions/mechatroner/rainbow-csv/3.13.0/1732335187526/Microsoft.VisualStudio.Services.Icons.Default"
    },
    {
        "name": "SQLite Viewer",
        "description": "View and manage SQLite databases directly within Visual Studio Code for fast database management.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://qwtel.gallerycdn.vsassets.io/extensions/qwtel/sqlite-viewer/0.9.5/1732264090808/Microsoft.VisualStudio.Services.Icons.Default"
    },
    {
        "name": "Tabnine",
        "description": "AI-powered code completion tool that helps write code faster by providing intelligent autocompletions.",
        "used_in": "Visual Studio Code",
        "logo_url": "https://tabnine.gallerycdn.vsassets.io/extensions/tabnine/tabnine-vscode/3.206.0/1735119575836/Microsoft.VisualStudio.Services.Icons.Default"
    },
]

# Search functionality
search_query = st.text_input("Search VSCode Extension:", "")

# Filter extensions based on the search query
filtered_extensions = [
    ext for ext in vscode_extensions if search_query.lower() in ext['name'].lower() or search_query.lower() in ext['description'].lower()
]

# Display filtered extensions in a grid of three cards per row
for i in range(0, len(filtered_extensions), 3):
    cols = st.columns(3)
    for col, ext in zip(cols, filtered_extensions[i:i+3]):
        with col:
            st.markdown(f"""
                <div class="card">
                    <img src="{ext['logo_url']}" alt="{ext['name']} Logo">
                    <p class="card-title">{ext['name']}</p>
                    <p class="card-description">{ext['description']}</p>
                    <div class="card-footer"><strong>Used in:</strong> {ext['used_in']}</div>
                </div>
            """, unsafe_allow_html=True)

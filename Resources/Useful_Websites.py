# Resources/web_scraping.py
title = "Useful Website"
content = "Some useful websites that can help us in different purposes."

# List of extensions with descriptions and Chrome Web Store links
USEFUL_WEBSITE = [
    {
        "name": "coursevania.com",
        "description": "Coursevania is a platform offering free online courses across various fields, including development, business, and IT, providing certificates upon completion to help learners build skills and advance their careers.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://coursevania.com/",
        "button_name": "Visit Website"
    },
    {
        "name": "Storia AI",
        "description": "Storia.ai is an AI-powered platform that transforms text into engaging visual stories, enhancing content presentation by converting written material into dynamic, interactive visuals that capture attention and improve user engagement.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://storia.ai",
        "button_name": "Visit Website"
    },
    {
        "name": "Undetectable.ai",
        "description": "Undetectable.ai is a tool that transforms AI-generated text into human-like content, effectively bypassing AI detection systems by making the text appear more natural and less machine-produced.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://undetectable.ai/",
        "button_name": "Visit Website"
    },
    {
        "name": "Kickresume.com",
        "description": "Kickresume is a platform offering tools to create professional resumes, cover letters, and portfolios, helping users enhance their job application success by presenting their skills and experience effectively.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.kickresume.com/en/",
        "button_name": "Visit Website"
    },
    {
        "name": "Tineye.com",
        "description": "TinEye is an image search and recognition platform that helps users find image sources, identify duplicates, and track usage across the web, offering valuable insights for copyright and content management.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://tineye.com/",
        "button_name": "Visit Website"
    },
    {
        "name": "Devdocs.io",
        "description": "DevDocs is an extensive API documentation aggregator that provides fast, offline access to documentation for programming languages and frameworks, helping developers quickly find the information they need.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://devdocs.io/",
        "button_name": "Visit Website"
    },
    {
        "name": "Deskin.io",
        "description": "Deskin.io is a platform that enables businesses to create and manage AI-powered customer support agents, enhancing service efficiency and providing automated, responsive support to customers for a better experience.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.deskin.io/",
        "button_name": "Visit Website"
    },
    {
        "name": "Explorer.globe.engineer",
        "description": "Explorer.globe.engineer is a mapping platform that visualizes global data, offering interactive tools for exploring geographical and environmental information, helping users gain insights into various global trends and patterns.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://explorer.globe.engineer/",
        "button_name": "Visit Website"
    },
    {
        "name": "Backgroundchecks.org",
        "description": "JustDeleteMe is a website that provides direct links and detailed guides for deleting accounts from various online services and platforms, simplifying the account removal process for users seeking privacy control.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://backgroundchecks.org/justdeleteme/",
        "button_name": "Visit Website"
    },
    {
        "name": "Yeschat.ai",
        "description": "YesChat.ai is an AI-powered platform that enables businesses to engage with customers through automated, conversational chatbots on websites and apps, improving customer support and interaction efficiency.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.yeschat.ai/",
        "button_name": "Visit Website"
    },
    {
        "name": "Filecr.com",
        "description": "FileCR is a tool or service that helps manage and track changes in files, typically for version control or backup purposes. It ensures file consistency, version history, and easy recovery of previous versions.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://filecr.com",
        "button_name": "Visit Website"
    },
    {
        "name": "Brandmark.io",
        "description": "Brandmark.io is a platform that uses AI to generate custom logos and brand identities, helping businesses and startups create unique, professional visuals to represent their brand and enhance their market presence.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://brandmark.io/",
        "button_name": "Visit Website"
    },
    {
        "name": "Carcarekiosk.com",
        "description": "CarCareKiosk offers easy-to-follow videos for car maintenance and repair. With step-by-step guides, it helps vehicle owners perform basic tasks, saving time and money while enhancing vehicle knowledge.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.carcarekiosk.com/videos",
        "button_name": "Visit Website"
    },
    {
        "name": "Simplepdf.com",
        "description": "SimplePDF is an online tool for editing, annotating, and modifying PDFs directly in your browser. It offers an intuitive interface, making PDF management fast, efficient, and accessible to everyone.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://simplepdf.com/editor",
        "button_name": "Visit Website"
    },
    {
        "name": "Localsend.org",
        "description": "LocalSend is an open-source platform enabling secure file transfers directly between devices without internet. It's fast, private, and perfect for sharing data seamlessly in offline environments.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://localsend.org/",
        "button_name": "Visit Website"
    },
    {
        "name": "Theresanaiforthat.com",
        "description": "There's an AI for That is a website showcasing diverse AI tools and applications for various industries and use cases, helping users discover innovative solutions to enhance productivity and creativity.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://theresanaiforthat.com/",
        "button_name": "Visit Website"
    },
    {
        "name": "Mrfreetools.com",
        "description": "MrFreeTools provides a variety of free online tools for tasks like text editing, image manipulation, and file conversion. It's a convenient platform for quick, easy, and efficient everyday needs.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://mrfreetools.com/tools/",
        "button_name": "Visit Website"
    },
    {
        "name": "FutureTools.com",
        "description": "FutureTools is a platform curating innovative AI tools and technologies, helping users discover new solutions for a wide range of tasks. It enables easy access to cutting-edge tools for productivity and creativity.",
        "logo_url": "https://png.pngtree.com/png-vector/20241021/ourmid/pngtree-3d-innovative-robot-with-earth-globe-design-on-transparent-background-png-image_14106884.png",
        "store_link": "https://www.futuretools.io/",
        "button_name": "Visit Website"
    }
]

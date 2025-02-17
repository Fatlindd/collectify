title = "ChatGPT Prompts"
content = "Explore a collection of powerful ChatGPT prompts to enhance creativity, productivity, and problem-solving."

CHATGPT_PROMPTS = [
    {
        "used": "To make chat act as [ROLE]",
        "description": "Act as a Full Stack Developer",
    },
    {
        "used": "Show as [FORMAT]",
        "description": 
        """
        1. A Table
        2. A List
        3. Summary
        4. HTML
        5. Code
        6. Spreadsheet
        7. Graphs
        8. CSV File
        9. Plain Text File
        10. JSON
        11. Rich Text
        12. Gantt Chart
        13. Markdown
        14. An Analogy
        15. Bullet Points
        """,
    },
    {
        "used": "Review your code for logical errors and security concerns",
        "description": "Review your provided code 'tempFunction' for any logical or security concerns and provide a list of recommendations.",
    },
    {
        "used": "Create Tests",
        "description": "Create two [ define technology ] tests for the above 'tempFunction' function. One that is expected to pass and one that is expected to fail.",
    },
    {
        "used": "Adding Documentation",
        "description": """
        I don't know how to code, but I want to understand how this works. Explain the following code to me in a way that a non-technical person can understand. Always use Markdown with nice formatting to make it easier to follow. Organize it by sections with headers. Include references to the code as markdown code blocks in each section. 
        
        The code: [insert code here]""",
    },
    {
        "used": "Explain Code",
        "description": """
        Context: I'm starting a new position as backend developer and I have to start to understand how some functions are working
        Technologies: [INSERT YOUR TECHNOLOGIES HERE]
        You have to: explain me the code line by line

        [INSERT YOUR CODE HERE]
        """,
    },
    {
        "used": "Architecture Diagram (Mermaid)",
        "description": """
        Write the Mermaid code for an architecture diagram for this solution [DESCRIBE SOLUTION]
        """,
    },
    {
        "used": "Entity Relationship Diagram (Mermaid)",
        "description": """
        Write the Mermaid code for an entity relationship diagram for these classes [INSERT CLASSES]

        """,
    },
    {
        "used": "Refactor Code",
        "description": """
        I have a piece of code and I need you do a refactor of it:

        [INSERT YOUR CODE HERE]
        """,
    },
    {
        "used": "Modernizing Old Code",
        "description": """
        Refactor the following code to modern es6 programming standards:

        [INSERT YOUR CODE HERE]
        """,
    },
    {
        "used": "Code in to Multiple Methods",
        "description": """
        Refactor the following code into multiple methods to improve readability and maintainability:

        [INSERT YOUR CODE HERE]
        """,
    },
    {
        "used": "Better Performance",
        "description": """
        Refactor the following code to improve performance:

        [INSERT YOUR CODE HERE]
        """,
    },
    {
        "used": "Follow coding style guidelines",
        "description": """
        Review the following code and refactor it to make it more DRY and adopt the SOLID programming principles.

        [INSERT YOUR CODE HERE]
        """,
    },
    {
        "used": "Detecting and Fixing Errors",
        "description": """
        Prompt 1#:
        Review this code for errors and refactor to fix any issues:

        [INSERT YOUR CODE HERE]
        
        Prompt 2#:
        I'm developing software in [INSERT YOUR TECHNOLOGIES HERE] and I need you help me to find and fix all the errors in my code, following the best practices. I'll provide you my code
        and you'll give me the code with all the corrections explained line by line

        Prompt 3#:
        I wrote this code [CODE] I got this error [ERROR] How can I fix it? or What does this error mean?
        """,
    },
    {
        "used": "Create Unit Tests",
        "description": """
        Prompt 1#:
        Please write unit tests for [file or module name] to ensure its proper functioning

        [insert code here]
        
        Prompt 2#:
        Create 2 unit tests for the provided code. One for a successful condition and one for failure.
        """,
    },
    {
        "used": "Create Functions",
        "description": """
        Prompt 1#:
        Context: I'm creating a software to manage projects
        Technologies: Go, PostgreSQL
        Description: It's a function that let me find users by its email or username.
        You have to: create the function for me
        """,
    },
    {
        "used": "You are a world-class software engineer",
        "description": """
        You are a world-class software engineer.

        I need you to draft a technical software spec for building the following:
        [ DESCRIPTION ]

        Think through how you would build it step by step.

        Then, respond with the complete spec as a well-organized markdown file.

        I will then reply with "build," and you will proceed to implement the exact spec, writing all of the code needed. I will periodically interject with "continue" to >prompt you to keep going. Continue until complete.
        """,
    },
    {
        "used": "Error Hendling",
        "description": """
        How can I improve the error handling in my [LANGUAGE] code? [CODE]
        """,
    },
    {
        "used": "Suggest Improvements",
        "description": """
        I'm working on a [LANGUAGE] project and I need you to review my code and suggest improvements. [CODE]
        """,
    },
    {
        "used": "Create an actionable marketing plan",
        "description": """
        Develop a marketing plan for [insert product or service]. 

        Include objectives, target audience, marketing channels, and tactics for reaching my desired    audience and driving sales.
        """,
    },
    {
        "used": "Leverage content marketing for lead generation",
        "description": """
        Develop a content marketing strategy for [insert business] to attract, engage, and convert leads into customers.
        """,
    },
    {
        "used": "Example Prompt for dbdiagram.io",
        "description": """
        Create an Entity-Relationship Diagram (ERD) in dbdiagram.io with the following tables:
        """,
    }
]
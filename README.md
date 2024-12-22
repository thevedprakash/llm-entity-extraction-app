project/
│
├── app.py                        # FastAPI main application entry
├── Dockerfile                    # Dockerfile to build the container
├── requirements.txt              # Required Python libraries
├── src/
│   ├── __init__.py               # Package initialization
│   ├── model_loader.py           # vLLM model loader
│   ├── entity_extraction.py      # Functions for entity extraction
│   └── prompts.py                # Predefined prompts for different use cases
│
├── static/
│   ├── index.html                # Web interface HTML file
│   └── script.js                 # JavaScript to interact with API
│
└── templates/                    # For any optional templating if needed

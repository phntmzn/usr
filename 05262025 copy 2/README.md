This project showcases a Python-based application for parsing and manipulating MIDI files. It provides a modular codebase, a Flask-powered web interface for uploading and processing `.mid` files, and tools for auto-generating Python functions from MIDI data. All required source code, documentation, and configuration files are included to help you build, run, and extend the application.
## Recent Updates

- **Raw MIDI Parsing:** Replaced external dependencies like `mido` with a custom parser using Python's `struct` module.
- **Flask Web Interface:** Added a web interface for uploading `.mid` files and dynamically generating Python function code.
- **Improved Modularity:** Refactored code to separate MIDI parsing, code generation, and Flask routing for better reusability and testing.
- **Auto-Generated Functions:** Now outputs Python functions (e.g., `drumpatterns()`) to streamline MIDI manipulation workflows.

## Key Features

- Modular and maintainable codebase
- Comprehensive setup and usage documentation
- Example files demonstrating core functionality

**Getting Started:**  
Review this README and follow the setup instructions. For detailed explanations, see inline code comments and additional documentation in the project directory.
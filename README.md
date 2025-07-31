# Library Organizer (Python + SQL)

A command-line interface (CLI) application developed in Python to help manage a personal collection of books. This project aims to provide a robust foundation for learning and applying Domain-Driven Design (DDD) principles, SQL database interactions, and effective Git/GitHub version control practices, including Continuous Integration (CI) with GitHub Actions.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture (Domain-Driven Design - DDD)](#architecture-domain-driven-design---ddd)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Development Workflow](#development-workflow)
  - [GitHub Issues & Projects](#github-issues--projects)
  - [Version Control (Git)](#version-control-git)
  - [Continuous Integration (GitHub Actions)](#continuous-integration-github-actions)
- [License](#license)
- [Contributing](#contributing)

## Project Overview

This project is a personal endeavor to build a comprehensive system for managing books. It starts as a simple CLI application, focusing on core functionalities like adding, listing, searching, and removing books. The goal is to gradually expand its capabilities, incorporating more complex features and potentially transitioning to a web-based interface as advanced concepts are learned.

## Features

### Current (MVP - Version 1.0)

- **Add Book:** Register new books with title, author, publication year, genre, ISBN, and reading status.
- **List Books:** Display all registered books in a clear, formatted list.
- **Search Books:** Find books by title or author.
- **Remove Book:** Delete books from the collection.

### Planned Features (Future Phases)

- Detailed Author and Genre management.
- Advanced search and filtering options.
- Reading status tracking and reporting.
- User management and authentication.
- Transition from SQLite to PostgreSQL/MySQL.
- Development of a RESTful API using Flask.
- Potential web-based UI or graphical desktop application.

## Architecture (Domain-Driven Design - DDD)

The project is structured following Domain-Driven Design (DDD) principles to ensure a clear separation of concerns, maintainability, and scalability.

- **`src/domain/`**: Contains the core business logic (entities, value objects, domain services).
  - `entities/`: `Book`, `Author`, `Genre`.
  - `value_objects/`: `ISBN`, `ReadingStatus`.
  - `services/`: `BookManager`.
- **`src/application/`**: Orchestrates domain logic to fulfill use cases.
  - `book_service.py`: Interacts with domain services and repositories.
- **`src/infrastructure/`**: Handles technical details like database access.
  - `database/`: SQLite connection (`sqlite_connector.py`), SQL scripts (`create_tables.sql`).
  - `repositories/`: `BookRepository`, `AuthorRepository`, `GenreRepository` (implementing data persistence).
- **`src/ui/`**: Manages user interaction.
  - `cli_app.py`: Command-Line Interface.

## Technologies Used

- **Python 3.x**
- **SQLite3** (for local database storage)
- **`sqlite3`** (Python's built-in SQLite adapter)
- **`pytest`** (for testing)

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/library-organizer-python-sql.git
   cd library-organizer-python-sql
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**

   On **Windows**:
   ```bash
   .venv\Scripts\activate
   ```

   On **macOS/Linux**:
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the CLI application:

```bash
python src/ui/cli_app.py
```

## Development Workflow

This project utilizes various GitHub features and best practices for development.

### GitHub Issues & Projects

Development tasks, bug fixes, and feature enhancements are tracked using GitHub Issues and organized on a GitHub Project board.

### Version Control (Git)

- **Branching:** Features are developed in separate branches (e.g., `feature/add-book-cli`).
- **Commits:** Commits are atomic and follow a conventional format (e.g., `feat: Add book entity`, `fix: Correct data validation bug`).
- **Pull Requests:** Changes are merged into `main` via Pull Requests.

### Continuous Integration (GitHub Actions)

A CI pipeline is set up using GitHub Actions to automatically run tests on every push to `main` and on Pull Requests, ensuring code quality and preventing regressions.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions, bug reports, or want to contribute.

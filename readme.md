# 1337x FastAPI Wrapper

## Overview

This project provides a FastAPI wrapper for the unofficial 1337x API, allowing you to easily integrate 1337x torrent functionality into your Python applications.

## Features

- Search for torrents based on various parameters.
- Get trending, top, and popular torrents.
- Browse torrents by category.
- Retrieve detailed information about a specific torrent.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mudabbirulsaad/1337x-wrapper.git
   cd 1337x-wrapper
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

2. The FastAPI application will be running at `http://127.0.0.1:8000`.

## Usage

### Searching for Torrents

Endpoint: `/search`

```bash
curl -X POST "http://127.0.0.1:8000/search" -d '{"query": "your_search_query"}'
```

### Getting Trending Torrents

Endpoint: `/trending`

```bash
curl -X POST "http://127.0.0.1:8000/trending" -d '{"category": "your_category"}'
```

### Getting Top Torrents

Endpoint: `/top`

```bash
curl -X POST "http://127.0.0.1:8000/top" -d '{"category": "your_category"}'
```

### Getting Popular Torrents

Endpoint: `/popular`

```bash
curl -X POST "http://127.0.0.1:8000/popular" -d '{"category": "your_category"}'
```

### Browsing Torrents by Category

Endpoint: `/browse`

```bash
curl -X POST "http://127.0.0.1:8000/browse" -d '{"category": "your_category", "page": 1}'
```

### Retrieving Torrent Information

Endpoint: `/info`

```bash
curl -X POST "http://127.0.0.1:8000/info" -d '{"torrentId": 12345}'
```

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and collaboration are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).

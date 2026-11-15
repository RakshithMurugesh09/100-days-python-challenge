# Day 46 - Pytest Testing & Spotify Playlist Musical

Day 46 of my Python learning challenge focuses on two areas: **automated testing with Pytest** and **working with the Spotify Web API using Spotipy**.

## Project Structure

```text
Day_46/
|-- pytest Test/
|   |-- main.py
|   `-- test_main.py
|
`-- Spotify Playlist Musical/
    |-- main.py
    |-- spotify.py
    `-- spotify.env
```

## 1. Pytest Test

This section is used to practice writing and running automated tests with **Pytest**.

### Files
- `main.py` - contains the Python functionality being tested.
- `test_main.py` - contains the Pytest test cases.

### Run the tests

```bash
pytest -v
```

## 2. Spotify Playlist Musical

This project practices using **Spotipy**, a Python library for the Spotify Web API. The application can authenticate with Spotify and search for tracks programmatically.

### Files
- `main.py` - main program logic.
- `spotify.py` - Spotify-related code/helper logic.
- `spotify.env` - stores Spotify API credentials locally.

### Environment Variables

The `spotify.env` file can contain:

```env
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
```

Load the custom environment file with:

```python
from dotenv import load_dotenv

load_dotenv("spotify.env")
```

## Installation

```bash
pip install spotipy python-dotenv pytest
```

## Important - Protect Spotify Credentials

Never commit `spotify.env` to GitHub because it contains the Spotify Client Secret.

Add this to `.gitignore`:

```gitignore
spotify.env
```

If the credentials have already been committed to a public repository, rotate the Spotify Client Secret in the Spotify Developer Dashboard.

## What I Practiced

- Writing tests using Pytest
- Running automated Python tests
- Using environment variables for secrets
- Authenticating with the Spotify Web API
- Searching Spotify tracks using Spotipy
- Keeping API credentials out of Git

## Day 46 Goal

Build confidence with automated testing while learning how Python applications securely authenticate with external APIs such as Spotify.

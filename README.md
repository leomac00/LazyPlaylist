# Spotify LazyPlaylist Creator

This application uses the Spotify API to create playlists from a provided list of tracks. It allows you to create a new playlist on Spotify and add tracks to it.

## Requirements

- Python 3.7 or higher
- `spotipy` library
- JSON configuration file with Spotify authentication details
- Text file with a list of tracks to be added to the playlist

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/leomac00/LazyPlaylist.git
   cd LazyPlaylist
   ```

2. **Install the dependencies**

   Make sure `pip` is installed and run:

   ```bash
   pip install spotipy
   ```

## Configuration

1. **Create a `config.json` file**

   Create a `config.json` file in the `resources` directory with the following format:

   ```json
   {
      "authentication": {
         "client_id": "your_client_id_here",
         "client_secret": "your_client_secret_here",
         "redirect_uri": "your_redirect_uri",
         "scope": "playlist-modify-public"
      },
      "user_data": {
         "username": "your_spotify_username_here",
         "playlist_name": "your_playlist_name_here"
      }
   }
   ```

   - `client_id`: Spotify Client ID.
   - `client_secret`: Spotify Client Secret.
   - `redirect_uri`: Redirect URI configured in the Spotify Developer Dashboard.
   - `scope`: Permissions scope requested for the application.
   - `username`: Your Spotify username.
   - `playlist_name`: Desired name for the new playlist.

2. **Create a `tracks.txt` file**

   Create a `tracks.txt` file in the `resources` directory with a list of tracks, one per line. For example:

   ```
    Fool's Overture - Supertramp
    Pink Moon - Nick Drake
    Dear Mr. Fantasy - Traffic
   ```

## Usage

1. **Update the config.json**

   In the `config.json` file, replace the dummy data mentioned above with the actual data you'll need to use.

2. **Run the script**

   ```bash
   python3 app.py
   ```

   This will create a new playlist on Spotify with the tracks listed in the `tracks.txt` file.

## Notes

- Ensure that the tracks in the `tracks.txt` file match the tracks available on Spotify so they can be added to the playlist.
- The application uses the `spotipy` library to interact with the Spotify API. More information about the library can be found [here](https://spotipy.readthedocs.io/en/2.16.1/).

## License

This project is licensed under the [MIT License](LICENSE).
```

### Explanation:
- **Requirements**: Lists the minimum versions and libraries needed.
- **Installation**: Steps to clone the repository and install dependencies.
- **Configuration**: Instructions for setting up necessary files.
- **Usage**: How to update the script and run it.
- **Notes**: Additional information and references.
- **License**: Type of license used for the project.

Feel free to adjust this according to your specific project and needs.
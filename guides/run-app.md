## How to run

1. Clone the repository to your local machine

```bash
git clone https://github.com/petterssonb/yt-mp3-converter-py.git
```

2. Navigate to the project directory.

```bash
cd yt-mp3-converter-py
```

3. Install the required Python dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

4. Follow the setup guide to connect the ***Spotify API*** (Complete the whole setup guide before moving on to running the app)

[Setup Guide](/guides/setup-guide.md)

5. Run the app
```bash
python main.py
```

- Using the Application

    - Enter the URL of the YouTube video you wish to download.
	- Click the “Download” button.
	- The application will download and convert the video to MP3 format.
	- The downloaded MP3 file will be saved in your spotify local files folder.
	- If the song matches a song on spotify you can add it to your playlist from the drop down menu
	- Or if it isn't on spotify enter the local files folder in spotify and add the song to your playlist
  
  ***If you don't have local files enabled in spotify:***

   - Click on ***settings*** in spotify
   - And scroll down until you see this (***see image below***) and enable local files:

    ![](/images/spotify.jpg)
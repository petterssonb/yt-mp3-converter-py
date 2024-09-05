# Setup Guide

## Prerequisites
Before you run the YouTube to MP3 converter app, make sure you have installed the required dependencies and set up your Spotify API credentials.

## 1. Install the Dependencies

Make sure ffmpeg is also installed on your system. Follow the instructions for your operating system:

 - ***macOS:*** Install with Homebrew ([install homebrew](https://www.youtube.com/watch?v=IWJKRmFLn-g)):
```bash
brew install ffmpeg
```

- ***Ubuntu/Linux:*** Install with apt:
```bash
sudo apt update
sudo apt install ffmpeg
```

- ***Windows:*** Download and install ***ffmpeg*** from the [FFmpeg website](https://www.ffmpeg.org/), and ensure it's added to your system's PATH.


## 2. Set Up Spotify API Credentials

To integrate with Spotify, you will need to create an app on the Spotify Developer Dashboard to get your ***Spotify Client ID***, ***Client Secret***, and set the ***Redirect URI***.

***Steps to Get Spotify Credentials***

 1. ***Visit the*** [Spotify Developer Dashboard](https://developer.spotify.com/) and log in with you Spotify account. If you don't have an account, create one first.

 2. ***Create an App:***
    - Click on “Create an App”.
  
	- Fill in the “App Name” (e.g., “YouTube to MP3 Converter”) and “App Description” (e.g., “App to convert YouTube videos to MP3 and add them to Spotify”).
  
	- Click Create to finish.

3. ***Get Client ID and Client Secret:***
	 - After creating the app, you will be taken to the app dashboard.
  
	 - Here, you will find the ***Client ID*** and ***Client Secret***. Copy these values, as you’ll need them in the next step.

4. ***Set Redirect URI:***
	 - In your app’s dashboard, click ***Edit Settings***.
  
	 - Under ***Redirect URIs***, add the following URI: http://localhost:8888/callback
  
	 - Click ***Save*** to apply the changes.


## 3. Set Environment Variables
Once you have obtained your Spotify credentials (Client ID, Client Secret), you’ll need to set them as environment variables on your system.

***On macOS and Linux:***

You can set environment variables by adding the following lines to your terminal or your shell configuration file (e.g., ~/.bashrc, ~/.zshrc, or ~/.bash_profile):
```bash
export SPOTIPY_CLIENT_ID='your_spotify_client_id'
export SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
```

After adding these lines, run the following command to apply the changes.
```bash
source ~/.zshrc # or source ~/.bashrc for bash users
```

***On Windows:***

You can set environment variables by following these steps:

1. Open the ***Start Menu*** and search for ***Environment Variables.***

2.	Select ***Edit the system environment variables***.

3.	In the ***System Properties*** window, click ***Environment Variables***.
4.	Under ***User variables***, click ***New*** and add the following variables:

 - ***Variable name***: SPOTIPY_CLIENT_ID
Value: ***Your Spotify Client ID***.
- ***Variable name***: SPOTIPY_CLIENT_SECRET
Value: ***Your Spotify Client Secret***.
- ***Variable name***: SPOTIPY_REDIRECT_URI
 Value: http://localhost:8888/callback.

- Click ***OK*** to save the changes and close the dialogs.

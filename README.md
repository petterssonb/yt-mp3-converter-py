# Youtube to mp3 converter

## Overview

The YouTube Downloader GUI is a Python-based application that allows users to download YouTube videos as MP3 files. The application is built with a modern interface using customtkinter and leverages yt-dlp for downloading and converting videos. The interface is designed to be user-friendly and provides real-time progress updates during the download process.

Compatibility Note: This application is compatible with Windows, Linux, and macOS. Follow the instructions in the “How to run” section to properly set up and run the program.

## Purpose

Always wanted to use a "converter app" to add songs from yt to my spotify playlist. So made this for fun and to play around with customtkinter which is a more modern version of tkinter.
Will add more functionality in the future so keep a heads up for updates :)

Click the link below to see the customtkinter repo for yourself:

[CustomTkinter Repo](https://github.com/TomSchimansky/CustomTkinter)


## User interface

<img src="images/image1.jpg" alt="UI Screenshot 1" width="400"/>

<img src="images/download.jpg" alt="Download Screenshot" width="400"/>

<img src="images/downloaded.jpg" alt="Downloaded Screenshot" width="400"/>


## Features

 - Download YouTube Videos as MP3: Enter the URL of a YouTube video to download and convert it to an MP3 file.
 - Progress Display: A progress bar and percentage indicator track the download status.
 - Modern UI: Utilizes customtkinter to offer a sleek and modern graphical user interface.
 - Cross-Platform: The application runs smoothly on Windows, macOS, and Linux.


## How to run

1. Clone the repository to your local machine

```bash
git clone https://github.com/petterssonb/yt-mp3-converter-py.git
```

2. Navigate to the project directory.

```bash
cd yt-mp3-converter-py
```

3. Install the required Python packages
```bash
pip install -r requirements.txt
```

4. 	Using the Application

    - Enter the URL of the YouTube video you wish to download.
	- Click the “Download” button.
	- The application will download and convert the video to MP3 format.
	- The downloaded MP3 file will be saved in your system’s Downloads folder.

LICENSE

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
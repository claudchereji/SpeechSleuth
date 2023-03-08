# SpeechSleuth :speech_balloon: :mag:


![Project Image](https://github.com/claudchereji/SpeechSleuth/blob/main/Untitled_Artwork1_11.png?raw=true)


SpeechSleuth is a powerful tool that utilizes yt-dlp to retrieve auto-generated subtitles from any YouTube channel that the user chooses. These subtitles are then converted from VTT to plain text, with most of the time codes removed. This plain text is then formatted into Markdown for a clean, easy-to-read layout. Finally, each segment of the Markdown file is analyzed by OpenAI for paragraph summarization, allowing for quick indexing and search functionality.

## Prerequisites

Before using SpeechSleuth, you will need to have the following installed:

    Python 3.6 or later
    vtt2text.py
    yt-dlp
    An OpenAI API key

## Installation

Clone the SpeechSleuth repository to your local machine. 
```https://github.com/claudchereji/SpeechSleuth.git```
or
[Download the zip file](https://github.com/claudchereji/SpeechSleuth/archive/refs/heads/main.zip)
Install the required Python packages by running pip install openai in the command line.
Set up your OpenAI API key as an environment variable by setting the OPENAI_API_KEY variable to your key.

## Usage

To use SpeechSleuth, simply run the speechsleuth.py script.


Once you have run the script, a Markdown file will be generated containing the formatted subtitles and summarizations for each segment.


## Contributing

If you find a bug or have a suggestion for how to improve SpeechSleuth, please submit an issue or pull request on the GitHub repository.
License

SpeechSleuth is OpenSource and CopyLeft

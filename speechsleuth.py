import os
import shutil
from pathlib import Path
import openai
import concurrent.futures
from pathlib import Path
from tqdm import tqdm
import subprocess
import re

video_url = input('Enter YouTube video URL: ')

# Define the yt-dlp command as a list of arguments
cmd = ['yt-dlp', '--write-auto-sub', '--sub-format', 'vtt', '--skip-download', video_url]

# Use subprocess to run the command
subprocess.run(cmd)

dir_path = '/home/claud/Desktop/fullScriptTest'

# Find all VTT files in the directory and execute vtt2text.py on each file
os.system('find {} -name "*.vtt" -exec python3 vtt2text.py {{}} \;'.format(dir_path))

# Specify the directory path containing the markdown files
directory = Path('/home/claud/Desktop/fullScriptTest')

# this for loop will cause a loading bar to appear in the terminal
for file_path in tqdm(directory.glob('*.txt'), desc='Processing files', unit='file'):
    # Your code for processing each file goes here

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a text file (ends with .txt)
        if filename.endswith('.txt'):
            # Join the directory path with the filename
            file_path = os.path.join(directory, filename)
            # Read the contents of the file
            with open(file_path, 'r') as file:
                content = file.read()
            # Use regular expression to split the text at every time code with format "00:02"
            segments = re.findall(r'((?:.*?\d{2}:\d{2}.*?){1}|.+)', content, flags=re.DOTALL)
            # Add two new lines before each time code and combine all the text in each segment into a single line
            segments_with_newlines = ['\n\n' + ' '.join(segment.split('\n')).replace('\r', '') if re.match(r'.*\d{2}:\d{2}.*', segment) else segment for segment in segments]
            # Join the segments back into a string
            new_content = ''.join(segments_with_newlines)
            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.write(new_content)

# Loop through each file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a text file (ends with .txt)
        if filename.endswith('.txt'):
            # Create a new filename by replacing the .txt extension with .md
            new_filename = os.path.splitext(filename)[0] + '.md'
            # Join the directory path with the original filename
            original_file_path = os.path.join(directory, filename)
            # Join the directory path with the new filename
            new_file_path = os.path.join(directory, new_filename)
            # Use the shutil library to copy the original file to the new file
            shutil.copy(original_file_path, new_file_path)


    # Specify the directory path containing the markdown files
    directory = Path('/home/claud/Desktop/fullScriptTest')

# Loop through each file in the directory
for file_path in directory.glob('*.md'):
    # Read the contents of the file
    with file_path.open('r') as file:
        content = file.read()

        # Split the content into segments based on the time code pattern
        segments = re.split(r'\n(\d{2}:\d{2})', content)
        text_segments = []
        for i, segment in enumerate(segments):
            # Ignore the time code segments
            if i % 2 == 0:
                text_segments.append(segment.strip())

         # Split the content into segments based on time codes
        segments = re.split(r'(\d{2}:\d{2})', content)

         # Add 2 new lines after each segment and combine all the text in each segment into a single line
        segments_with_newlines = [' '.join(segment.split('\n')).replace('\r', '') + '\n\n' for segment in segments]

        # Join the updated segments back into a string
        new_content = '\n'.join(segments_with_newlines)

        # Write the updated content back to the file
        with file_path.open('w') as file:
            file.write(new_content)


    # Set up OpenAI API key
    openai.api_key = "YOUR_API_KEY"

    # Specify the directory path containing the markdown files
    directory = '/home/claud/Desktop/fullScriptTest'

    # Set up OpenAI summarization parameters
    model_engine = "text-davinci-002"
    max_tokens = 20
    temperature = 0.9
    n = 1
    stop = '###'

        
    # Define a function to summarize a single segment
    def summarize(segment):
        response = openai.Completion.create(
            engine=model_engine,
            prompt=("Summarize this in the most concise way possible: ")+ content,
            max_tokens=max_tokens,
            temperature=temperature,
            n=n,
            stop=stop
        )
        summary = response.choices[0].text.strip()
        header = f'## {summary}\n\n'
        return header + segment


    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a markdown file (ends with .md)
        if filename.endswith('.md'):
            # Join the directory path with the filename
            file_path = os.path.join(directory, filename)
            # Read the contents of the file
            with open(file_path, 'r') as file:
                content = file.read()
            # Split the content into segments
            segments = content.split('\n\n')
            # Summarize each segment using multithreading
            with concurrent.futures.ThreadPoolExecutor() as executor:
                summarized_segments = list(executor.map(summarize, segments))
            # Join the summarized segments back together
            new_content = '\n\n'.join(summarized_segments)
            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.write(new_content)
                
# delete all .txt and .vtt files in the current directory
os.system("rm *.txt *.vtt")

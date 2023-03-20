# Import the required libraries
import requests
import os

# Define a function to download Wikipedia abstracts
def download_wikipedia_abstracts():
    # Set the URL to download the latest Wikipedia abstracts XML file
    URL = 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz'
    
    # Check if the "data" directory esxists, and if not, create it
    os.makedirs('data', exist_ok=True)
    
    # Try to download the file and handle exceptions
    try:
        # Send an HTTP request to the URL to download the file as a stream
        with requests.get(URL, stream=True) as r:
            # Raise an exception if the HTTP request fails
            r.raise_for_status()
            
            # Open the output file in binary write mode
            with open('data/enwiki-latest-abstract.xml.gz', 'wb') as f:
                # Iterate through the content in chunks of 1 MB
                for i, chunk in enumerate(r.iter_content(chunk_size=1024*1024)):
                    # Write the current chunk to the output file
                    f.write(chunk)
                    
                    # Print a progress update every 10 MB
                    if i % 10 == 0:
                        print(f'Downloaded {i} megabytes', end='\r')
    # Catch and print any exceptions that occur during the download process
    except Exception as e:
        print(f"An error occurred: {e}")

# If this script is being run as the main module, call the download_wikipedia_abstracts function
if __name__ == '__main__':
    download_wikipedia_abstracts()

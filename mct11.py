import webbrowser
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

def download_file(url, filename):
    """Downloads a file from a URL, handling potential errors."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):  # 8KB chunks
                file.write(chunk)
        print(f"Successfully downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None  # Explicitly return None on error
    except Exception as e:
        print(f"An unexpected error occurred while downloading {url}: {e}")
        return None
    return filename # Return downloaded file name

def open_windows_11_download_page():
    """Opens the official Windows 11 download page and attempts to locate and download the Media Creation Tool."""
    windows_11_download_url = "https://www.microsoft.com/nl-nl/software-download/windows11"

    print("Opening the official Windows 11 download page in your web browser...")
    webbrowser.open_new_tab(windows_11_download_url)
    print("Attempting to download the Media Creation Tool automatically...")

    #  Direct download URL for Media Creation Tool.
    download_link = "https://go.microsoft.com/fwlink/?linkid=2156295" # Changed to provided link

    try:
        # Construct absolute URL if necessary
        if not download_link.startswith(('http://', 'https://')):
            download_link = urllib.parse.urljoin(windows_11_download_url, download_link)

        print(f"Found Media Creation Tool download link: {download_link}")
        filename = "MediaCreationTool.exe" #  Fixed filename
        downloaded_file = download_file(download_link, filename)
        if downloaded_file:
            print(f"Media Creation Tool downloaded to: {downloaded_file}")
            return  # Exit the function after successful download
        else:
            print("Download failed. Please download manually from the website.")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing the download page: {e}")
        print("Please visit the page manually to download the Media Creation Tool.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please download the Media Creation Tool manually.")

if __name__ == "__main__":
    open_windows_11_download_page()
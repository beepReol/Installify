import requests
import os

def download_file(url, filename):
    """Downloads a file from a URL, handling potential errors."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Successfully downloaded: {filename}")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while downloading {url}: {e}")
        return None
    return filename

def download_windows_10_mct():
    """Downloads the Windows 10 Media Creation Tool."""
    download_url = "https://go.microsoft.com/fwlink/?LinkId=2265055"
    filename = "MediaCreationToolW10.exe"
    print("Downloading Windows 10 Media Creation Tool...")
    try:
        downloaded_file = download_file(download_url, filename)
        if downloaded_file:
            print(f"Media Creation Tool downloaded to: {downloaded_file}")
        else:
            print("Download failed. Please download the Windows 10 Media Creation Tool manually.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please download the Windows 10 Media Creation Tool manually.")

if __name__ == "__main__":
    download_windows_10_mct()
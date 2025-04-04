import requests
import os
import time

def download_file(url, filename):
    """Downloads a file from a URL, handling potential errors and provides a detailed progress.

    Args:
        url (str): De URL van het bestand dat gedownload moet worden.
        filename (str): De naam waaronder het bestand opgeslagen moet worden.
    """
    try:
        print(f"Downloading from: {url}")
        # Use a session for connection pooling
        with requests.Session() as session:
            response = session.get(url, stream=True, allow_redirects=True)  # Volg redirects
            response.raise_for_status()  # Check for download errors

            total_size_in_bytes = int(response.headers.get('content-length', 0))
            bytes_downloaded = 0
            chunk_size = 1024 * 1024  # 1MB chunk size
            start_time = time.time()  # Start time for ETA calculation

            if total_size_in_bytes:
                print(f"Total file size: {total_size_in_bytes / (1024 * 1024):.2f} MB")  # Display total size

            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        file.write(chunk)
                        bytes_downloaded += len(chunk)
                        elapsed_time = time.time() - start_time
                        if total_size_in_bytes:
                            percentage = (bytes_downloaded / total_size_in_bytes) * 100
                            # Calculate ETA
                            if bytes_downloaded > 0:
                                estimated_time_seconds = (total_size_in_bytes - bytes_downloaded) / (bytes_downloaded / elapsed_time)
                                estimated_time_minutes = estimated_time_seconds / 60
                                print(f"Downloaded {percentage:.2f}%, {bytes_downloaded / (1024 * 1024):.2f} MB, ETA: {estimated_time_minutes:.2f} min", end='\r')
                            else:
                                print(f"Downloaded {percentage:.2f}%, {bytes_downloaded / (1024 * 1024):.2f} MB", end='\r')
                        else:
                            print(f"Downloaded {bytes_downloaded / (1024 * 1024):.2f} MB, Elapsed: {elapsed_time:.0f} sec", end='\r')

            print(f"Successfully downloaded: {filename}")
            return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def download_ubuntu_iso():
    """Downloads the Ubuntu ISO from the specified URL."""
    ubuntu_url = "https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-desktop-amd64.iso?_ga=2.114383175.1975303594.1743798096-640975423.1740070537&_gl=1*st2lqm*_gcl_au*NDE3MTUzNTQ1LjE3NDAwNzA1Mzk."
    filename = "ubuntu-24.04.2-desktop-amd64.iso"

    print(f"Downloading Ubuntu ISO: {filename}")
    downloaded_file = download_file(ubuntu_url, filename)

    if downloaded_file:
        print(f"Ubuntu ISO downloaded to: {downloaded_file}")
    else:
        print("Download failed. Please download the Ubuntu ISO manually.")

if __name__ == "__main__":
    download_ubuntu_iso()


from chromeversion import get_chrome_version
from downloader import download_chrome_driver

if __name__ == '__main__':
    chrome_version = get_chrome_version()
    download_chrome_driver(chrome_version)

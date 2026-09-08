import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Web page URL
url = "https://news.ycombinator.com/"

# Send request to the web page
response = requests.get(url)

# Check whether request was successful
if response.status_code == 200:

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    print("NEWS HEADLINES AND HYPERLINKS")
    print("=" * 60)

    # Find news headlines
    headlines = soup.find_all("span", class_="titleline")

    for i, headline in enumerate(headlines, start=1):

        # Find the hyperlink inside the headline
        link = headline.find("a")

        if link:
            title = link.get_text(strip=True)
            href = link.get("href")

            # Convert relative URLs to absolute URLs
            full_url = urljoin(url, href)

            print(f"{i}. {title}")
            print(f"   Link: {full_url}")
            print()

else:
    print("Failed to retrieve the web page.")
    print("Status code:", response.status_code)

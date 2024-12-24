import requests
from bs4 import BeautifulSoup # type: ignore
from config import TARGET_URL

def scrape_web_content() -> str:
    """
    주어진 URL에서 텍스트 콘텐츠를 추출합니다.

    Args:
        url (str): 크롤링할 웹 페이지 URL

    Returns:
        str: 텍스트 콘텐츠
    """
    response = requests.get(TARGET_URL)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch URL: {TARGET_URL}, Status Code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text(strip=True)

from data_collection.file_explorer import list_files
from data_collection.web_scraper import scrape_web_content
from data_collection.api_fetcher import fetch_api_data

def main():
    # 파일 탐색
    files = list_files()
    print("Found files:", files)
    
    # 웹 크롤링
    content = scrape_web_content()
    print("Web Content:", content)
    
    # API 데이터 수집
    api_data = fetch_api_data()
    print("API Data:", api_data)

if __name__ == "__main__":
    main()

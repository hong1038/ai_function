# __init__.py

import os

# 패키지 초기화 메시지
print(f"Initializing data_collection package. Current directory: {os.getcwd()}")

# 패키지 모듈 가져오기
from .file_explorer import list_files
from .web_scraper import scrape_web_content
from .api_fetcher import fetch_api_data

# 외부에서 접근 가능한 함수 정의
__all__ = [
    "list_files",
    "scrape_web_content",
    "fetch_api_data",
]

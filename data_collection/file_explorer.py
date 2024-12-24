import os
from config import DIRECTORY_TO_SEARCH, ALLOWED_EXTENSIONS

def list_files() -> list:
    """
    특정 디렉토리에서 주어진 확장자의 파일 목록을 반환합니다.

    Args:
        DIRECTORY_TO_SEARCH (str): 탐색할 디렉토리 경로
        ALLOWED_EXTENSIONS (list): 허용할 파일 확장자 리스트 (예: ['.txt', '.pdf'])

    Returns:
        list: 파일 경로 리스트
    """
    if not os.path.exists(DIRECTORY_TO_SEARCH):
        raise FileNotFoundError(f"Directory not found: {DIRECTORY_TO_SEARCH}")
    
    files = []
    for root, _, filenames in os.walk(DIRECTORY_TO_SEARCH):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                files.append(os.path.join(root, filename))
    return files

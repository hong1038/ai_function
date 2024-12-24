import requests
from config import API_ENDPOINT, API_PARAMS

def fetch_api_data() -> dict:
    """
    주어진 API 엔드포인트에서 데이터를 가져옵니다.

    Args:
        API_ENDPOINT (str): API URL
        API_PARAMS (dict): API 요청에 필요한 파라미터 (기본값: None)

    Returns:
        dict: API 응답 데이터
    """
    response = requests.get(API_ENDPOINT, params=API_PARAMS)
    if response.status_code != 200:
        raise Exception(f"API request failed: {API_ENDPOINT}, Status Code: {response.status_code}")
    
    return response.json()

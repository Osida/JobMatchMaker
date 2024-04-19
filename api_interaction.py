import requests

def make_post_request(api_url, request_data):
    try:
        api_response = requests.post(api_url, json=request_data)
        api_response.raise_for_status()
        return api_response.json()
    except requests.exceptions.HTTPError:
        print(f'HTTP error occurred while making a request to {api_url}.')
    except requests.exceptions.ConnectionError:
        print('Connection error occurred. Please check your internet connection.')
    except requests.exceptions.Timeout:
        print(f'Request to {api_url} timed out.')
    except requests.exceptions.RequestException as request_error:
        print(f'An error occurred while making a request to {api_url}: {request_error}')
    return None

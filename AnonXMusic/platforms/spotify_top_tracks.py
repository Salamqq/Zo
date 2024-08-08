import requests

# Authorization token
token = 'BQDLcL6fQ_yCxJswYTBu3dHz-a_PCQDUoPgKkooOoVaT1eRNEXBRT6etZIY71Y4UnyLCr3vrfwsjT-43YZ0R5y8wdmrQKyGmrOXxBkTnZ-HbIZOJctH0CSAMPi6qwAan7mIXx8-YGhtFd9-EK7BWcfBlbRj2UPt2YbvVTkgYoxz0NIifTQa4a4o84vr_xJUlHtSLWT4lGU3-loKhsdkIzXMwZmzahnfRDtSMwnPP03qUydWkdtYDNYFco4UKlq3sBK4G_mUaFDxwEVHSnr79ITDrbdf3KQ'

def fetch_web_api(endpoint, method, body=None):
    url = f'https://api.spotify.com/{endpoint}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.request(method, url, headers=headers, json=body)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def get_top_tracks():
    endpoint = 'v1/me/top/tracks?time_range=long_term&limit=5'
    response = fetch_web_api(endpoint, 'GET')
    if response:
        return response['items']
    return []

top_tracks = get_top_tracks()
if top_tracks:
    for track in top_tracks:
        name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        print(f"{name} by {artists}")
else:
    print("No top tracks found.")

import requests
import xml.dom.minidom
import json
#josn, requests는 pip install 필요할수도

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {e}"

def format_xml(xml_string):
    dom = xml.dom.minidom.parseString(xml_string)
    pretty_xml = dom.toprettyxml()
    return pretty_xml

# 특정 URL 설정
url = ""

result = fetch_url(url)

# 응답이 XML 형식일 경우 포맷팅
if result.startswith("<?xml"):
    result = format_xml(result)

print(result)

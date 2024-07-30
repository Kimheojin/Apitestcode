import requests
import json
import csv
import os

# 사용자 정의 변수
ttbkey = ""
MaxResults = 50
QueryType = "BlogBest"
csv_filename = "BlogBest.csv"
# 편집자 추천 뭐시기만 사용
# 국내도서, 외서만 가능
categoryID = "112011"
# 요청할 페이지 수
num_pages = 10

# 결과값에서 필요한 필드만 추출
filtered_books = []
seen_isbn13 = set()

for page in range(1, num_pages + 1):
    

    # URL 생성
    url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={ttbkey}&QueryType={QueryType}&MaxResults={MaxResults}&start={page}&SearchTarget=Book&output=JS&Version=20131101"

    # 요청 보내기
    response = requests.get(url)

    # 요청 성공 여부 확인
    if response.status_code == 200:
        try:
            # JSON 응답을 Python 객체로 변환
            data = response.json()

            books = data.get('item', [])

            for book in books:
                isbn13 = book.get('isbn13')
                title = book.get('title')
                description = book.get('description')
                author = book.get('author')

                # 필드가 모두 존재하고 비어있지 않은 경우만 저장
                if isbn13 and title and description and author and isbn13 not in seen_isbn13:
                    filtered_books.append({
                        'isbn13': isbn13,
                        'title': title,
                        'description': description,
                        'author': author
                    })
                    seen_isbn13.add(isbn13)

        except json.JSONDecodeError:
            print("응답을 JSON으로 디코딩하는 데 실패했습니다.")
    else:
        print(f"요청 실패: 상태 코드 {response.status_code}")

# 현재 디렉토리에 CSV 파일 저장
output_file = os.path.join(os.getcwd(), csv_filename)

# CSV 파일이 이미 존재하는지 확인
file_exists = os.path.isfile(output_file)

# CSV 파일에 데이터 저장
with open(output_file, 'a' if file_exists else 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['isbn13', 'title', 'description', 'author']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 파일이 존재하지 않는 경우에만 헤더를 작성
    if not file_exists:
        writer.writeheader()

    for book in filtered_books:
        writer.writerow(book)

print(f"데이터가 {output_file} 파일에 성공적으로 저장되었습니다.")

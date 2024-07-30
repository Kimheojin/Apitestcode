import os
import glob
import csv

# 현재 디렉토리 내의 모든 CSV 파일 찾기
csv_files = glob.glob(os.path.join(os.getcwd(), "*.csv"))

all_books = []
seen_isbn13 = set()

for file in csv_files:
    with open(file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            isbn13 = row.get('isbn13')
            title = row.get('title')
            description = row.get('description')
            author = row.get('author')

            # 필드가 모두 존재하고 비어있지 않으며, 중복되지 않은 경우만 추가
            if isbn13 and title and description and author and isbn13 not in seen_isbn13:
                all_books.append({
                    'isbn13': isbn13,
                    'title': title,
                    'description': description,
                    'author': author
                })
                seen_isbn13.add(isbn13)

# 합친 데이터를 새로운 CSV 파일로 저장
output_file = os.path.join(os.getcwd(), "merged_books.csv")

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['isbn13', 'title', 'description', 'author']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for book in all_books:
        writer.writerow(book)

print(f"모든 CSV 파일이 합쳐져서 {output_file} 파일에 저장되었습니다.")

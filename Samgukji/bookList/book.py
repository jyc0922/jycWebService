import os
print("=== SCRIPT START ===")
print("현재 경로:", os.getcwd())
print("파일 존재:", os.path.exists("bookListVer1.csv"))
import csv

csv_path = "bookListVer1.csv"
html_path = "bookListVer1.html"

html_head = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>삼국지 도서 목록</title>
    <style>
        :root {
            --primary-bg-color: #f5f1e6;
            --secondary-bg-color: #f9f6ef;
            --table-header-bg: #e0cfa4;
            --table-row-bg: #fcfaf5;
            --table-border: #bfa77a;
            --main-font: 'Nanum Myeongjo', serif;
        }
        body {
            background: var(--primary-bg-color);
            font-family: var(--main-font);
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 40px auto 40px auto;
            background: var(--secondary-bg-color);
            border-radius: 18px;
            box-shadow: 0 4px 24px 0 rgba(80,60,20,0.08);
            padding: 32px 24px;
        }
        h1 {
            text-align: center;
            font-size: 2.2rem;
            margin-bottom: 32px;
            color: #7a5c1c;
            letter-spacing: 2px;
        }
        .scroll-table {
            overflow-x: auto;
            background: var(--content-bg-color, #fcfaf5);
            border-radius: 12px;
            box-shadow: 0 2px 8px 0 rgba(80,60,20,0.04);
            margin-bottom: 24px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            min-width: 1200px;
            font-size: 1rem;
        }
        th, td {
            border: 1px solid var(--table-border);
            padding: 8px 10px;
            text-align: left;
        }
        th {
            background: var(--table-header-bg);
            color: #4d3a0b;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background: var(--table-row-bg);
        }
        tr:hover {
            background: #f3e7c7;
        }
        @media (max-width: 700px) {
            .container { padding: 8px 2px; }
            table { font-size: 0.85rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>삼국지 도서 목록</h1>
        <div class="scroll-table">
            <table>
"""

html_tail = """
            </table>
        </div>
        <p style="text-align:center; color:#a08a5c; font-size:0.95rem; margin-top:32px;">※ 표가 너무 길 경우, PC에서 가로 스크롤로 전체 내용을 확인하세요.</p>
    </div>
</body>
</html>
"""

try:
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_head)
        # 헤더
        f.write("                <thead>\n                    <tr>\n")
        for col in rows[0]:
            f.write(f"                        <th>{col}</th>\n")
        f.write("                    </tr>\n                </thead>\n                <tbody>\n")
        # 데이터
        for row in rows[1:]:
            f.write("                    <tr>\n")
            for col in row:
                f.write(f"                        <td>{col}</td>\n")
            f.write("                    </tr>\n")
        f.write("                </tbody>\n")
        f.write(html_tail)
    
    print(f"HTML 변환 완료! {len(rows)}개의 행이 변환되었습니다.")
    print(f"생성된 파일: {html_path}")

except Exception as e:
    print(f"오류 발생: {e}")
    raise

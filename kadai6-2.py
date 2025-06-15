"""
課題6-2: 世の中のオープンデータを調査して、データを取得するプログラム

【選択したオープンデータ】
名前: 気象庁防災情報XMLオープンデータ
概要: 日本気象庁が提供する天気予報、警報・注意報などの防災気象情報
     無料でリアルタイムの公式気象データを利用可能

【エンドポイントと機能】
URL: https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json
機能: 指定した地域コードの天気予報データをJSON形式で取得
パラメータ: area_code（地域コード：130000=東京都、270000=大阪府など）

【使い方】
1. 地域コードを指定してAPIにアクセス
2. 認証不要で直接データ取得
3. JSON形式の天気予報データを表示
"""

import requests
import json

# 気象庁オープンデータのURL（東京都の天気予報）
API_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

# APIリクエスト実行
response = requests.get(API_URL)
data = response.json()

# 結果表示
print("=== 気象庁オープンデータ（東京都天気予報） ===")
print(json.dumps(data, indent=2, ensure_ascii=False))
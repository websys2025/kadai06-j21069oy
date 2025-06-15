"""
課題6-1: e-Stat APIを使って人口推計以外のデータを取得するプログラム

【取得するデータの種類】
- 住民基本台帳人口移動報告データ（転入・転出者数）
- これは人口推計とは異なる住民登録ベースの移動統計データ

【使用するエンドポイント】
- getStatsData: 統計データの実数値を取得するAPI
- URL: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData

【APIの機能】
- 指定した統計表から実際の数値データを取得
- 地域・時間・分類項目での絞り込み検索が可能
- メタデータも同時取得可能

【使い方】
- 確実に存在する統計表IDを使用
- 基本的なパラメータのみ指定してデータ取得
- 取得したJSONデータを確認・表示
"""

import requests
import json

#
APP_ID = "2179a005ad38c63e1858e3dd6b237020fb37751d"
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"


params = {
    "appId": APP_ID,
    "statsDataId": "0003065345",
    "cdArea": "13000,27000",
    "metaGetFlg": "Y",
    "cntGetFlg": "N",
    "lang": "J"
}

print("=== 住民基本台帳人口移動報告データの取得開始 ===")
print(f"使用する統計表ID: {params['statsDataId']}")
print(f"対象地域: 東京都・大阪府")
print()

try:
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        if "GET_STATS_DATA" in data:
            result = data["GET_STATS_DATA"]["RESULT"]
            print(f"APIステータス: {result['STATUS']}")

            if result["STATUS"] == 0:
                print("データ取得成功！")


                if "STATISTICAL_DATA" in data["GET_STATS_DATA"]:
                    table_info = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["TABLE_INF"]
                    print(f"統計表名: {table_info.get('TITLE', {}).get('$', '不明')}")
                    print(f"統計名: {table_info.get('STATISTICS_NAME', '不明')}")

            else:
                print(f"APIエラー: {result.get('ERROR_MSG', '不明なエラー')}")

        # 完全なデータを表示
        print("\n=== 取得した完全なデータ ===")
        print(json.dumps(data, indent=2, ensure_ascii=False))

    else:
        print(f"HTTPエラー: {response.status_code}")

except Exception as e:
    print(f"リクエスト実行エラー: {e}")
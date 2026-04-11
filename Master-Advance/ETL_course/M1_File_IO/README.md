# M1 — File I/O

> 讀寫 CSV、Excel、JSON、XML — 這是資料工程師每天的工作

## 你會學到

- `pd.read_csv()` / `df.to_csv()` — 最常用的格式
- `pd.read_excel()` / `df.to_excel()` — 商業環境的 dominant format
- `pd.read_json()` / `df.to_json()` — API 回傳通常長這樣
- `pd.read_xml()` / `df.to_xml()` — 舊系統、政府資料常見
- 編碼（`encoding='utf-8-sig'`）與分隔符號的坑

## 課程檔案

- **`S1_file_io.ipynb`** — 主講義，四種格式的讀寫示範

## 資料檔

`data/` 資料夾包含四種格式的練習資料：

| 檔案 | 格式 | 來源 |
|:-----|:-----|:-----|
| `垃圾車點位資訊.csv` | CSV | 政府開放資料 |
| `通訊錄.xlsx` | Excel | 合成範例 |
| `taipei.json` | JSON | 台北市 API |
| `jobs.xml` | XML | 求職網站資料 |

## 常踩的坑

1. **CSV 中文亂碼** → 用 `encoding='utf-8-sig'` 或 `encoding='cp950'`
2. **Excel 多個 sheet** → `pd.read_excel(path, sheet_name='工作表1')` 或 `sheet_name=None` 讀全部
3. **JSON 巢狀結構** → 用 `pd.json_normalize()` 攤平
4. **XML 命名空間** → `pd.read_xml()` 的 `namespaces` 參數

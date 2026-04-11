# M2 — SQL + Python

> 資料不只住在 CSV 裡 — 大部分時候，它住在資料庫

## 你會學到

- 用 Python 內建的 `sqlite3` 連線、查詢、寫入
- 用 **`pd.read_sql()`** 把查詢結果直接變成 DataFrame（超好用）
- 用 `df.to_sql()` 把 DataFrame 寫回資料庫
- **參數化查詢**防 SQL injection
- Transaction（commit / rollback）

## 課程檔案

- **`S2_sql_python.ipynb`** — 主講義：從零開始建資料庫、塞資料、查詢、串 Pandas

## SQL 腳本

`sql/` 資料夾的 SQL 檔案會在 notebook 裡被執行：

| 檔案 | 用途 |
|:-----|:-----|
| `01_create_database.sql` | 建立資料庫 |
| `02_create_tables.sql` | 建立三張表（customers、products、orders） |
| `03_insert_data.sql` | 塞入範例資料 |
| `04_restore_data.sql` | 還原到初始狀態（練習出錯可 reset） |

## 為什麼用 SQLite？

- **零安裝** — Python 內建 `sqlite3` 模組，不用裝 MySQL/PostgreSQL
- **單檔存檔** — 整個資料庫就是一個 `.db` 檔，好備份、好移動
- **完整 SQL 語法** — 該有的 JOIN、GROUP BY、子查詢都有
- **業界真的在用** — Android 手機、瀏覽器、airline 系統都在用 SQLite

學會 SQLite，之後換 PostgreSQL/MySQL 只需要換連線字串（`create_engine(...)`）就好。

## 常踩的坑

1. **忘記 `conn.commit()`** → 寫入沒生效
2. **字串拼接 SQL** → SQL injection 漏洞，一律用 `?` 參數化
3. **連線沒關** → 用 `with sqlite3.connect(...)` context manager
4. **日期型別** → SQLite 沒有原生 DATE，存字串，讀回來用 `pd.to_datetime()`

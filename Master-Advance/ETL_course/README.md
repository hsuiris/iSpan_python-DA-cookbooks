# ETL 工程實務

> **課程定位：** Python 資料工程師的必備工具箱
> **前置知識：** Python 基礎、Pandas 基本操作
> **學完後你會：** 寫出可維護、可測試、可監控的 ETL pipeline

---

## 為什麼要上這門課？

資料分析課教你「怎麼分析資料」，但真實世界還有一個隱藏關卡：

> 資料從哪來？怎麼載進來？壞資料怎麼處理？Pipeline 掛了怎麼知道？怎麼換環境不用改程式？

這門課把這些「資料工程底層功夫」一次補齊。每一個模組都是業界每天在用的技能。

---

## 課程地圖

| 模組 | 主題 | 你會學到 | 業界用途 |
|:----:|:-----|:--------|:---------|
| **M1** | [File I/O](M1_File_IO/) | Pandas 讀寫 CSV/Excel/JSON/XML | 每天都在做的檔案交換 |
| **M2** | [SQL + Python](M2_SQL_Python/) | sqlite3、`pd.read_sql()`、參數化查詢 | 從資料庫抽資料回來分析 |
| **M3** | [Logging](M3_Logging/) | `logging` 模組、log level、檔案輪替 | Pipeline 出事時的偵錯線索 |
| **M4** | [Config Management](M4_Config_Management/) | `configparser`、YAML、`.env` | 一份程式、多套環境（dev/prod） |
| **M5** | [Python Utils](M5_Python_Utils/) | `pathlib`、`zip`、type hints | 寫出更 Pythonic 的程式 |
| **M6** | [Integration Capstone](M6_Integration_Capstone/) | 把 M1~M5 串成一個完整 ETL | 面試作品集 / 實戰練習 |

---

## 學習路徑

```
M1 File I/O
    │ (「資料從檔案來」)
    ▼
M2 SQL + Python
    │ (「資料也可能從資料庫來」)
    ▼
M3 Logging          ┐
M4 Config           │ (這三個是工程基礎建設，順序可交換)
M5 Python Utils     ┘
    │
    ▼
M6 Integration Capstone
    (「把前面學的全部用上，做出一個完整 ETL」)
```

**建議進度：** 每週一個模組，M6 留兩週做專案。

---

## 環境準備

```bash
# 1. 進入課程資料夾
cd Master-Advance/ETL_course

# 2. 建議用虛擬環境
python -m venv .venv
source .venv/bin/activate       # Mac/Linux
# .venv\Scripts\activate        # Windows

# 3. 安裝套件
pip install -r requirements.txt

# 4. 啟動 Jupyter
jupyter lab
```

> **Note**：M2 的 SQL 練習使用 Python 內建的 `sqlite3`，**不需要安裝任何資料庫**。

---

## 目錄結構

```
ETL_course/
├── README.md                       ← 你在看的檔案
├── requirements.txt
├── M1_File_IO/
│   ├── README.md
│   ├── S1_file_io.ipynb
│   └── data/                       ← 練習用的原始資料檔
├── M2_SQL_Python/
│   ├── README.md
│   ├── S2_sql_python.ipynb
│   └── sql/                        ← 建表與匯入用的 SQL 腳本
├── M3_Logging/
│   ├── README.md
│   ├── S3_logging.ipynb
│   ├── S3b_logger_advanced.ipynb
│   └── logging.conf
├── M4_Config_Management/
│   ├── README.md
│   ├── S4_config_management.ipynb
│   └── config/
├── M5_Python_Utils/
│   ├── README.md
│   ├── S5_pathlib.ipynb
│   ├── S6_zip_iteration.ipynb
│   └── S7_type_hints.ipynb
└── M6_Integration_Capstone/
    ├── README.md
    └── S8_etl_pipeline.ipynb
```

---

## 如何跟這門課搭配其他課？

| 你已經學過 | 接下來 |
|:-----------|:-------|
| 剛學完 Pandas 基礎 | 從 M1 開始，把 I/O 的坑一次學會 |
| 會 Pandas 但沒碰過 SQL | 跳 M2，最短時間補齊資料庫存取 |
| 要上線一個 ETL 專案 | M3 + M4 是上線前的最低門檻 |
| 要整合成作品集 | 直接做 M6 Capstone |

# M6 — Integration Capstone

> 把 M1~M5 全部用上，做出一個**可以放履歷**的 ETL pipeline

## 專案目標

你要寫一個**電商訂單資料 pipeline**，完成下列步驟：

```
┌──────────────────┐
│ 1. Extract       │  讀 CSV + 讀 SQLite DB        ← 用到 M1 + M2
└────────┬─────────┘
         ▼
┌──────────────────┐
│ 2. Transform     │  清理、合併、計算 KPI         ← 用到 Pandas 基礎
└────────┬─────────┘
         ▼
┌──────────────────┐
│ 3. Load          │  寫回 SQLite + 輸出 Excel 報表 ← 用到 M1 + M2
└────────┬─────────┘
         ▼
┌──────────────────┐
│ 整個過程全程 log  │                              ← 用到 M3
│ 所有參數從 config │                              ← 用到 M4
│ 程式碼有 type hint│                              ← 用到 M5
└──────────────────┘
```

## 課程檔案

- **`S8_etl_pipeline.ipynb`** — Capstone 主講義 + 完整實作示範

## 完成後你會有

- 一份可以 `python pipeline.py --env dev` 跑起來的專案
- 一個**「我會寫 ETL」** 的作品集項目
- 面試時可以自信地說：「我做過一個整合 CSV/SQL/logging/config 的 ETL pipeline」

## 驗收標準

完成的 pipeline 應該滿足：

- [ ] Extract 階段支援 CSV 和 SQL 兩種來源
- [ ] Transform 有至少一個資料清理步驟（去重 / 型別轉換 / 缺值處理）
- [ ] Transform 有至少一個聚合計算（月營收 / 類別統計 / VIP 分群）
- [ ] Load 階段同時寫 DB 和 Excel
- [ ] 每個階段都有 `logger.info()`，錯誤有 `logger.error()`
- [ ] 所有路徑、檔名、DB 連線字串都從 `config.yaml` 讀
- [ ] 所有函式簽名都有 type hints
- [ ] 有一個 `main()` 函式協調整個流程

## 延伸挑戰（加分項）

- 改寫成純 `.py` 檔，用 `argparse` 支援命令列參數
- 加上 pytest 單元測試
- 用 cron / GitHub Actions 排程執行
- 換成 PostgreSQL 或 DuckDB 試試看

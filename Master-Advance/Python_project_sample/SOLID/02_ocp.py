"""
O - Open/Closed Principle 開放封閉原則
========================================
"Software entities should be OPEN for extension, CLOSED for modification."

口訣：「加新功能用加新類，不要改舊類。」

本檔對應 moushih.com/solid 的 Logger 範例：
  反例：Logger 內部用 if _target == "Console" / elif "File" / elif "WebApi"
        每加一種輸出位置就要動原 class、重編譯、重測試
  正解：定義 ILogger 介面，每種輸出寫成獨立 class，要加新的只新增子類

跑：python3 02_ocp.py
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol


# =====================================================================
# ❌ BAD：每加一種 target 都要回來改 if/elif
# =====================================================================
class LoggerBad:
    """
    違反 OCP 的訊號：
      - 加 target 要動 __init__ 加一個分支
      - 加 target 要動 log 加一個分支
      - 既有的測試全部都要重跑（你動了它）
    """

    def __init__(self, target: str) -> None:
        self._target = target

    def log(self, msg: str) -> None:
        if self._target == "Console":
            print(f"  [BAD][Console] {msg}")
        elif self._target == "File":
            print(f"  [BAD][File] (假裝) 寫到 app.log: {msg}")
        # 老闆：加個寫到 Web API 的好嗎？→ 你又要改這支檔案
        else:
            raise ValueError(f"unknown target: {self._target}")


# =====================================================================
# ✅ GOOD：定義抽象，新增輸出 = 新增子類，不動既有程式碼
# =====================================================================
class ILogger(Protocol):
    def log(self, msg: str) -> None: ...


class ConsoleLogger:
    def log(self, msg: str) -> None:
        print(f"  [Console] {msg}")


class FileLogger:
    def __init__(self, path: str) -> None: self.path = path
    def log(self, msg: str) -> None:
        print(f"  [File] (假裝) 寫到 {self.path}: {msg}")


# 老闆：加 Web API → 不用動 ConsoleLogger / FileLogger，新增一個就好
class WebApiLogger:
    def __init__(self, url: str) -> None: self.url = url
    def log(self, msg: str) -> None:
        print(f"  [Web] (假裝) POST {self.url} body={msg!r}")


# 想要同時打多個目的地？再開一個 composite logger，依然零修改既有 class
class FanOutLogger:
    def __init__(self, *loggers: ILogger) -> None:
        self._loggers = loggers

    def log(self, msg: str) -> None:
        for lg in self._loggers:
            lg.log(msg)


# =====================================================================
# 客戶端：只認 ILogger 介面
# =====================================================================
class App:
    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

    def do_work(self) -> None:
        self.logger.log("App started")
        self.logger.log("doing work…")


def main() -> None:
    print("--- BAD：if/elif 每加一個 target 就要動原 class ---")
    LoggerBad("Console").log("hello")
    LoggerBad("File").log("hello")

    print("\n--- GOOD：開新類即可 ---")
    App(ConsoleLogger()).do_work()
    print()
    App(FileLogger("/tmp/app.log")).do_work()
    print()
    App(WebApiLogger("https://api.log/ingest")).do_work()

    print("\n--- 進階：不改任何既有 class，組合出『同時打 3 個』---")
    multi = FanOutLogger(
        ConsoleLogger(),
        FileLogger("/tmp/multi.log"),
        WebApiLogger("https://api.log/ingest"),
    )
    App(multi).do_work()

    print("""
要點：
  - 既有 class（ConsoleLogger / FileLogger / App）一行都沒動
  - 新功能 = 新類別。原始碼版控 diff 只新增、無修改 → 風險小
  - 測試：舊功能不需重測，新功能只需測新類
""")


if __name__ == "__main__":
    main()

"""
S - Single Responsibility Principle 單一責任原則
================================================
"A class should have only ONE reason to change."

口訣：「責任 = 改變的理由」。
      一個類別如果有 N 個理由可能讓你修改它，它就違反 SRP。

本檔對應 moushih.com/solid 的 OrderManager 範例：
  反例：OrderManager 同時管「訂單資料」+「DB 連線」+「資料過濾」+「格式轉換」
  正解：拆成 OrderRepository（負責 DB）與 Logger（負責記錄）

跑：python3 01_srp.py
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


# =====================================================================
# ❌ BAD：一個類別塞了 4 種責任，每個責任都可能變動
# =====================================================================
class OrderManagerBad:
    """
    四個改變理由：
      1. DB 廠商換 (Postgres → MySQL) → 動 _conn_string、_save_to_db
      2. 過濾規則改 → 動 filter_orders
      3. log 輸出格式改 → 動 log
      4. 商業邏輯改 → 動 add_order
    任何一個一動，整支檔案的測試都要重跑。高耦合、低內聚。
    """

    def __init__(self) -> None:
        self._conn_string = "postgres://localhost/db"   # 責任 1：DB 設定
        self._orders: list[dict[str, Any]] = []         # 責任 4：訂單資料

    def add_order(self, order: dict[str, Any]) -> None:
        self._orders.append(order)
        self._save_to_db(order)
        self.log(f"new order {order}")

    def _save_to_db(self, order: dict[str, Any]) -> None:    # 責任 1
        print(f"  [BAD] (假裝) 用 {self._conn_string} 存 {order}")

    def filter_orders(self, min_amount: int) -> list[dict[str, Any]]:  # 責任 2
        return [o for o in self._orders if o["amount"] >= min_amount]

    def log(self, msg: str) -> None:                              # 責任 3
        print(f"  [BAD][LOG] {msg}")


# =====================================================================
# ✅ GOOD：一個類別只一個責任。要換什麼就只動那一個檔案。
# =====================================================================
@dataclass
class Order:
    id: int
    customer: str
    amount: int


class OrderRepository:
    """責任：訂單持久化（換 DB 只改這裡）。"""

    def __init__(self, conn_string: str) -> None:
        self._conn_string = conn_string

    def save(self, order: Order) -> None:
        print(f"  [Repo] (假裝) 用 {self._conn_string} 存 {order}")


class OrderFilter:
    """責任：訂單過濾規則（業務規則改只動這裡）。"""

    @staticmethod
    def by_min_amount(orders: list[Order], min_amount: int) -> list[Order]:
        return [o for o in orders if o.amount >= min_amount]


class Logger:
    """責任：log 輸出（換成寫檔 / 送到 ELK 只改這裡）。"""

    def log(self, msg: str) -> None:
        print(f"  [LOG] {msg}")


class OrderService:
    """責任：協調流程（業務動作）。把上面三個元件組起來用。"""

    def __init__(self, repo: OrderRepository, logger: Logger) -> None:
        self._repo = repo
        self._logger = logger
        self._orders: list[Order] = []

    def add(self, order: Order) -> None:
        self._orders.append(order)
        self._repo.save(order)
        self._logger.log(f"new order #{order.id} from {order.customer}")

    def all(self) -> list[Order]:
        return list(self._orders)


def main() -> None:
    print("--- BAD：一個類別 4 個責任 ---")
    bad = OrderManagerBad()
    bad.add_order({"id": 1, "customer": "Alice", "amount": 500})
    bad.add_order({"id": 2, "customer": "Bob", "amount": 100})
    print(f"  >=200: {bad.filter_orders(200)}")

    print("\n--- GOOD：拆成 Repo / Filter / Logger / Service ---")
    service = OrderService(
        repo=OrderRepository("postgres://localhost/db"),
        logger=Logger(),
    )
    service.add(Order(1, "Alice", 500))
    service.add(Order(2, "Bob", 100))
    print(f"  >=200: {OrderFilter.by_min_amount(service.all(), 200)}")

    print("""
要點：
  - 每個類別只有一個改變理由
  - 換 DB / 換 log 後端 / 改過濾規則 → 各自只動一支檔案
  - 測試也好寫：可以單獨 mock Logger 不影響 Repo
""")


if __name__ == "__main__":
    main()

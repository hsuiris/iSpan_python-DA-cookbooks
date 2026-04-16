"""
I - Interface Segregation Principle 介面隔離原則
================================================
"Clients should not be forced to depend on methods they do not use."

口訣：「多個小介面好過一個肥介面。」
      ISP 是 SRP 在介面層次的延伸：類別有單一責任，介面也該有單一用途。

本檔對應 moushih.com/solid 的 IAllInOneCar 範例：
  反例：一個 IAllInOneCar 把 StartEngine / Drive / StopEngine / ChangeEngine
        全塞進去。Driver 被迫實作 ChangeEngine，只好拋 NotImplementedError。
  正解：拆成 IDriver（駕駛操作）+ IMechanic（維修操作）。
        Driver 只實作前者，Mechanic 只實作後者。

跑：python3 04_isp.py
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol


# =====================================================================
# ❌ BAD：一個肥介面，硬塞所有相關操作
# =====================================================================
class IAllInOneCar(ABC):
    @abstractmethod
    def start_engine(self) -> None: ...
    @abstractmethod
    def drive(self) -> None: ...
    @abstractmethod
    def stop_engine(self) -> None: ...
    @abstractmethod
    def change_engine(self) -> None: ...   # ← 駕駛根本用不到


class DriverBad(IAllInOneCar):
    def start_engine(self) -> None: print("  [BAD][Driver] 發動")
    def drive(self) -> None: print("  [BAD][Driver] 開車")
    def stop_engine(self) -> None: print("  [BAD][Driver] 熄火")

    def change_engine(self) -> None:
        # 被介面逼出來的「假動作」。LSP 警報、ISP 警報同時亮
        raise NotImplementedError("駕駛不會換引擎")


# =====================================================================
# ✅ GOOD：按角色拆介面，每個角色只面對自己用得到的方法
# =====================================================================
class IDriver(Protocol):
    def start_engine(self) -> None: ...
    def drive(self) -> None: ...
    def stop_engine(self) -> None: ...


class IMechanic(Protocol):
    def change_engine(self) -> None: ...
    def change_oil(self) -> None: ...


class Driver:
    """只實作駕駛該做的事。介面乾淨、不需拋例外。"""

    def start_engine(self) -> None: print("  [Driver] 發動")
    def drive(self) -> None: print("  [Driver] 開車")
    def stop_engine(self) -> None: print("  [Driver] 熄火")


class Mechanic:
    """只實作維修該做的事。"""

    def change_engine(self) -> None: print("  [Mechanic] 換引擎")
    def change_oil(self) -> None: print("  [Mechanic] 換機油")


# 一個人同時是駕駛又是技師？沒問題，同時實作兩個介面
class DriverMechanic:
    def start_engine(self) -> None: print("  [Both] 發動")
    def drive(self) -> None: print("  [Both] 開車")
    def stop_engine(self) -> None: print("  [Both] 熄火")
    def change_engine(self) -> None: print("  [Both] 換引擎")
    def change_oil(self) -> None: print("  [Both] 換機油")


# =====================================================================
# 客戶端：吃哪個介面就只認哪個
# =====================================================================
def daily_commute(d: IDriver) -> None:
    d.start_engine(); d.drive(); d.stop_engine()


def maintenance(m: IMechanic) -> None:
    m.change_oil(); m.change_engine()


def main() -> None:
    print("--- BAD：肥介面逼出 NotImplementedError ---")
    bad = DriverBad()
    bad.start_engine(); bad.drive(); bad.stop_engine()
    try:
        bad.change_engine()
    except NotImplementedError as e:
        print(f"  炸了 → {e}")

    print("\n--- GOOD：拆成兩個小介面 ---")
    print("  daily_commute(Driver):")
    daily_commute(Driver())

    print("  maintenance(Mechanic):")
    maintenance(Mechanic())

    print("  同一個人同時實作兩個介面也行：")
    both = DriverMechanic()
    daily_commute(both)
    maintenance(both)

    print("""
要點：
  - 看到 NotImplementedError、空實作、unused 參數 → 通常是 ISP 警報
  - 介面該以「客戶端的使用情境」分組，不是「實作方便」分組
  - 拆成 N 個小介面後：要實作 N 個其實一樣輕鬆，但客戶端依賴變乾淨了
""")


if __name__ == "__main__":
    main()

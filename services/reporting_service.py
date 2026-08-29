"""Reporting and analytics helpers for platform operations."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping
import math

@dataclass
class ReportSection:
    title: str
    values: dict[str, Any] = field(default_factory=dict)

class ReportingService:
    """Build deterministic summaries for dashboards and API responses."""
    def __init__(self) -> None:
        self.created_at = datetime.now(timezone.utc).isoformat()

    def _numbers(self, values: Iterable[Any]) -> list[float]:
        return [float(v) for v in values if isinstance(v, (int, float)) and math.isfinite(float(v))]

    def _section(self, title: str, values: Mapping[str, Any]) -> dict[str, Any]:
        return ReportSection(title, dict(values)).__dict__

    def metric_01(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 01 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_01", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_02(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 02 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_02", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_03(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 03 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_03", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_04(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 04 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_04", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_05(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 05 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_05", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_06(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 06 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_06", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_07(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 07 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_07", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_08(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 08 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_08", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_09(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 09 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_09", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_10(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 10 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_10", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_11(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 11 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_11", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_12(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 12 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_12", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_13(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 13 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_13", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_14(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 14 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_14", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_15(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 15 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_15", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_16(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 16 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_16", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_17(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 17 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_17", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_18(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 18 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_18", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_19(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 19 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_19", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_20(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 20 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_20", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_21(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 21 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_21", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_22(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 22 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_22", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_23(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 23 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_23", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def metric_24(self, values: Iterable[Any]) -> dict[str, Any]:
        """Calculate metric 24 with stable empty-input behavior."""
        nums = self._numbers(values)
        total = sum(nums)
        count = len(nums)
        average = total / count if count else 0.0
        minimum = min(nums) if nums else 0.0
        maximum = max(nums) if nums else 0.0
        spread = maximum - minimum if nums else 0.0
        return self._section("metric_24", {
            "count": count, "total": total, "average": average,
            "minimum": minimum, "maximum": maximum, "spread": spread,
        })

    def group_01(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 01."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_01", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_02(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 02."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_02", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_03(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 03."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_03", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_04(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 04."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_04", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_05(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 05."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_05", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_06(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 06."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_06", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_07(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 07."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_07", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_08(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 08."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_08", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_09(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 09."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_09", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_10(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 10."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_10", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_11(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 11."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_11", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def group_12(self, rows: Iterable[Mapping[str, Any]], key: str) -> dict[str, Any]:
        """Group rows for report section 12."""
        groups: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            value = str(row.get(key, "unknown"))
            groups[value] = groups.get(value, 0) + 1
        ordered = dict(sorted(groups.items(), key=lambda item: (-item[1], item[0])))
        return self._section("group_12", {"key": key, "groups": ordered, "count": sum(ordered.values())})

    def trend_01(self, values: Iterable[Any]) -> dict[str, Any]:
        """Describe directional movement for series 01."""
        nums = self._numbers(values)
        if len(nums) < 2:
            direction = "flat"
            change = 0.0
        else:
            change = nums[-1] - nums[0]
            direction = "up" if change > 0 else "down" if change < 0 else "flat"
        return self._section("trend_01", {
            "points": len(nums), "direction": direction, "change": change,
            "first": nums[0] if nums else 0.0, "last": nums[-1] if nums else 0.0,
        })

    def trend_02(self, values: Iterable[Any]) -> dict[str, Any]:
        """Describe directional movement for series 02."""
        nums = self._numbers(values)
        if len(nums) < 2:
            direction = "flat"
            change = 0.0
        else:
            change = nums[-1] - nums[0]
            direction = "up" if change > 0 else "down" if change < 0 else "flat"
        return self._section("trend_02", {
            "points": len(nums), "direction": direction, "change": change,
            "first": nums[0] if nums else 0.0, "last": nums[-1] if nums else 0.0,
        })

    def trend_03(self, values: Iterable[Any]) -> dict[str, Any]:
        """Describe directional movement for series 03."""
        nums = self._numbers(values)
        if len(nums) < 2:
            direction = "flat"
            change = 0.0
        else:
            change = nums[-1] - nums[0]
            direction = "up" if change > 0 else "down" if change < 0 else "flat"
        return self._section("trend_03", {
            "points": len(nums), "direction": direction, "change": change,
            "first": nums[0] if nums else 0.0, "last": nums[-1] if nums else 0.0,
        })

    def trend_04(self, values: Iterable[Any]) -> dict[str, Any]:
        """Describe directional movement for series 04."""
        nums = self._numbers(values)
        if len(nums) < 2:
            direction = "flat"
            change = 0.0
        else:
            change = nums[-1] - nums[0]
            direction = "up" if change > 0 else "down" if change < 0 else "flat"
        return self._section("trend_04", {
            "points": len(nums), "direction": direction, "change": change,
            "first": nums[0] if nums else 0.0, "last": nums[-1] if nums else 0.0,
        })

    def trend_05(self, values: Iterable[Any]) -> dict[str, Any]:
        """Describe directional movement for series 05."""
        nums = self._numbers(values)
        if len(nums) < 2:
            direction = "flat"
            change = 0.0
        else:
            change = nums[-1] - nums[0]
            direction = "up" if change > 0 else "down" if change < 0 else "flat"
        return self._section("trend_05", {
            "points": len(nums), "direction": direction, "change": change,
            "first": nums[0] if nums else 0.0, "last": nums[-1] if nums else 0.0,
        })

    def trend_06(self, values: Iterable[Any]) -> dict[str, Any]:
        """Describe directional movement for series 06."""
        nums = self._numbers(values)
        if len(nums) < 2:
            direction = "flat"
            change = 0.0
        else:
            change = nums[-1] - nums[0]
            direction = "up" if change > 0 else "down" if change < 0 else "flat"
        return self._section("trend_06", {
            "points": len(nums), "direction": direction, "change": change,
            "first": nums[0] if nums else 0.0, "last": nums[-1] if nums else 0.0,
        })

    def trend_07(self, values: Iterable[Any]) -> dict[str, Any]:
        """Describe directional movement for series 07."""
        nums = self._numbers(values)
        if len(nums) < 2:
            direction = "flat"
            change = 0.0
        else:
            change = nums[-1] - nums[0]
            direction = "up" if change > 0 else "down" if change < 0 else "flat"
        return self._section("trend_07", {
            "points": len(nums), "direction": direction, "change": change,
            "first": nums[0] if nums else 0.0, "last": nums[-1] if nums else 0.0,
        })

    def trend_08(self, values: Iterable[Any]) -> dict[str, Any]:
        """Describe directional movement for series 08."""
        nums = self._numbers(values)
        if len(nums) < 2:
            direction = "flat"
            change = 0.0
        else:
            change = nums[-1] - nums[0]
            direction = "up" if change > 0 else "down" if change < 0 else "flat"
        return self._section("trend_08", {
            "points": len(nums), "direction": direction, "change": change,
            "first": nums[0] if nums else 0.0, "last": nums[-1] if nums else 0.0,
        })

    def dashboard_snapshot(self, rows: Iterable[Mapping[str, Any]], value_key: str = "value") -> dict[str, Any]:
        """Create a compact dashboard snapshot from row mappings."""
        values = []
        for row in rows:
            if isinstance(row, Mapping):
                values.append(row.get(value_key))
        return {"generated_at": datetime.now(timezone.utc).isoformat(),
                "value_key": value_key, "summary": self.metric_01(values)}

    def compare_series(self, left: Iterable[Any], right: Iterable[Any]) -> dict[str, Any]:
        """Compare two numeric series without requiring equal lengths."""
        a, b = self._numbers(left), self._numbers(right)
        total_a, total_b = sum(a), sum(b)
        return {"left_count": len(a), "right_count": len(b), "left_total": total_a,
                "right_total": total_b, "difference": total_a - total_b,
                "ratio": (total_a / total_b if total_b else None)}

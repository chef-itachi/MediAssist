"""Summarize real medication-reminder check-ins without storing medication details."""
import argparse
import csv
from collections import Counter
from datetime import date, datetime
from pathlib import Path

FIELDS = ("date", "time", "context", "result", "delay_minutes")
RESULTS = {"taken", "late", "missed"}


def load_checkins(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None or any(field not in reader.fieldnames for field in FIELDS):
            raise ValueError(f"CSV must include these columns: {', '.join(FIELDS)}")

        rows = []
        errors = []
        for line, row in enumerate(reader, start=2):
            try:
                date.fromisoformat((row.get("date") or "").strip())
                datetime.strptime((row.get("time") or "").strip(), "%H:%M")
                context = (row.get("context") or "").strip()
                if not context:
                    raise ValueError("context is required")
                result = (row.get("result") or "").strip().lower()
                if result not in RESULTS:
                    raise ValueError("result must be taken, late, or missed")
                delay = (row.get("delay_minutes") or "").strip()
                if delay:
                    minutes = int(delay)
                    if minutes < 0:
                        raise ValueError("delay_minutes cannot be negative")
                elif result == "late":
                    raise ValueError("late check-ins require delay_minutes")
                else:
                    minutes = 0
                if result == "late" and minutes == 0:
                    raise ValueError("late check-ins require a positive delay")
                if result != "late" and minutes:
                    raise ValueError("delay_minutes is only used for late check-ins")
                rows.append({
                    "date": row["date"].strip(),
                    "time": row["time"].strip(),
                    "context": context,
                    "result": result,
                    "delay_minutes": str(minutes),
                })
            except (TypeError, ValueError) as exc:
                errors.append(f"row {line}: {exc}")

    if errors:
        raise ValueError("Invalid CSV data:\n" + "\n".join(errors))
    if not rows:
        raise ValueError("CSV has a header but no check-ins yet; add real observations first.")
    return rows


def summarize(rows: list[dict[str, str]]) -> dict:
    outcomes = Counter(row["result"] for row in rows)
    missed_by_context = Counter(row["context"] for row in rows if row["result"] == "missed")
    late_rows = [row for row in rows if row["result"] == "late"]
    most_missed = None
    if missed_by_context:
        highest = max(missed_by_context.values())
        most_missed = sorted(context for context, count in missed_by_context.items() if count == highest)
    return {
        "total": len(rows),
        "taken": outcomes["taken"],
        "late": outcomes["late"],
        "missed": outcomes["missed"],
        "most_missed_contexts": most_missed or [],
        "average_late_minutes": round(
            sum(int(row["delay_minutes"]) for row in late_rows) / len(late_rows), 1
        ) if late_rows else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize real medication-reminder check-ins.")
    parser.add_argument(
        "--csv",
        type=Path,
        default=Path(__file__).with_name("data.csv"),
        help="Path to a private CSV of check-ins (default: prototype/data.csv)",
    )
    args = parser.parse_args()
    if not args.csv.is_file():
        parser.exit(
            1,
            f"CSV not found: {args.csv}\n"
            "Copy data.example.csv to data.csv, then add real, consented check-ins.\n",
        )
    try:
        report = summarize(load_checkins(args.csv))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")

    print(f"Check-ins: {report['total']}")
    print(f"Taken on time: {report['taken']}")
    print(f"Taken late: {report['late']}")
    print(f"Missed: {report['missed']}")
    if report["most_missed_contexts"]:
        print("Most missed context: " + ", ".join(report["most_missed_contexts"]))
    else:
        print("Most missed context: none recorded")
    if report["average_late_minutes"] is not None:
        print(f"Average delay when late: {report['average_late_minutes']} minutes")
    print("Use this summary only to discuss non-medical reminder cues; follow the prescribed schedule.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

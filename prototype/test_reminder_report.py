import tempfile
import unittest
from pathlib import Path

from reminder_report import load_checkins, summarize


class ReminderReportTests(unittest.TestCase):
    def test_summarizes_outcomes_and_missed_context(self):
        rows = [
            {"date": "2026-11-11", "time": "08:00", "context": "before breakfast", "result": "taken", "delay_minutes": "0"},
            {"date": "2026-11-11", "time": "13:00", "context": "household work", "result": "missed", "delay_minutes": "0"},
            {"date": "2026-11-12", "time": "13:00", "context": "household work", "result": "late", "delay_minutes": "15"},
        ]

        report = summarize(rows)

        self.assertEqual(report["total"], 3)
        self.assertEqual(report["taken"], 1)
        self.assertEqual(report["late"], 1)
        self.assertEqual(report["missed"], 1)
        self.assertEqual(report["most_missed_contexts"], ["household work"])
        self.assertEqual(report["average_late_minutes"], 15)

    def test_rejects_bad_rows_instead_of_skipping_them(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkins.csv"
            path.write_text(
                "date,time,context,result,delay_minutes\n"
                "not-a-date,25:00,,unknown,\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "row 2"):
                load_checkins(path)

    def test_reports_empty_dataset(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkins.csv"
            path.write_text("date,time,context,result,delay_minutes\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "no check-ins"):
                load_checkins(path)


if __name__ == "__main__":
    unittest.main()

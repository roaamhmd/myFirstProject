import os
import sys
from datetime import datetime


class SystemTester:

    def __init__(self, project_name="githubProject"):
        self.project_name = project_name
        self.timestamp = datetime.now()

    def get_system_info(self):
        return {
            "Python Version": sys.version.split()[0],
            "Execution Path": sys.executable,
            "Working Directory": os.getcwd(),
            "Script File": os.path.basename(__file__),
        }

    def run_diagnostics(self):
        print("=" * 55)
        print(f"🚀 FULL ENVIRONMENT DIAGNOSTIC: {self.project_name}")
        print("=" * 55)

        # 1. System & Path Checks
        print("\n📌 SYSTEM DETAILS:")
        for key, val in self.get_system_info().items():
            print(f"  • {key:<18}: {val}")

        # 2. Logic & Data Processing Test
        print("\n⚡ DATA PROCESSING TEST:")
        dataset = [12, 45, 67, 23, 89, 34]
        transformed = [x * 2 for x in dataset if x > 30]

        print(f"  • Original Data     : {dataset}")
        print(f"  • Filtered (>30) *2 : {transformed}")
        print(
            f"  • Stats             : Max = {max(dataset)} | Min = {min(dataset)} | Total = {sum(dataset)}"
        )

        # 3. Execution Confirmation
        print("\n" + "-" * 55)
        formatted_time = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"✅ STATUS: Python is fully functional on VS Code! ({formatted_time})"
        )
        print("=" * 55 + "\n")


if __name__ == "__main__":
    tester = SystemTester()
    tester.run_diagnostics()
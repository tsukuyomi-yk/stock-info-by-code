import subprocess
import os

SOURCE_FILE = "fetch/fetch_stockdata.py"
ERROR_LOG = "logs/error.log"
FIXED_FILE = "fetch/fetch_stockdata_fixed.py"

def call_gemini(error_log, original_code):
    prompt = f"""
以下のPythonコードにはバグがあります。

【元のコード】
{original_code}

【pytestのエラーログ】
{error_log}

このバグを修正したコードだけを返してください（コメント不要）。
"""
    result = subprocess.run(
        ["gemini", "chat", "--input", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout

if __name__ == "__main__":
    if not os.path.exists(ERROR_LOG):
        print("Error log not found.")
        exit(1)

    with open(ERROR_LOG, encoding="utf-8") as f:
        error_log = f.read()

    with open(SOURCE_FILE, encoding="utf-8") as f:
        original_code = f.read()

    fixed_code = call_gemini(error_log, original_code)

    with open(FIXED_FILE, "w", encoding="utf-8") as f:
        f.write(fixed_code.strip())

    print(f"修正済みコードを {FIXED_FILE} に出力しました。")

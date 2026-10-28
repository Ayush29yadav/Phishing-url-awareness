# EWB Phishing URL Awareness Checker

## Overview
Phishing is a trick that uses fake links or messages to persuade people to share passwords, payment details, or other private information. This beginner Python project reads URL text and highlights a few visible warning signs so a person can review a link more carefully.

**Important:** The checker never visits URLs, sends requests, or scans websites. It is an educational awareness aid, not a malware detector or a definitive safety verdict.

## Features
- Flags an `@` symbol in the URL.
- Flags URLs longer than 100 characters.
- Flags IPv4-looking numeric hostnames.
- Flags hostnames with five or more dot-separated labels.
- Flags hostname text containing `xn--` (punycode marker).
- Flags the `http` scheme.
- Explains why each warning matters.
- Handles empty input and malformed URL formats.
- Repeats checks until the user enters `q`, `quit`, or `exit`.

## Requirements
- Python 3.10 or later.
- No extra packages are required.

## How to Run
1. Open this folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Run:

   ```powershell
   python phishing_checker.py
   ```

   If `python` is not recognised on Windows, try `py phishing_checker.py`. On macOS/Linux, use `python3 phishing_checker.py`.

4. Enter one of the sample strings from `tests/test_samples.md`.
5. Type `q` to quit.

## Example Output
Your output will vary based on the sample you enter. For `http://192.0.2.10/account`, expect warnings about an IP-address hostname and HTTP, plus explanatory hints and a review summary.

## Testing
The five required workbook samples and their expected results are listed in [`tests/test_samples.md`](tests/test_samples.md). Fill in the actual result and PASS/FAIL columns only after running each sample.

## Screenshots
After running the program, save clear, genuine screenshots of your own terminal output as:
- `screenshots/sample_run.png`
- `screenshots/test_results.png`

Do not use mock screenshots as evidence. See the EWB workbook screenshot instructions and ensure no private information is visible.

## Improvements
1. **Repeat/quit loop:** You can inspect multiple sample strings in one run and enter `q` to exit. This avoids restarting the program after each sample.
2. **Warning explanations:** Each warning includes a plain-language reason, helping a beginner understand why it matters.
3. **Malformed input handling:** Invalid URL formats are caught and reported instead of crashing the program.

## Limitations
- It checks only six visible URL clues; the explanatory text does not make the verdict definitive.
- No warning signs found does **not** mean a URL is safe.
- Long URLs, IP addresses, HTTP, many hostname labels, and punycode can occur for legitimate reasons.
- The checker does not validate website reputation, page content, certificates, redirects, or malware.
- It does not make network requests or open URLs.

## Ethical Use
Use the workbook's sample strings for testing. Do not open suspicious links to test them, collect credentials, send phishing messages, or test websites without written permission. Never commit passwords, API keys, or private data to GitHub.

## Author
[Write your name, batch/course, and EWB Courses details here.]

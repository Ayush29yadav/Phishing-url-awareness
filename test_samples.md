# Test Samples — Phishing URL Awareness Checker

Use only the sample strings from the EWB workbook. The program checks URL text only; it does not open links.

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs; reminder that this does not prove safety | Fill in after running | Fill in |
| 2 | `http://192.0.2.10/account` | IP-address hostname and HTTP warnings | Fill in after running | Fill in |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol and HTTP warnings | Fill in after running | Fill in |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments/subdomains warning | Fill in after running | Fill in |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname warning | Fill in after running | Fill in |

## How to complete this record

1. Run each sample in `phishing_checker.py`.
2. Write the actual warnings printed by your program.
3. Mark PASS only if the actual result matches the expected result.
4. If a result differs, investigate and retest before submitting.

Do not claim tests passed until you have run them yourself.

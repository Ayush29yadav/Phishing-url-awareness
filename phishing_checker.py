"""
EWB Phishing URL Awareness Checker
Educational URL-text checks only. This program never visits a URL.
"""

import re
from urllib.parse import urlparse


WARNING_HINTS = {
    "Contains an @ symbol; inspect carefully.": (
        "Browsers treat the text before @ as user information, so the real "
        "hostname may be different from the name you noticed."
    ),
    "Unusually long URL (over 100 characters).": (
        "Long URLs can make the destination harder to notice, although many "
        "legitimate URLs are long too."
    ),
    "Uses an IP address instead of a familiar domain.": (
        "A numeric hostname can hide the identity of the service. IP addresses "
        "can also be legitimate in some settings."
    ),
    "Contains many hostname segments/subdomains.": (
        "Many dot-separated hostname labels can make a destination confusing; "
        "this alone does not prove malicious intent."
    ),
    "Contains a punycode-style hostname.": (
        "The xn-- marker can represent international characters, including "
        "look-alike characters."
    ),
    "Uses HTTP. HTTPS alone does not prove trust.": (
        "HTTP does not encrypt the connection. HTTPS is encrypted, but it does "
        "not prove that a website is honest."
    ),
}


def inspect_url(url):
    """Return warning messages for URL text without making any network request."""
    url = url.strip()
    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    findings = []

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    return findings


def main():
    """Read sample URL text repeatedly until the user chooses to quit."""
    print("=" * 43)
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")
    print("Use workbook sample strings only. Type q to quit.")
    print("=" * 43)

    while True:
        raw_url = input("\nEnter a sample URL to inspect (or q to quit): ").strip()

        if raw_url.lower() in {"q", "quit", "exit"}:
            print("Goodbye. Stay careful with unexpected links!")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")

        if findings and findings[0] == "No URL entered.":
            print("- No URL entered. Please try again.")
            continue

        for item in findings:
            print("- " + item)
            if item in WARNING_HINTS:
                print("  Why it matters: " + WARNING_HINTS[item])

        warning_count = sum(item in WARNING_HINTS for item in findings)
        if warning_count:
            print(f"\nREVIEW CAREFULLY: {warning_count} warning sign(s) found.")
        elif findings and findings[0] == "This text is not a valid URL format.":
            print("\nPlease check the URL text format and try again.")
        elif findings and findings[0] == "Could not identify a hostname.":
            print("\nPlease enter text that includes a hostname.")
        else:
            print("\nNo listed warning signs found. This does NOT prove safety.")

        print("Reminder: this is an awareness aid, not a definitive safety verdict.")


if __name__ == "__main__":
    main()

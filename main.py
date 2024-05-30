import argparse
import requests
import tldextract
import re
import fnmatch

# Fetch the HTML content from a URL or file
def fetch_html_content(source):
    if source.startswith("http://") or source.startswith("https://"):
        response = requests.get(source)
        return response.text
    else:
        with open(source, "r") as file:
            return file.read()

def is_valid_domain(domain, allowed_domains):
    extracted = tldextract.extract(domain)
    
    if allowed_domains == ["*"]:
        return bool(extracted.domain) and bool(extracted.suffix)
    else:
        if (extracted.subdomain):
            full_domain = f'{extracted.subdomain}.{extracted.domain}.{extracted.suffix}'
        else:
            full_domain = f'{extracted.domain}.{extracted.suffix}'

        for allowed_domain in allowed_domains:
            if fnmatch.fnmatch(full_domain, allowed_domain):
                return True
        return False

def extract_domains_from_html(html_content, allowed_domains):
    domains = set()

    domains_regex = r"((?:https?://)?(?:www\.)?[\w.-]+(?:\.[a-zA-Z]{2,})+[^\"\']*)"

    # Extract text from specified tags
    matches = re.findall(domains_regex, html_content)
    for match in matches:
        domains.add(match)

    # Filter out valid domains
    valid_domains = set()
    for domain in domains:
        if is_valid_domain(domain, allowed_domains):
            if domain.startswith('.'):
                domain = domain.lstrip('.')

            valid_domains.add(domain)

    return valid_domains

def get_root_domain(domain):
    extracted = tldextract.extract(domain)
    return f"{extracted.domain}.{extracted.suffix}"

def get_subdomain(domain):
    extracted = tldextract.extract(domain)

    if (extracted.subdomain):
        return f"{extracted.subdomain}.{extracted.domain}.{extracted.suffix}"
    else:
        return f"{extracted.domain}.{extracted.suffix}"

def main(args):
    html_content = fetch_html_content(args.source)
    domains = extract_domains_from_html(html_content, args.domains)

    if args.summary:
        summary = {}
        for domain in domains:
            if (args.subdomains):
                root_domain = get_subdomain(domain)
            else:
                root_domain = get_root_domain(domain)
            summary[root_domain] = summary.get(root_domain, 0) + 1
        print("Summary separated by root domain:")
        print("-" * 100)

        sorted_summary = sorted(summary.items(), key=lambda x: x[1], reverse=True)

        for root_domain, count in sorted_summary:
            print(f"{count: 4d} occurrences: {root_domain}")
    else:
        print("Domains extracted:")
        print("-" * 100)

        for domain in domains:
            print(domain)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract all links from an HTML file")

    parser.add_argument("source", type=str, help="URL or file path of the HTML content to extract domains from")
    parser.add_argument("--domains", nargs="+", default=["*"], help="A list of domains with wildcards like *.google.com")
    parser.add_argument("--summary", action="store_true", help="Return a summary separated by root domain")
    parser.add_argument("--subdomains", action="store_true", help="Have a list of subdomains in the summary")

    args = parser.parse_args()
    main(args)

import dns.resolver

def dns_lookup(domain, record_type='A'):
    try:
        answers = dns.resolver.query(domain, record_type)
        return answers
    except dns.resolver.NXDOMAIN:
        print(f"Error: No such domain '{domain}'")
    except dns.resolver.NoAnswer:
        print(f"Error: No answer for '{domain}'")
    except Exception as e:
        print(f"Error: {str(e)}")

domain = 'example.com'
record_type = 'A'  # You can change this to other record types like 'MX', 'TXT', etc.

results = dns_lookup(domain, record_type)
if results:
    print(f"Results for {domain} ({record_type}):")
    for rdata in results:
        print(f"{rdata.to_text()}")
else:
    print(f"No results for {domain} ({record_type})")

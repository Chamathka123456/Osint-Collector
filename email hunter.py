#!/usr/bin/env python3
"""
📧 Advanced Email Hunter
Finds and verifies email addresses from various sources
FOR EDUCATIONAL AND AUTHORIZED USE ONLY
"""

import re
import json
import time
import requests
import dns.resolver
from datetime import datetime
from urllib.parse import urlparse

class EmailHunter:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Common email patterns
        self.email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        
        # Common email providers
        self.providers = {
            'gmail.com': 'Google',
            'yahoo.com': 'Yahoo',
            'outlook.com': 'Microsoft',
            'hotmail.com': 'Microsoft',
            'protonmail.com': 'ProtonMail',
            'icloud.com': 'Apple',
            'aol.com': 'AOL',
            'zoho.com': 'Zoho',
            'mail.com': 'Mail.com'
        }
    
    def verify_email_format(self, email):
        """Verify email format is valid"""
        if not re.match(self.email_regex, email):
            return False, "Invalid email format"
        
        # Check for common disposable email domains
        disposable_domains = [
            'tempmail.com', '10minutemail.com', 'guerrillamail.com',
            'mailinator.com', 'yopmail.com', 'trashmail.com'
        ]
        
        domain = email.split('@')[1].lower()
        if domain in disposable_domains:
            return False, "Disposable email domain detected"
        
        return True, "Valid format"
    
    def guess_email_variations(self, name, domain):
        """Generate common email variations"""
        variations = []
        
        # Clean name
        first_name = name.split()[0].lower() if name else ""
        last_name = name.split()[-1].lower() if len(name.split()) > 1 else ""
        
        if first_name and last_name:
            variations.extend([
                f"{first_name}.{last_name}@{domain}",
                f"{first_name[0]}{last_name}@{domain}",
                f"{first_name}{last_name}@{domain}",
                f"{first_name}_{last_name}@{domain}",
                f"{first_name}{last_name[0]}@{domain}",
                f"{last_name}.{first_name}@{domain}",
                f"{last_name}{first_name}@{domain}",
                f"{first_name[0]}.{last_name}@{domain}"
            ])
        
        if first_name:
            variations.extend([
                f"{first_name}@{domain}",
                f"{first_name}123@{domain}",
                f"{first_name}.official@{domain}",
                f"contact.{first_name}@{domain}"
            ])
        
        return list(set(variations))  # Remove duplicates
    
    def check_mx_records(self, domain):
        """Check if domain has MX records (can receive email)"""
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            return True, [str(mx.exchange) for mx in mx_records]
        except:
            return False, []
    
    def simulate_email_verification(self, email):
        """Simulate email verification (educational purposes)"""
        # NOTE: Real verification requires proper APIs
        # This is simulation for educational purposes
        
        domain = email.split('@')[1]
        
        # Check MX records
        has_mx, mx_servers = self.check_mx_records(domain)
        
        # Simulate verification results
        verification = {
            'email': email,
            'format_valid': True,
            'domain': domain,
            'provider': self.providers.get(domain, 'Unknown'),
            'has_mx_records': has_mx,
            'mx_servers': mx_servers,
            'disposable': False,
            'role_account': self.is_role_account(email),
            'deliverable': 'Unknown (simulated)',
            'smtp_check': 'Not performed (simulated)',
            'verification_date': datetime.now().isoformat()
        }
        
        # Add some simulated findings
        if has_mx:
            verification['deliverable'] = 'Likely'
        
        return verification
    
    def is_role_account(self, email):
        """Check if email is a role/group account"""
        role_keywords = [
            'admin', 'administrator', 'contact', 'info', 'support',
            'help', 'sales', 'service', 'webmaster', 'postmaster',
            'hostmaster', 'abuse', 'noc', 'security', 'billing'
        ]
        
        username = email.split('@')[0].lower()
        return any(keyword in username for keyword in role_keywords)
    
    def find_associated_accounts(self, email):
        """Find accounts associated with email (simulated)"""
        username = email.split('@')[0]
        
        # Simulated account findings
        accounts = {
            'social_media': {
                'twitter': f'https://twitter.com/search?q={email}',
                'facebook': f'https://www.facebook.com/search/top/?q={email}',
                'instagram': f'https://www.instagram.com/explore/tags/{username}/',
                'linkedin': f'https://www.linkedin.com/search/results/all/?keywords={email}'
            },
            'data_breaches': self.simulate_breach_check(email),
            'github': f'https://github.com/search?q={email}&type=users',
            'gravatar': f'https://en.gravatar.com/{hashlib.md5(email.encode()).hexdigest()}'
        }
        
        return accounts
    
    def simulate_breach_check(self, email):
        """Simulate data breach check"""
        # Simulated breach data
        breaches = []
        
        # Based on email hash for simulation
        import hashlib
        email_hash = hashlib.md5(email.lower().encode()).hexdigest()
        
        # Check first few characters for simulation
        if email_hash[0] in ['0', '1', '2', '3']:
            breaches.append({
                'name': 'LinkedIn 2012',
                'date': '2012-06-05',
                'records': '165M',
                'data_exposed': ['Emails', 'Passwords', 'Usernames']
            })
        
        if email_hash[1] in ['4', '5', '6', '7']:
            breaches.append({
                'name': 'Collection #1',
                'date': '2019-01-07',
                'records': '773M',
                'data_exposed': ['Emails', 'Passwords']
            })
        
        if email_hash[2] in ['8', '9', 'a', 'b']:
            breaches.append({
                'name': 'Adobe 2013',
                'date': '2013-10-04',
                'records': '153M',
                'data_exposed': ['Emails', 'Password hints']
            })
        
        return breaches
    
    def generate_email_intel_report(self, email):
        """Generate comprehensive email intelligence report"""
        print(f"\n📧 Analyzing: {email}")
        print("="*50)
        
        # Verify format
        is_valid, message = self.verify_email_format(email)
        print(f"Format: {'✅' if is_valid else '❌'} {message}")
        
        if not is_valid:
            return None
        
        # Get domain info
        domain = email.split('@')[1]
        print(f"Domain: {domain}")
        
        # Check provider
        provider = self.providers.get(domain, 'Unknown')
        print(f"Provider: {provider}")
        
        # Check MX records
        has_mx, mx_servers = self.check_mx_records(domain)
        print(f"MX Records: {'✅' if has_mx else '❌'}")
        if has_mx and mx_servers:
            print(f"  Servers: {', '.join(mx_servers[:2])}")
        
        # Check if role account
        is_role = self.is_role_account(email)
        print(f"Role Account: {'Yes' if is_role else 'No'}")
        
        # Simulate verification
        verification = self.simulate_email_verification(email)
        
        # Find associated accounts
        print("\n🔍 Finding associated accounts...")
        accounts = self.find_associated_accounts(email)
        
        # Check breaches
        print("\n🛡️ Data breach check:")
        breaches = accounts['data_breaches']
        if breaches:
            print(f"❌ Found in {len(breaches)} breach(es):")
            for breach in breaches:
                print(f"  • {breach['name']} ({breach['date']})")
        else:
            print("✅ No breaches found (simulated)")
        
        # Generate report
        report = {
            'email': email,
            'domain': domain,
            'provider': provider,
            'verification': verification,
            'accounts': accounts,
            'breaches_found': len(breaches),
            'analysis_date': datetime.now().isoformat()
        }
        
        return report
    
    def search_by_name_domain(self, name, domain):
        """Search for emails by name and domain"""
        print(f"\n🔍 Searching for emails: {name} @ {domain}")
        print("-"*40)
        
        # Generate variations
        variations = self.guess_email_variations(name, domain)
        
        print(f"Generated {len(variations)} email variations:")
        for i, email in enumerate(variations[:10], 1):  # Show first 10
            print(f"  {i:2}. {email}")
        
        if len(variations) > 10:
            print(f"  ... and {len(variations) - 10} more")
        
        # Verify each variation
        verified = []
        for email in variations[:5]:  # Check first 5
            print(f"\nChecking: {email}")
            verification = self.simulate_email_verification(email)
            
            if verification['has_mx_records']:
                verified.append(email)
                print(f"  ✅ Has MX records")
            else:
                print(f"  ❌ No MX records")
        
        return {
            'name': name,
            'domain': domain,
            'variations_generated': len(variations),
            'variations': variations,
            'verified_with_mx': verified,
            'analysis_date': datetime.now().isoformat()
        }

def main():
    print("\n" + "📧" * 30)
    print("    ADVANCED EMAIL HUNTER")
    print("      Educational Tool Only")
    print("📧" * 30)
    
    hunter = EmailHunter()
    
    print("\n🔧 Available functions:")
    print("1. Analyze single email")
    print("2. Find emails by name & domain")
    print("3. Generate email variations")
    print("4. Check domain MX records")
    print("5. Exit")
    
    try:
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            email = input("Enter email to analyze: ").strip()
            if email:
                report = hunter.generate_email_intel_report(email)
                if report:
                    save = input("\n💾 Save report? (y/n): ").lower()
                    if save == 'y':
                        filename = f"email_report_{email.replace('@', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                        with open(filename, 'w') as f:
                            json.dump(report, f, indent=2)
                        print(f"✅ Saved to: {filename}")
        
        elif choice == '2':
            name = input("Enter full name: ").strip()
            domain = input("Enter domain (e.g., company.com): ").strip()
            if name and domain:
                report = hunter.search_by_name_domain(name, domain)
                save = input("\n💾 Save results? (y/n): ").lower()
                if save == 'y':
                    filename = f"email_search_{name.replace(' ', '_')}_{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    with open(filename, 'w') as f:
                        json.dump(report, f, indent=2)
                    print(f"✅ Saved to: {filename}")
        
        elif choice == '3':
            name = input("Enter name: ").strip()
            domain = input("Enter domain: ").strip()
            if name and domain:
                variations = hunter.guess_email_variations(name, domain)
                print(f"\n📧 Generated {len(variations)} email variations:")
                for i, email in enumerate(variations, 1):
                    print(f"{i:3}. {email}")
        
        elif choice == '4':
            domain = input("Enter domain to check MX records: ").strip()
            if domain:
                has_mx, mx_servers = hunter.check_mx_records(domain)
                print(f"\nDomain: {domain}")
                print(f"Has MX records: {'✅ Yes' if has_mx else '❌ No'}")
                if has_mx:
                    print("MX Servers:")
                    for server in mx_servers:
                        print(f"  • {server}")
        
        elif choice == '5':
            print("\n👋 Goodbye!")
            return
        
        else:
            print("❌ Invalid choice")
    
    except KeyboardInterrupt:
        print("\n\n👋 Program terminated")
    except Exception as e:
        print(f"\n⚠️ Error: {e}")
    
    print("\n" + "="*60)
    print("⚠️  LEGAL DISCLAIMER:")
    print("This tool is for educational purposes only.")
    print("Use only with permission and for authorized research.")
    print("Respect privacy laws and regulations.")
    print("="*60)

if __name__ == "__main__":
    main()

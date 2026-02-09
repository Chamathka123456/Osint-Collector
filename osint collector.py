#!/usr/bin/env python3
"""
🕵️ OSINT Information Collector - Advanced Edition
Gathers publicly available emails, usernames, and information
FOR LEGAL ETHICAL RESEARCH ONLY
"""

import os
import sys
import json
import time
import re
import requests
import phonenumbers
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import hashlib

class OSINTCollector:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        # Common email patterns
        self.email_patterns = [
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            r'[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|outlook|hotmail|protonmail)\.(?:com|net|org)',
        ]
        
        # Common username patterns
        self.username_patterns = [
            r'@([A-Za-z0-9_]{3,30})',
            r'username[:=]\s*([A-Za-z0-9_]{3,30})',
            r'user[:=]\s*([A-Za-z0-9_]{3,30})',
        ]
        
        # Data breach databases (educational simulation)
        self.breach_patterns = {
            'rockyou': r'password.*[:=].*',
            'linkedin_2012': r'linkedin.*2012.*breach',
            'collection1': r'collection.*#1.*credentials'
        }
    
    def extract_emails_from_text(self, text):
        """Extract email addresses from text"""
        emails = set()
        for pattern in self.email_patterns:
            found = re.findall(pattern, text, re.IGNORECASE)
            emails.update(found)
        return list(emails)
    
    def extract_usernames_from_text(self, text):
        """Extract usernames from text"""
        usernames = set()
        for pattern in self.username_patterns:
            found = re.findall(pattern, text, re.IGNORECASE)
            usernames.update(found)
        return list(usernames)
    
    def search_google_dorks(self, query):
        """Generate Google dorks for OSINT (Educational)"""
        dorks = [
            f'"{query}" site:linkedin.com',
            f'"{query}" site:facebook.com',
            f'"{query}" site:twitter.com',
            f'"{query}" site:instagram.com',
            f'"{query}" "@gmail.com" OR "@yahoo.com"',
            f'"{query}" filetype:pdf OR filetype:doc OR filetype:docx',
            f'"{query}" intext:"@gmail.com" OR intext:"contact"',
            f'"{query}" "email" OR "contact" OR "reach"',
        ]
        return dorks
    
    def check_haveibeenpwned_simulated(self, email):
        """Simulate checking HaveIBeenPwned (Educational)"""
        # NOTE: Real API requires subscription
        # This is simulation for educational purposes
        
        common_breaches = {
            'linkedin_2012': {
                'name': 'LinkedIn 2012',
                'date': '2012-06-05',
                'records': '165 million',
                'data_classes': ['Email addresses', 'Passwords', 'Usernames']
            },
            'collection1': {
                'name': 'Collection #1',
                'date': '2019-01-07',
                'records': '773 million',
                'data_classes': ['Email addresses', 'Passwords']
            },
            'adobe_2013': {
                'name': 'Adobe 2013',
                'date': '2013-10-04',
                'records': '153 million',
                'data_classes': ['Email addresses', 'Password hints', 'Usernames']
            }
        }
        
        # Simulate finding breaches based on email hash
        email_hash = hashlib.md5(email.lower().encode()).hexdigest()
        breaches_found = []
        
        # Check first character of hash to simulate probability
        if email_hash[0] in ['a', 'b', 'c', 'd']:
            breaches_found.append(common_breaches['linkedin_2012'])
        if email_hash[1] in ['e', 'f', 'g', 'h']:
            breaches_found.append(common_breaches['collection1'])
        if email_hash[2] in ['i', 'j', 'k', 'l']:
            breaches_found.append(common_breaches['adobe_2013'])
        
        return breaches_found
    
    def search_social_media(self, username):
        """Check if username exists on social media (simulated)"""
        platforms = {
            'twitter': f'https://twitter.com/{username}',
            'instagram': f'https://instagram.com/{username}',
            'github': f'https://github.com/{username}',
            'reddit': f'https://reddit.com/user/{username}',
            'pinterest': f'https://pinterest.com/{username}',
            'tumblr': f'https://{username}.tumblr.com',
        }
        
        results = {}
        for platform, url in platforms.items():
            # Simulate checking (in real tool, you'd make HTTP requests)
            results[platform] = {
                'url': url,
                'exists': 'Possibly',  # Simulation
                'last_checked': datetime.now().isoformat()
            }
        
        return results
    
    def find_associated_emails(self, phone_number):
        """Find emails associated with a phone number (simulated patterns)"""
        # Clean phone number
        clean_phone = re.sub(r'[^0-9]', '', phone_number)
        if clean_phone.startswith('94'):
            clean_phone = clean_phone[2:]  # Remove country code
        
        # Common email patterns based on phone
        possible_emails = []
        
        # Pattern 1: phone@gmail.com
        possible_emails.append(f"{clean_phone}@gmail.com")
        
        # Pattern 2: first 7 digits
        if len(clean_phone) >= 7:
            possible_emails.append(f"{clean_phone[:7]}@yahoo.com")
        
        # Pattern 3: with name variations (simulated)
        name_variations = ['john', 'saman', 'kamal', 'nimal', 'sarah']
        for name in name_variations[:2]:  # Only check first 2 for simulation
            possible_emails.append(f"{name}.{clean_phone[-4:]}@gmail.com")
            possible_emails.append(f"{name}{clean_phone[-3:]}@outlook.com")
        
        return list(set(possible_emails))  # Remove duplicates
    
    def search_public_records_simulated(self, name, phone=None, email=None):
        """Simulate searching public records"""
        records = {
            'people_search_engines': [
                'BeenVerified',
                'Spokeo',
                'Whitepages',
                'TruePeopleSearch',
                'FastPeopleSearch'
            ],
            'possible_matches': [],
            'associated_addresses': [],
            'relatives': []
        }
        
        # Generate simulated matches
        if name:
            # Common Sri Lankan names
            surnames = ['Perera', 'Fernando', 'Silva', 'De Silva', 'Ratnayake', 'Wijesinghe']
            cities = ['Colombo', 'Kandy', 'Galle', 'Jaffna', 'Negombo', 'Kurunegala']
            
            for surname in surnames[:3]:
                records['possible_matches'].append({
                    'name': f"{name} {surname}",
                    'location': f"{cities[len(name) % len(cities)]}, Sri Lanka",
                    'age_range': f"{(len(name) * 5) % 50 + 20}-{(len(name) * 5) % 50 + 30}",
                    'confidence': f"{70 + (len(name) * 3) % 30}%"
                })
        
        if phone:
            # Generate addresses based on phone prefix
            prefix = phone[3:5] if len(phone) > 4 else '70'
            areas = {
                '70': 'Colombo 03',
                '71': 'Colombo 07',
                '72': 'Colombo 05',
                '77': 'Colombo 01',
                '81': 'Kandy City'
            }
            
            if prefix in areas:
                records['associated_addresses'].append({
                    'address': f"123 Main Street, {areas[prefix]}",
                    'type': 'Possible',
                    'source': 'Phone prefix analysis'
                })
        
        return records
    
    def generate_email_report(self, email):
        """Generate comprehensive email report"""
        print(f"\n📧 Analyzing email: {email}")
        print("-" * 40)
        
        # Check breaches (simulated)
        print("🔍 Checking data breaches...")
        breaches = self.check_haveibeenpwned_simulated(email)
        
        if breaches:
            print(f"❌ Found in {len(breaches)} data breaches:")
            for breach in breaches:
                print(f"  • {breach['name']} ({breach['date']})")
                print(f"    Records: {breach['records']}")
                print(f"    Data exposed: {', '.join(breach['data_classes'])}")
        else:
            print("✅ No known breaches found (simulated)")
        
        # Extract username from email
        username = email.split('@')[0]
        print(f"\n👤 Username extracted: {username}")
        
        # Check social media (simulated)
        print("\n🌐 Checking social media presence...")
        social = self.search_social_media(username)
        
        for platform, data in social.items():
            print(f"  • {platform.capitalize()}: {data['url']}")
            print(f"    Exists: {data['exists']}")
        
        return {
            'email': email,
            'username': username,
            'breaches_found': len(breaches),
            'breach_details': breaches,
            'social_media': social,
            'analysis_date': datetime.now().isoformat()
        }
    
    def generate_phone_report(self, phone_number):
        """Generate comprehensive phone report"""
        print(f"\n📞 Analyzing phone: {phone_number}")
        print("-" * 40)
        
        try:
            parsed = phonenumbers.parse(phone_number, None)
            carrier_info = phonenumbers.carrier.name_for_number(parsed, 'en') or 'Unknown'
            country = phonenumbers.geocoder.description_for_number(parsed, 'en')
            
            print(f"📍 Country: {country}")
            print(f"📡 Carrier: {carrier_info}")
            print(f"✅ Valid: {phonenumbers.is_valid_number(parsed)}")
            
            # Find associated emails
            print("\n🔗 Finding associated emails...")
            associated_emails = self.find_associated_emails(phone_number)
            
            if associated_emails:
                print(f"Found {len(associated_emails)} possible email patterns:")
                for email in associated_emails[:5]:  # Show first 5
                    print(f"  • {email}")
            else:
                print("No email patterns found")
            
            # Generate Google dorks
            print("\n🔍 Google search suggestions:")
            dorks = self.search_google_dorks(phone_number)
            for i, dork in enumerate(dorks[:3], 1):
                print(f"  {i}. {dork}")
            
            return {
                'phone': phone_number,
                'country': country,
                'carrier': carrier_info,
                'is_valid': phonenumbers.is_valid_number(parsed),
                'associated_emails': associated_emails,
                'google_dorks': dorks,
                'analysis_date': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def generate_name_report(self, full_name):
        """Generate comprehensive name report"""
        print(f"\n👤 Analyzing name: {full_name}")
        print("-" * 40)
        
        # Extract first and last name
        name_parts = full_name.split()
        first_name = name_parts[0] if name_parts else ""
        last_name = name_parts[-1] if len(name_parts) > 1 else ""
        
        print(f"📝 First name: {first_name}")
        print(f"📝 Last name: {last_name}")
        
        # Common email patterns
        print("\n📧 Possible email patterns:")
        email_patterns = []
        
        if first_name and last_name:
            email_patterns.extend([
                f"{first_name}.{last_name}@gmail.com",
                f"{first_name[0]}{last_name}@yahoo.com",
                f"{first_name}{last_name[0]}@outlook.com",
                f"{first_name.lower()}_{last_name.lower()}@protonmail.com"
            ])
        
        if first_name:
            email_patterns.extend([
                f"{first_name}123@gmail.com",
                f"{first_name}.official@yahoo.com",
                f"official.{first_name}@gmail.com"
            ])
        
        for email in email_patterns:
            print(f"  • {email}")
        
        # Search public records (simulated)
        print("\n📁 Searching public records (simulated)...")
        records = self.search_public_records_simulated(full_name)
        
        if records['possible_matches']:
            print(f"Found {len(records['possible_matches'])} possible matches:")
            for match in records['possible_matches'][:3]:  # Show first 3
                print(f"  • {match['name']} in {match['location']}")
                print(f"    Age: {match['age_range']}, Confidence: {match['confidence']}")
        
        # Social media check
        print("\n🌐 Social media username suggestions:")
        username_suggestions = []
        
        if first_name and last_name:
            username_suggestions.extend([
                f"{first_name}{last_name}",
                f"{first_name}.{last_name}",
                f"{first_name[0]}{last_name}",
                f"{first_name}_{last_name}",
                f"{first_name.lower()}{last_name.lower()}"
            ])
        
        for username in username_suggestions[:5]:
            print(f"  • @{username}")
        
        return {
            'full_name': full_name,
            'first_name': first_name,
            'last_name': last_name,
            'email_patterns': email_patterns,
            'username_suggestions': username_suggestions,
            'public_records': records,
            'analysis_date': datetime.now().isoformat()
        }
    
    def save_full_report(self, reports, output_file=None):
        """Save all reports to a JSON file"""
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"osint_report_{timestamp}.json"
        
        with open(output_file, 'w') as f:
            json.dump(reports, f, indent=2, default=str)
        
        return output_file

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                 🕵️ OSINT INFORMATION GATHERER                  ║
    ║              Advanced Public Data Collection Tool              ║
    ║                                                                ║
    ║      ⚠️  FOR LEGAL ETHICAL RESEARCH PURPOSES ONLY ⚠️         ║
    ║      Use only for yourself or with explicit permission         ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    print_banner()
    
    # Check dependencies
    try:
        import phonenumbers
        import requests
    except ImportError:
        print("❌ Missing required packages!")
        print("Installing dependencies...")
        os.system(f"{sys.executable} -m pip install phonenumbers requests")
        print("✅ Please restart the script!")
        return
    
    collector = OSINTCollector()
    all_reports = {}
    
    print("\n📊 What would you like to search?")
    print("1. Email address")
    print("2. Phone number")
    print("3. Full name")
    print("4. Multiple inputs")
    print("5. Exit")
    
    try:
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            email = input("Enter email address: ").strip()
            if '@' in email:
                report = collector.generate_email_report(email)
                all_reports['email_report'] = report
            else:
                print("❌ Invalid email format")
                
        elif choice == '2':
            phone = input("Enter phone number (with country code): ").strip()
            if phone:
                if not phone.startswith('+'):
                    phone = '+94' + phone.lstrip('0')
                report = collector.generate_phone_report(phone)
                if report:
                    all_reports['phone_report'] = report
                    
        elif choice == '3':
            name = input("Enter full name: ").strip()
            if name:
                report = collector.generate_name_report(name)
                all_reports['name_report'] = report
                
        elif choice == '4':
            print("\n📥 Enter multiple pieces of information (press Enter to skip):")
            
            email = input("Email: ").strip()
            if email and '@' in email:
                print("\n📧 Analyzing email...")
                report = collector.generate_email_report(email)
                all_reports['email_report'] = report
            
            phone = input("\nPhone: ").strip()
            if phone:
                if not phone.startswith('+'):
                    phone = '+94' + phone.lstrip('0')
                print("\n📞 Analyzing phone...")
                report = collector.generate_phone_report(phone)
                if report:
                    all_reports['phone_report'] = report
            
            name = input("\nName: ").strip()
            if name:
                print("\n👤 Analyzing name...")
                report = collector.generate_name_report(name)
                all_reports['name_report'] = report
        
        elif choice == '5':
            print("\n👋 Goodbye!")
            return
        
        else:
            print("❌ Invalid choice")
            return
        
        # Save report if we have data
        if all_reports:
            save = input("\n💾 Save full report to file? (y/n): ").lower()
            if save == 'y':
                filename = collector.save_full_report(all_reports)
                print(f"✅ Report saved to: {filename}")
                
                # Show summary
                print("\n" + "="*60)
                print("📋 REPORT SUMMARY")
                print("="*60)
                
                if 'email_report' in all_reports:
                    report = all_reports['email_report']
                    print(f"📧 Email: {report['email']}")
                    print(f"   Breaches found: {report['breaches_found']}")
                    print(f"   Username: {report['username']}")
                
                if 'phone_report' in all_reports:
                    report = all_reports['phone_report']
                    print(f"\n📞 Phone: {report['phone']}")
                    print(f"   Country: {report['country']}")
                    print(f"   Associated emails: {len(report.get('associated_emails', []))}")
                
                if 'name_report' in all_reports:
                    report = all_reports['name_report']
                    print(f"\n👤 Name: {report['full_name']}")
                    print(f"   Email patterns: {len(report['email_patterns'])}")
                    print(f"   Username suggestions: {len(report['username_suggestions'])}")
                
                print("\n" + "="*60)
                print("⚠️  REMEMBER: This is simulated data for educational purposes")
                print("="*60)
        
        else:
            print("\n❌ No data collected")
        
        print("\n" + "💡" * 30)
        print("   Important Reminders:")
        print("   1. Use only for authorized research")
        print("   2. Respect privacy and laws")
        print("   3. This is simulated/educational data")
        print("   4. Real OSINT requires proper tools and training")
        print("💡" * 30)
        
    except KeyboardInterrupt:
        print("\n\n👋 Program terminated")
    except Exception as e:
        print(f"\n⚠️ Error: {e}")

if __name__ == "__main__":
    main()#!/usr/bin/env python3
"""
🕵️ OSINT Information Collector - Advanced Edition
Gathers publicly available emails, usernames, and information
FOR LEGAL ETHICAL RESEARCH ONLY
"""

import os
import sys
import json
import time
import re
import requests
import phonenumbers
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import hashlib

class OSINTCollector:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        # Common email patterns
        self.email_patterns = [
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            r'[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|outlook|hotmail|protonmail)\.(?:com|net|org)',
        ]
        
        # Common username patterns
        self.username_patterns = [
            r'@([A-Za-z0-9_]{3,30})',
            r'username[:=]\s*([A-Za-z0-9_]{3,30})',
            r'user[:=]\s*([A-Za-z0-9_]{3,30})',
        ]
        
        # Data breach databases (educational simulation)
        self.breach_patterns = {
            'rockyou': r'password.*[:=].*',
            'linkedin_2012': r'linkedin.*2012.*breach',
            'collection1': r'collection.*#1.*credentials'
        }
    
    def extract_emails_from_text(self, text):
        """Extract email addresses from text"""
        emails = set()
        for pattern in self.email_patterns:
            found = re.findall(pattern, text, re.IGNORECASE)
            emails.update(found)
        return list(emails)
    
    def extract_usernames_from_text(self, text):
        """Extract usernames from text"""
        usernames = set()
        for pattern in self.username_patterns:
            found = re.findall(pattern, text, re.IGNORECASE)
            usernames.update(found)
        return list(usernames)
    
    def search_google_dorks(self, query):
        """Generate Google dorks for OSINT (Educational)"""
        dorks = [
            f'"{query}" site:linkedin.com',
            f'"{query}" site:facebook.com',
            f'"{query}" site:twitter.com',
            f'"{query}" site:instagram.com',
            f'"{query}" "@gmail.com" OR "@yahoo.com"',
            f'"{query}" filetype:pdf OR filetype:doc OR filetype:docx',
            f'"{query}" intext:"@gmail.com" OR intext:"contact"',
            f'"{query}" "email" OR "contact" OR "reach"',
        ]
        return dorks
    
    def check_haveibeenpwned_simulated(self, email):
        """Simulate checking HaveIBeenPwned (Educational)"""
        # NOTE: Real API requires subscription
        # This is simulation for educational purposes
        
        common_breaches = {
            'linkedin_2012': {
                'name': 'LinkedIn 2012',
                'date': '2012-06-05',
                'records': '165 million',
                'data_classes': ['Email addresses', 'Passwords', 'Usernames']
            },
            'collection1': {
                'name': 'Collection #1',
                'date': '2019-01-07',
                'records': '773 million',
                'data_classes': ['Email addresses', 'Passwords']
            },
            'adobe_2013': {
                'name': 'Adobe 2013',
                'date': '2013-10-04',
                'records': '153 million',
                'data_classes': ['Email addresses', 'Password hints', 'Usernames']
            }
        }
        
        # Simulate finding breaches based on email hash
        email_hash = hashlib.md5(email.lower().encode()).hexdigest()
        breaches_found = []
        
        # Check first character of hash to simulate probability
        if email_hash[0] in ['a', 'b', 'c', 'd']:
            breaches_found.append(common_breaches['linkedin_2012'])
        if email_hash[1] in ['e', 'f', 'g', 'h']:
            breaches_found.append(common_breaches['collection1'])
        if email_hash[2] in ['i', 'j', 'k', 'l']:
            breaches_found.append(common_breaches['adobe_2013'])
        
        return breaches_found
    
    def search_social_media(self, username):
        """Check if username exists on social media (simulated)"""
        platforms = {
            'twitter': f'https://twitter.com/{username}',
            'instagram': f'https://instagram.com/{username}',
            'github': f'https://github.com/{username}',
            'reddit': f'https://reddit.com/user/{username}',
            'pinterest': f'https://pinterest.com/{username}',
            'tumblr': f'https://{username}.tumblr.com',
        }
        
        results = {}
        for platform, url in platforms.items():
            # Simulate checking (in real tool, you'd make HTTP requests)
            results[platform] = {
                'url': url,
                'exists': 'Possibly',  # Simulation
                'last_checked': datetime.now().isoformat()
            }
        
        return results
    
    def find_associated_emails(self, phone_number):
        """Find emails associated with a phone number (simulated patterns)"""
        # Clean phone number
        clean_phone = re.sub(r'[^0-9]', '', phone_number)
        if clean_phone.startswith('94'):
            clean_phone = clean_phone[2:]  # Remove country code
        
        # Common email patterns based on phone
        possible_emails = []
        
        # Pattern 1: phone@gmail.com
        possible_emails.append(f"{clean_phone}@gmail.com")
        
        # Pattern 2: first 7 digits
        if len(clean_phone) >= 7:
            possible_emails.append(f"{clean_phone[:7]}@yahoo.com")
        
        # Pattern 3: with name variations (simulated)
        name_variations = ['john', 'saman', 'kamal', 'nimal', 'sarah']
        for name in name_variations[:2]:  # Only check first 2 for simulation
            possible_emails.append(f"{name}.{clean_phone[-4:]}@gmail.com")
            possible_emails.append(f"{name}{clean_phone[-3:]}@outlook.com")
        
        return list(set(possible_emails))  # Remove duplicates
    
    def search_public_records_simulated(self, name, phone=None, email=None):
        """Simulate searching public records"""
        records = {
            'people_search_engines': [
                'BeenVerified',
                'Spokeo',
                'Whitepages',
                'TruePeopleSearch',
                'FastPeopleSearch'
            ],
            'possible_matches': [],
            'associated_addresses': [],
            'relatives': []
        }
        
        # Generate simulated matches
        if name:
            # Common Sri Lankan names
            surnames = ['Perera', 'Fernando', 'Silva', 'De Silva', 'Ratnayake', 'Wijesinghe']
            cities = ['Colombo', 'Kandy', 'Galle', 'Jaffna', 'Negombo', 'Kurunegala']
            
            for surname in surnames[:3]:
                records['possible_matches'].append({
                    'name': f"{name} {surname}",
                    'location': f"{cities[len(name) % len(cities)]}, Sri Lanka",
                    'age_range': f"{(len(name) * 5) % 50 + 20}-{(len(name) * 5) % 50 + 30}",
                    'confidence': f"{70 + (len(name) * 3) % 30}%"
                })
        
        if phone:
            # Generate addresses based on phone prefix
            prefix = phone[3:5] if len(phone) > 4 else '70'
            areas = {
                '70': 'Colombo 03',
                '71': 'Colombo 07',
                '72': 'Colombo 05',
                '77': 'Colombo 01',
                '81': 'Kandy City'
            }
            
            if prefix in areas:
                records['associated_addresses'].append({
                    'address': f"123 Main Street, {areas[prefix]}",
                    'type': 'Possible',
                    'source': 'Phone prefix analysis'
                })
        
        return records
    
    def generate_email_report(self, email):
        """Generate comprehensive email report"""
        print(f"\n📧 Analyzing email: {email}")
        print("-" * 40)
        
        # Check breaches (simulated)
        print("🔍 Checking data breaches...")
        breaches = self.check_haveibeenpwned_simulated(email)
        
        if breaches:
            print(f"❌ Found in {len(breaches)} data breaches:")
            for breach in breaches:
                print(f"  • {breach['name']} ({breach['date']})")
                print(f"    Records: {breach['records']}")
                print(f"    Data exposed: {', '.join(breach['data_classes'])}")
        else:
            print("✅ No known breaches found (simulated)")
        
        # Extract username from email
        username = email.split('@')[0]
        print(f"\n👤 Username extracted: {username}")
        
        # Check social media (simulated)
        print("\n🌐 Checking social media presence...")
        social = self.search_social_media(username)
        
        for platform, data in social.items():
            print(f"  • {platform.capitalize()}: {data['url']}")
            print(f"    Exists: {data['exists']}")
        
        return {
            'email': email,
            'username': username,
            'breaches_found': len(breaches),
            'breach_details': breaches,
            'social_media': social,
            'analysis_date': datetime.now().isoformat()
        }
    
    def generate_phone_report(self, phone_number):
        """Generate comprehensive phone report"""
        print(f"\n📞 Analyzing phone: {phone_number}")
        print("-" * 40)
        
        try:
            parsed = phonenumbers.parse(phone_number, None)
            carrier_info = phonenumbers.carrier.name_for_number(parsed, 'en') or 'Unknown'
            country = phonenumbers.geocoder.description_for_number(parsed, 'en')
            
            print(f"📍 Country: {country}")
            print(f"📡 Carrier: {carrier_info}")
            print(f"✅ Valid: {phonenumbers.is_valid_number(parsed)}")
            
            # Find associated emails
            print("\n🔗 Finding associated emails...")
            associated_emails = self.find_associated_emails(phone_number)
            
            if associated_emails:
                print(f"Found {len(associated_emails)} possible email patterns:")
                for email in associated_emails[:5]:  # Show first 5
                    print(f"  • {email}")
            else:
                print("No email patterns found")
            
            # Generate Google dorks
            print("\n🔍 Google search suggestions:")
            dorks = self.search_google_dorks(phone_number)
            for i, dork in enumerate(dorks[:3], 1):
                print(f"  {i}. {dork}")
            
            return {
                'phone': phone_number,
                'country': country,
                'carrier': carrier_info,
                'is_valid': phonenumbers.is_valid_number(parsed),
                'associated_emails': associated_emails,
                'google_dorks': dorks,
                'analysis_date': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def generate_name_report(self, full_name):
        """Generate comprehensive name report"""
        print(f"\n👤 Analyzing name: {full_name}")
        print("-" * 40)
        
        # Extract first and last name
        name_parts = full_name.split()
        first_name = name_parts[0] if name_parts else ""
        last_name = name_parts[-1] if len(name_parts) > 1 else ""
        
        print(f"📝 First name: {first_name}")
        print(f"📝 Last name: {last_name}")
        
        # Common email patterns
        print("\n📧 Possible email patterns:")
        email_patterns = []
        
        if first_name and last_name:
            email_patterns.extend([
                f"{first_name}.{last_name}@gmail.com",
                f"{first_name[0]}{last_name}@yahoo.com",
                f"{first_name}{last_name[0]}@outlook.com",
                f"{first_name.lower()}_{last_name.lower()}@protonmail.com"
            ])
        
        if first_name:
            email_patterns.extend([
                f"{first_name}123@gmail.com",
                f"{first_name}.official@yahoo.com",
                f"official.{first_name}@gmail.com"
            ])
        
        for email in email_patterns:
            print(f"  • {email}")
        
        # Search public records (simulated)
        print("\n📁 Searching public records (simulated)...")
        records = self.search_public_records_simulated(full_name)
        
        if records['possible_matches']:
            print(f"Found {len(records['possible_matches'])} possible matches:")
            for match in records['possible_matches'][:3]:  # Show first 3
                print(f"  • {match['name']} in {match['location']}")
                print(f"    Age: {match['age_range']}, Confidence: {match['confidence']}")
        
        # Social media check
        print("\n🌐 Social media username suggestions:")
        username_suggestions = []
        
        if first_name and last_name:
            username_suggestions.extend([
                f"{first_name}{last_name}",
                f"{first_name}.{last_name}",
                f"{first_name[0]}{last_name}",
                f"{first_name}_{last_name}",
                f"{first_name.lower()}{last_name.lower()}"
            ])
        
        for username in username_suggestions[:5]:
            print(f"  • @{username}")
        
        return {
            'full_name': full_name,
            'first_name': first_name,
            'last_name': last_name,
            'email_patterns': email_patterns,
            'username_suggestions': username_suggestions,
            'public_records': records,
            'analysis_date': datetime.now().isoformat()
        }
    
    def save_full_report(self, reports, output_file=None):
        """Save all reports to a JSON file"""
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"osint_report_{timestamp}.json"
        
        with open(output_file, 'w') as f:
            json.dump(reports, f, indent=2, default=str)
        
        return output_file

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                 🕵️ OSINT INFORMATION GATHERER                  ║
    ║              Advanced Public Data Collection Tool              ║
    ║                                                                ║
    ║      ⚠️  FOR LEGAL ETHICAL RESEARCH PURPOSES ONLY ⚠️         ║
    ║      Use only for yourself or with explicit permission         ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    print_banner()
    
    # Check dependencies
    try:
        import phonenumbers
        import requests
    except ImportError:
        print("❌ Missing required packages!")
        print("Installing dependencies...")
        os.system(f"{sys.executable} -m pip install phonenumbers requests")
        print("✅ Please restart the script!")
        return
    
    collector = OSINTCollector()
    all_reports = {}
    
    print("\n📊 What would you like to search?")
    print("1. Email address")
    print("2. Phone number")
    print("3. Full name")
    print("4. Multiple inputs")
    print("5. Exit")
    
    try:
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            email = input("Enter email address: ").strip()
            if '@' in email:
                report = collector.generate_email_report(email)
                all_reports['email_report'] = report
            else:
                print("❌ Invalid email format")
                
        elif choice == '2':
            phone = input("Enter phone number (with country code): ").strip()
            if phone:
                if not phone.startswith('+'):
                    phone = '+94' + phone.lstrip('0')
                report = collector.generate_phone_report(phone)
                if report:
                    all_reports['phone_report'] = report
                    
        elif choice == '3':
            name = input("Enter full name: ").strip()
            if name:
                report = collector.generate_name_report(name)
                all_reports['name_report'] = report
                
        elif choice == '4':
            print("\n📥 Enter multiple pieces of information (press Enter to skip):")
            
            email = input("Email: ").strip()
            if email and '@' in email:
                print("\n📧 Analyzing email...")
                report = collector.generate_email_report(email)
                all_reports['email_report'] = report
            
            phone = input("\nPhone: ").strip()
            if phone:
                if not phone.startswith('+'):
                    phone = '+94' + phone.lstrip('0')
                print("\n📞 Analyzing phone...")
                report = collector.generate_phone_report(phone)
                if report:
                    all_reports['phone_report'] = report
            
            name = input("\nName: ").strip()
            if name:
                print("\n👤 Analyzing name...")
                report = collector.generate_name_report(name)
                all_reports['name_report'] = report
        
        elif choice == '5':
            print("\n👋 Goodbye!")
            return
        
        else:
            print("❌ Invalid choice")
            return
        
        # Save report if we have data
        if all_reports:
            save = input("\n💾 Save full report to file? (y/n): ").lower()
            if save == 'y':
                filename = collector.save_full_report(all_reports)
                print(f"✅ Report saved to: {filename}")
                
                # Show summary
                print("\n" + "="*60)
                print("📋 REPORT SUMMARY")
                print("="*60)
                
                if 'email_report' in all_reports:
                    report = all_reports['email_report']
                    print(f"📧 Email: {report['email']}")
                    print(f"   Breaches found: {report['breaches_found']}")
                    print(f"   Username: {report['username']}")
                
                if 'phone_report' in all_reports:
                    report = all_reports['phone_report']
                    print(f"\n📞 Phone: {report['phone']}")
                    print(f"   Country: {report['country']}")
                    print(f"   Associated emails: {len(report.get('associated_emails', []))}")
                
                if 'name_report' in all_reports:
                    report = all_reports['name_report']
                    print(f"\n👤 Name: {report['full_name']}")
                    print(f"   Email patterns: {len(report['email_patterns'])}")
                    print(f"   Username suggestions: {len(report['username_suggestions'])}")
                
                print("\n" + "="*60)
                print("⚠️  REMEMBER: This is simulated data for educational purposes")
                print("="*60)
        
        else:
            print("\n❌ No data collected")
        
        print("\n" + "💡" * 30)
        print("   Important Reminders:")
        print("   1. Use only for authorized research")
        print("   2. Respect privacy and laws")
        print("   3. This is simulated/educational data")
        print("   4. Real OSINT requires proper tools and training")
        print("💡" * 30)
        
    except KeyboardInterrupt:
        print("\n\n👋 Program terminated")
    except Exception as e:
        print(f"\n⚠️ Error: {e}")

if __name__ == "__main__":
    main()

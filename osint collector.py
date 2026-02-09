#!/usr/bin/env python3
"""
🔍 OSINT Collector v2.0 - Complete Edition
Educational & Authorized Use Only
"""

import os
import sys
import json
import time
import logging
from datetime import datetime, timedelta
import hashlib

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class OSINTCollector:
    def __init__(self):
        self.version = "2.0"
        self.author = "OSINT Research Team"
        self.license = "Educational Use Only"
        self.setup_logging()
        self.setup_directories()
        
    def setup_logging(self):
        """Configure secure logging system"""
        os.makedirs('logs', exist_ok=True)
        
        log_file = f"logs/osint_{datetime.now().strftime('%Y%m%d')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"OSINT Collector v{self.version} started")
        
    def setup_directories(self):
        """Create necessary directories"""
        directories = ['reports', 'exports', 'cache', 'tmp']
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            
    def check_dependencies(self):
        """Verify all required packages are installed"""
        required = ['phonenumbers', 'requests', 'dnspython', 'cryptography']
        missing = []
        
        for package in required:
            try:
                __import__(package.replace('-', '_'))
                self.logger.info(f"✓ {package} loaded")
            except ImportError:
                missing.append(package)
                self.logger.error(f"✗ {package} missing")
        
        if missing:
            print(f"\n❌ Missing packages: {', '.join(missing)}")
            print(f"Install with: pip install {' '.join(missing)}")
            return False
            
        return True
        
    def display_banner(self):
        """Display application banner"""
        banner = f"""
        ╔══════════════════════════════════════════════════════════╗
        ║               🔍 OSINT COLLECTOR v{self.version}               ║
        ║            Advanced Information Gathering Tool           ║
        ║                                                          ║
        ║    ⚠️  FOR EDUCATIONAL & AUTHORIZED RESEARCH ONLY ⚠️    ║
        ║        Use only with explicit permission                 ║
        ╚══════════════════════════════════════════════════════════╝
        
        📊 Features:
        • Phone Number Analysis       • Email Intelligence
        • Username Enumeration        • Domain Investigation
        • Social Media Recon          • Report Generation
        • Data Encryption             • Audit Logging
        
        📍 Current Directory: {os.getcwd()}
        ⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        print(banner)
        
    def get_legal_consent(self):
        """Obtain user consent and verify understanding"""
        legal_text = """
        ╔══════════════════════════════════════════════════════════╗
        ║                    TERMS OF USE                          ║
        ╚══════════════════════════════════════════════════════════╝
        
        By using this tool, you agree to:
        
        1. LEGAL COMPLIANCE
           • Only research yourself or with EXPLICIT WRITTEN permission
           • Comply with GDPR, CCPA, and all applicable privacy laws
           • Never violate platform Terms of Service
        
        2. ETHICAL USE
           • NO harassment, stalking, or doxxing
           • NO illegal or malicious activities
           • Respect all privacy rights
        
        3. DATA PROTECTION
           • Encrypt sensitive information
           • Delete data after legitimate use
           • Maintain confidentiality
        
        4. ACCOUNTABILITY
           • All searches are logged
           • You are responsible for your actions
           • Misuse may have legal consequences
        
        Type 'I AGREE' to continue or anything else to exit.
        """
        
        print(legal_text)
        consent = input("\n➤ Enter 'I AGREE' to continue: ").strip()
        
        if consent != 'I AGREE':
            print("\n❌ Access denied. You must agree to the terms.")
            self.logger.warning("User declined terms")
            sys.exit(0)
            
        self.logger.info("User agreed to terms")
        return True
        
    def main_menu(self):
        """Display main menu"""
        while True:
            print("\n" + "═" * 70)
            print("📊 MAIN CONTROL PANEL")
            print("═" * 70)
            print("1. 🔍 Phone Number Intelligence")
            print("2. 📧 Email Address Analysis")
            print("3. 👤 Username Investigation")
            print("4. 🌐 Domain & Website Recon")
            print("5. 📱 Social Media Lookup")
            print("6. 📄 Generate Comprehensive Report")
            print("7. ⚙️  Settings & Configuration")
            print("8. 📖 View Documentation")
            print("9. 🚪 Exit")
            print("═" * 70)
            
            try:
                choice = input("\n➤ Select option (1-9): ").strip()
                
                if choice == '1':
                    self.phone_intelligence()
                elif choice == '2':
                    self.email_analysis()
                elif choice == '3':
                    self.username_investigation()
                elif choice == '4':
                    self.domain_recon()
                elif choice == '5':
                    self.social_media_lookup()
                elif choice == '6':
                    self.generate_report()
                elif choice == '7':
                    self.settings_menu()
                elif choice == '8':
                    self.show_documentation()
                elif choice == '9':
                    self.exit_program()
                else:
                    print("❌ Invalid selection")
                    
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user")
                self.exit_program()
            except Exception as e:
                print(f"❌ Error: {e}")
                self.logger.error(f"Menu error: {e}")
                
    def phone_intelligence(self):
        """Comprehensive phone number analysis"""
        print("\n" + "─" * 70)
        print("📞 PHONE NUMBER INTELLIGENCE")
        print("─" * 70)
        
        try:
            import phonenumbers
            from phonenumbers import carrier, geocoder, timezone
            
            phone = input("\n➤ Enter phone number (with country code): ").strip()
            
            if not phone:
                print("❌ No input provided")
                return
                
            # Log the search
            search_hash = hashlib.md5(phone.encode()).hexdigest()[:8]
            self.logger.info(f"Phone search: {search_hash}")
            
            # Format phone
            original = phone
            if phone.startswith('0'):
                phone = '+94' + phone[1:]  # Default Sri Lanka
            elif not phone.startswith('+'):
                phone = '+' + phone
                
            print(f"\n🔍 Analyzing: {phone}")
            print("─" * 40)
            
            # Parse and validate
            parsed = phonenumbers.parse(phone, None)
            
            if not phonenumbers.is_valid_number(parsed):
                print("❌ Invalid phone number")
                return
                
            # Extract information
            info = {
                'original': original,
                'formatted': phone,
                'national': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL),
                'international': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                'country': geocoder.description_for_number(parsed, 'en'),
                'carrier': carrier.name_for_number(parsed, 'en') or 'Unknown',
                'timezone': timezone.time_zones_for_number(parsed),
                'type': self.get_number_type(phonenumbers.number_type(parsed)),
                'valid': True,
                'timestamp': datetime.now().isoformat()
            }
            
            # Display results
            print(f"\n✅ VALID PHONE NUMBER DETECTED")
            print(f"📱 National Format: {info['national']}")
            print(f"🌍 International: {info['international']}")
            print(f"🇺🇳 Country: {info['country']}")
            print(f"📡 Carrier: {info['carrier']}")
            
            if info['timezone']:
                print(f"🕐 Timezone: {info['timezone'][0]}")
                
            print(f"📞 Type: {info['type']}")
            
            # Generate email patterns
            self.generate_phone_patterns(phone)
            
            # Save to report
            save = input("\n💾 Save to report? (y/n): ").lower()
            if save == 'y':
                self.save_phone_report(info)
                
        except ImportError:
            print("❌ Missing module: phonenumbers")
            print("Install with: pip install phonenumbers")
        except Exception as e:
            print(f"❌ Analysis error: {e}")
            self.logger.error(f"Phone analysis error: {e}")
            
    def get_number_type(self, num_type):
        """Convert numeric type to readable format"""
        types = {
            0: "Fixed Line",
            1: "Mobile",
            2: "Fixed Line or Mobile",
            3: "Toll Free",
            4: "Premium Rate",
            5: "Shared Cost",
            6: "VoIP",
            7: "Personal Number",
            8: "Pager",
            9: "UAN",
            10: "Voicemail"
        }
        return types.get(num_type, "Unknown")
        
    def generate_phone_patterns(self, phone):
        """Generate email patterns from phone"""
        clean = phone.replace('+', '').replace(' ', '')
        
        # Remove country code if present
        if clean.startswith('94'):
            clean = clean[2:]  # Sri Lanka
        
        print(f"\n📧 POSSIBLE EMAIL PATTERNS:")
        print(f"  • {clean}@gmail.com")
        print(f"  • {clean}@yahoo.com")
        
        if len(clean) >= 7:
            print(f"  • {clean[:7]}@outlook.com")
            print(f"  • whatsapp{clean[-6:]}@protonmail.com")
            
        print(f"  • contact{clean[-4:]}@email.com")
        
    def save_phone_report(self, info):
        """Save phone analysis report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/phone_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(info, f, indent=2, default=str)
                
            print(f"✅ Report saved: {filename}")
            self.logger.info(f"Phone report saved: {filename}")
            
        except Exception as e:
            print(f"❌ Save error: {e}")
            self.logger.error(f"Report save error: {e}")
            
    def email_analysis(self):
        """Comprehensive email analysis"""
        print("\n" + "─" * 70)
        print("📧 EMAIL ADDRESS ANALYSIS")
        print("─" * 70)
        
        import re
        
        email = input("\n➤ Enter email address: ").strip().lower()
        
        if not email or '@' not in email:
            print("❌ Invalid email format")
            return
            
        # Log the search
        search_hash = hashlib.md5(email.encode()).hexdigest()[:8]
        self.logger.info(f"Email search: {search_hash}")
        
        print(f"\n🔍 Analyzing: {email}")
        print("─" * 40)
        
        # Validate format
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_regex, email):
            print("❌ Invalid email format")
            return
            
        username, domain = email.split('@')
        
        # Check disposable emails
        disposable = self.is_disposable_email(domain)
        
        # Check MX records
        mx_info = self.check_mx_records(domain)
        
        # Generate report
        info = {
            'email': email,
            'username': username,
            'domain': domain,
            'disposable': disposable,
            'mx_records': mx_info,
            'social_profiles': self.generate_social_links(username),
            'timestamp': datetime.now().isoformat()
        }
        
        # Display results
        print(f"\n✅ EMAIL ANALYSIS COMPLETE")
        print(f"📧 Address: {email}")
        print(f"👤 Username: {username}")
        print(f"🌐 Domain: {domain}")
        print(f"📭 Disposable: {'⚠️ Yes' if disposable else '✅ No'}")
        
        if mx_info['has_mx']:
            print(f"📨 MX Records: ✅ Present ({len(mx_info['servers'])} servers)")
            for server in mx_info['servers'][:2]:
                print(f"    • {server}")
        else:
            print(f"📨 MX Records: ❌ None found")
            
        print(f"\n🌐 SOCIAL MEDIA CHECK:")
        for platform, url in info['social_profiles'].items():
            print(f"  • {platform}: {url}")
            
        # Save option
        save = input("\n💾 Save to report? (y/n): ").lower()
        if save == 'y':
            self.save_email_report(info)
            
    def is_disposable_email(self, domain):
        """Check if email domain is disposable"""
        disposable_domains = [
            'tempmail', '10minutemail', 'guerrillamail',
            'mailinator', 'yopmail', 'trashmail',
            'maildrop', 'fakeinbox', 'tempr'
        ]
        
        return any(d in domain.lower() for d in disposable_domains)
        
    def check_mx_records(self, domain):
        """Check domain MX records"""
        try:
            import dns.resolver
            
            mx_info = {
                'has_mx': False,
                'servers': []
            }
            
            answers = dns.resolver.resolve(domain, 'MX')
            mx_info['has_mx'] = True
            mx_info['servers'] = [str(r.exchange) for r in answers]
            
            return mx_info
            
        except:
            return {'has_mx': False, 'servers': []}
            
    def generate_social_links(self, username):
        """Generate social media profile links"""
        return {
            'Twitter': f"https://twitter.com/{username}",
            'Instagram': f"https://instagram.com/{username}",
            'GitHub': f"https://github.com/{username}",
            'Reddit': f"https://reddit.com/user/{username}",
            'LinkedIn': f"https://linkedin.com/in/{username}"
        }
        
    def save_email_report(self, info):
        """Save email analysis report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/email_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(info, f, indent=2, default=str)
                
            print(f"✅ Report saved: {filename}")
            self.logger.info(f"Email report saved: {filename}")
            
        except Exception as e:
            print(f"❌ Save error: {e}")
            
    def username_investigation(self):
        """Username enumeration across platforms"""
        print("\n" + "─" * 70)
        print("👤 USERNAME INVESTIGATION")
        print("─" * 70)
        
        username = input("\n➤ Enter username to investigate: ").strip()
        
        if not username:
            print("❌ No username provided")
            return
            
        # Log the search
        search_hash = hashlib.md5(username.encode()).hexdigest()[:8]
        self.logger.info(f"Username search: {search_hash}")
        
        print(f"\n🔍 Checking username: @{username}")
        print("─" * 40)
        
        # Platform list for checking
        platforms = {
            'Twitter': f"https://twitter.com/{username}",
            'Instagram': f"https://instagram.com/{username}",
            'GitHub': f"https://github.com/{username}",
            'Reddit': f"https://reddit.com/user/{username}",
            'Pinterest': f"https://pinterest.com/{username}",
            'TikTok': f"https://tiktok.com/@{username}",
            'Twitch': f"https://twitch.tv/{username}",
            'YouTube': f"https://youtube.com/@{username}",
            'Steam': f"https://steamcommunity.com/id/{username}",
            'Spotify': f"https://open.spotify.com/user/{username}"
        }
        
        print("\n🌐 PLATFORM LINKS:")
        for platform, url in platforms.items():
            print(f"  • {platform:12} → {url}")
            
        print(f"\n💡 TIPS:")
        print("  • Use browser to manually check each link")
        print("  • Look for profile pictures and activity")
        print("  • Check for connected accounts")
        
        # Save results
        save = input("\n💾 Save platform list? (y/n): ").lower()
        if save == 'y':
            self.save_username_report(username, platforms)
            
    def save_username_report(self, username, platforms):
        """Save username investigation report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/username_{username}_{timestamp}.json"
        
        report = {
            'username': username,
            'platforms': platforms,
            'check_date': datetime.now().isoformat(),
            'note': 'Manual verification required'
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2, default=str)
                
            print(f"✅ Report saved: {filename}")
            self.logger.info(f"Username report saved: {filename}")
            
        except Exception as e:
            print(f"❌ Save error: {e}")
            
    def domain_recon(self):
        """Domain and website reconnaissance"""
        print("\n" + "─" * 70)
        print("🌐 DOMAIN RECONNAISSANCE")
        print("─" * 70)
        
        print("\n⚠️  Feature Under Development")
        print("Domain reconnaissance requires additional modules.")
        print("\nTo enable, install:")
        print("  pip install whois python-whois beautifulsoup4")
        
        domain = input("\n➤ Enter domain (e.g., example.com): ").strip()
        
        if not domain:
            print("❌ No domain provided")
            return
            
        print(f"\n🔍 Basic information for: {domain}")
        print("─" * 40)
        
        # Basic DNS check
        try:
            import dns.resolver
            
            print("\n🔗 DNS INFORMATION:")
            
            # Check A record
            try:
                answers = dns.resolver.resolve(domain, 'A')
                print(f"  • A Records: {', '.join([str(r) for r in answers])}")
            except:
                print(f"  • A Records: Not found")
                
            # Check MX records
            mx_info = self.check_mx_records(domain)
            if mx_info['has_mx']:
                print(f"  • MX Records: Found ({len(mx_info['servers'])})")
            else:
                print(f"  • MX Records: Not found")
                
        except ImportError:
            print("❌ DNS module not available")
            
        print(f"\n🔗 URL FORMATS:")
        print(f"  • http://{domain}")
        print(f"  • https://{domain}")
        print(f"  • http://www.{domain}")
        print(f"  • https://www.{domain}")
        
    def social_media_lookup(self):
        """Social media intelligence gathering"""
        print("\n" + "─" * 70)
        print("📱 SOCIAL MEDIA INTELLIGENCE")
        print("─" * 70)
        
        print("\n⚠️  Manual Investigation Required")
        print("This tool provides search links. Manual verification is needed.")
        
        target = input("\n➤ Enter name, username, or email: ").strip()
        
        if not target:
            print("❌ No input provided")
            return
            
        print(f"\n🔍 Searching for: {target}")
        print("─" * 40)
        
        # Social media search links
        searches = {
            'Google': f"https://www.google.com/search?q={target}",
            'Facebook': f"https://www.facebook.com/search/top/?q={target}",
            'LinkedIn': f"https://www.linkedin.com/search/results/all/?keywords={target}",
            'Twitter': f"https://twitter.com/search?q={target}",
            'Instagram': f"https://www.instagram.com/web/search/topsearch/?query={target}",
            'GitHub': f"https://github.com/search?q={target}&type=users",
            'Reddit': f"https://www.reddit.com/search/?q={target}",
            'YouTube': f"https://www.youtube.com/results?search_query={target}",
            'TikTok': f"https://www.tiktok.com/search?q={target}"
        }
        
        print("\n🔗 SEARCH LINKS:")
        for platform, url in searches.items():
            print(f"  • {platform:10} → {url}")
            
        print(f"\n💡 INVESTIGATION TIPS:")
        print("  1. Check profile pictures")
        print("  2. Look for connected accounts")
        print("  3. Verify account creation dates")
        print("  4. Check activity patterns")
        
    def generate_report(self):
        """Generate comprehensive report"""
        print("\n" + "─" * 70)
        print("📄 REPORT GENERATION")
        print("─" * 70)
        
        print("\nAvailable reports in 'reports/' directory:")
        
        try:
            import glob
            
            reports = glob.glob('reports/*.json')
            
            if not reports:
                print("  No reports found")
                return
                
            for i, report in enumerate(reports, 1):
                filename = os.path.basename(report)
                size = os.path.getsize(report)
                print(f"  {i:2}. {filename} ({size} bytes)")
                
            print(f"\n📁 Total reports: {len(reports)}")
            
        except Exception as e:
            print(f"❌ Error listing reports: {e}")
            
    def settings_menu(self):
        """Settings and configuration"""
        print("\n" + "─" * 70)
        print("⚙️  SETTINGS & CONFIGURATION")
        print("─" * 70)
        
        print("\n1. 📊 View System Information")
        print("2. 🧹 Clear Cache & Temporary Files")
        print("3. 📁 Open Reports Directory")
        print("4. 📜 View Activity Logs")
        print("5. 🔙 Back to Main Menu")
        
        choice = input("\n➤ Select option: ").strip()
        
        if choice == '1':
            self.system_info()
        elif choice == '2':
            self.clear_cache()
        elif choice == '3':
            self.open_reports_dir()
        elif choice == '4':
            self.view_logs()
            
    def system_info(self):
        """Display system information"""
        import platform
        
        print("\n" + "─" * 40)
        print("📊 SYSTEM INFORMATION")
        print("─" * 40)
        
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Python: {platform.python_version()}")
        print(f"Processor: {platform.processor()}")
        print(f"Directory: {os.getcwd()}")
        print(f"Reports: {len(os.listdir('reports')) if os.path.exists('reports') else 0}")
        
    def clear_cache(self):
        """Clear cache and temporary files"""
        confirm = input("\n⚠️  Clear all cache files? (y/n): ").lower()
        
        if confirm == 'y':
            try:
                import shutil
                
                if os.path.exists('cache'):
                    shutil.rmtree('cache')
                    os.makedirs('cache')
                    print("✅ Cache cleared")
                    
                if os.path.exists('tmp'):
                    shutil.rmtree('tmp')
                    os.makedirs('tmp')
                    print("✅ Temporary files cleared")
                    
            except Exception as e:
                print(f"❌ Error: {e}")
                
    def open_reports_dir(self):
        """Open reports directory"""
        reports_dir = os.path.join(os.getcwd(), 'reports')
        
        if os.path.exists(reports_dir):
            print(f"\n📁 Reports directory: {reports_dir}")
            print("\nFiles:")
            
            files = os.listdir(reports_dir)
            for file in files:
                print(f"  • {file}")
        else:
            print("❌ Reports directory not found")
            
    def view_logs(self):
        """View activity logs"""
        log_dir = os.path.join(os.getcwd(), 'logs')
        
        if os.path.exists(log_dir):
            print(f"\n📜 Logs directory: {log_dir}")
            print("\nAvailable logs:")
            
            logs = os.listdir(log_dir)
            for log in logs:
                print(f"  • {log}")
                
            view = input("\nView specific log? (filename or 'no'): ").strip()
            
            if view != 'no' and view in logs:
                with open(os.path.join(log_dir, view), 'r') as f:
                    print(f"\n{'-'*40}")
                    print(f.read()[:1000])  # First 1000 chars
                    print(f"{'-'*40}")
        else:
            print("❌ Logs directory not found")
            
    def show_documentation(self):
        """Show documentation"""
        print("\n" + "═" * 70)
        print("📖 DOCUMENTATION")
        print("═" * 70)
        
        docs = """
        OSINT COLLECTOR - USER GUIDE
        
        1. PHONE ANALYSIS
           • Enter phone with country code (+94 for Sri Lanka)
           • Get carrier, location, and timezone
           • Generate associated email patterns
        
        2. EMAIL ANALYSIS
           • Validate email format and domain
           • Check for disposable emails
           • Verify MX records for deliverability
           • Generate social media search links
        
        3. USERNAME INVESTIGATION
           • Check username across 10+ platforms
           • Get direct profile links
           • Manual verification required
        
        4. DOMAIN RECON
           • Basic DNS information
           • URL format generation
           • Requires additional modules for full features
        
        5. SOCIAL MEDIA
           • Generate search links across platforms
           • Manual investigation required
           • Ethical use mandatory
        
        SECURITY FEATURES:
        • All searches are logged
        • Reports are saved with timestamps
        • No automatic data collection
        • Manual verification required
        
        LEGAL REQUIREMENTS:
        • Only research yourself or with permission
        • No harassment, stalking, or doxxing
        • Comply with all applicable laws
        • Delete data after legitimate use
        
        Directory Structure:
        • /reports/ - Saved analysis reports
        • /logs/    - Activity and search logs
        • /cache/   - Temporary data
        • /exports/ - Export files
        
        Version: 2.0 | Educational Use Only
        """
        
        print(docs)
        input("\nPress Enter to continue...")
        
    def exit_program(self):
        """Exit the program gracefully"""
        print("\n" + "═" * 70)
        print("👋 THANK YOU FOR USING OSINT COLLECTOR")
        print("═" * 70)
        print("\nRemember:")
        print("• Use this tool ethically and legally")
        print("• Respect privacy and data protection laws")
        print("• Delete sensitive data after use")
        print("• Report any issues or concerns")
        
        self.logger.info("Program exited normally")
        sys.exit(0)

def main():
    """Main entry point"""
    try:
        # Create collector instance
        collector = OSINTCollector()
        
        # Display banner
        collector.display_banner()
        
        # Check dependencies
        if not collector.check_dependencies():
            print("\n❌ Please install missing dependencies first")
            return
            
        # Get legal consent
        if not collector.get_legal_consent():
            return
            
        # Enter main menu
        collector.main_menu()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        logging.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

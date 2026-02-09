#!/usr/bin/env python3
"""
🔎 Quick OSINT Search Tool
Fast searches for emails, usernames, and phone info
"""

import re
import json
from datetime import datetime

def quick_email_search(email):
    """Quick email analysis"""
    print(f"\n📧 Quick Email Analysis: {email}")
    print("-"*40)
    
    # Extract username and domain
    if '@' in email:
        username, domain = email.split('@')
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        
        # Common patterns
        print(f"\n💡 Possible variations:")
        print(f"  • {username}123@{domain}")
        print(f"  • {username}.official@{domain}")
        print(f"  • contact.{username}@{domain}")
        
        # Social media
        print(f"\n🌐 Social media check:")
        print(f"  Twitter: https://twitter.com/{username}")
        print(f"  Instagram: https://instagram.com/{username}")
        print(f"  GitHub: https://github.com/{username}")
    
    return {
        'email': email,
        'username': username if '@' in email else None,
        'domain': domain if '@' in email else None,
        'searched_at': datetime.now().isoformat()
    }

def quick_phone_search(phone):
    """Quick phone analysis"""
    print(f"\n📞 Quick Phone Analysis: {phone}")
    print("-"*40)
    
    # Clean phone
    clean = re.sub(r'[^0-9+]', '', phone)
    
    # Sri Lankan prefixes
    prefixes = {
        '70': 'Mobitel - Colombo',
        '71': 'Mobitel - Western',
        '72': 'Dialog - Colombo',
        '74': 'Dialog - Suburbs',
        '75': 'Airtel - Urban',
        '77': 'Dialog/Hutch - Urban',
        '78': 'Hutch - Major Cities',
        '81': 'Mobitel - Kandy'
    }
    
    if clean.startswith('+94'):
        prefix = clean[3:5]
        info = prefixes.get(prefix, 'Unknown operator')
        print(f"Prefix: {prefix}")
        print(f"Info: {info}")
    
    # Email patterns from phone
    clean_num = clean.replace('+', '')
    if clean_num.startswith('94'):
        clean_num = clean_num[2:]
    
    print(f"\n📧 Possible email patterns:")
    print(f"  • {clean_num}@gmail.com")
    print(f"  • whatsapp.{clean_num}@yahoo.com")
    if len(clean_num) >= 7:
        print(f"  • {clean_num[:7]}@outlook.com")
    
    return {
        'phone': phone,
        'clean': clean,
        'prefix': prefix if clean.startswith('+94') and len(clean) > 4 else None,
        'searched_at': datetime.now().isoformat()
    }

def main():
    print("\n🔎 QUICK OSINT SEARCH TOOL")
    print("="*50)
    
    while True:
        print("\nWhat to search?")
        print("1. Email address")
        print("2. Phone number")
        print("3. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            email = input("Enter email: ").strip()
            if '@' in email:
                result = quick_email_search(email)
                
                save = input("\nSave result? (y/n): ").lower()
                if save == 'y':
                    filename = f"search_email_{email.replace('@', '_')}_{datetime.now().strftime('%H%M%S')}.json"
                    with open(filename, 'w') as f:
                        json.dump(result, f, indent=2)
                    print(f"✅ Saved to {filename}")
        
        elif choice == '2':
            phone = input("Enter phone: ").strip()
            if phone:
                result = quick_phone_search(phone)
                
                save = input("\nSave result? (y/n): ").lower()
                if save == 'y':
                    filename = f"search_phone_{phone.replace('+', '')}_{datetime.now().strftime('%H%M%S')}.json"
                    with open(filename, 'w') as f:
                        json.dump(result, f, indent=2)
                    print(f"✅ Saved to {filename}")
        
        elif choice == '3':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()

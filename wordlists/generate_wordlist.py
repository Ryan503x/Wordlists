import itertools
import argparse

def generate_wordlist():
    """Generate wordlist using hardcoded patterns"""
    
    # HARDCODED PATTERNS - EDIT THESE AS NEEDED
    LETTER_PAIRS = [
        'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm',
        'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz'
    ]
    
    NUMBER_COMBINATIONS = [
        "11111", "123123", "321321", "112233", "11223344", "1122334455", 
        "112233445566", "12345", "123456", "1234567", "12345678", "123456789",
        "135531", "13579", "221133", "22222", "223311", "24680", "332211",
        "332211332211", "33333", "44444", "54321", "55555", "654321", 
        "667788", "987654321"
    ]
    
    SYMBOLS = ["!", "#", "@"]
    
    MASKS = [
        "?l?n",         # Aa12345
        "?l?s?n",       # Aa!12345
        "?l?s?s?n",     # Aa!!12345
        "?l?n?s",       # Aa12345!
        "?l?n?s?s",     # Aa12345!!
    ]
    
    all_passwords = []
    
    for letter_pair in LETTER_PAIRS:
        for number_combo in NUMBER_COMBINATIONS:
            for mask in MASKS:
                password = mask
                
                # Replace mask placeholders with actual values
                password = password.replace("?l", letter_pair)
                password = password.replace("?n", number_combo)
                
                # Handle symbols - generate all combinations for symbol placeholders
                symbol_count = password.count("?s")
                if symbol_count > 0:
                    # Generate all possible symbol combinations for this mask
                    for symbol_combo in itertools.product(SYMBOLS, repeat=symbol_count):
                        temp_password = password
                        for symbol in symbol_combo:
                            temp_password = temp_password.replace("?s", symbol, 1)
                        all_passwords.append(temp_password)
                else:
                    all_passwords.append(password)
    
    # Remove duplicates and sort
    unique_passwords = sorted(list(set(all_passwords)))
    return unique_passwords

def save_wordlist(wordlist, filename="wordlist_output.txt"):
    """Save wordlist to file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for password in wordlist:
                f.write(password + '\n')
        
        print(f"[+] saved to {filename} successfully with {len(wordlist)} combination word")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Generate custom wordlist from hardcoded patterns')
    parser.add_argument('-o', '--output', default='wordlist_output.txt', 
                       help='Output filename (default: wordlist_output.txt)')
    
    args = parser.parse_args()
    
    wordlist = generate_wordlist()
    
    # Save to file
    save_wordlist(wordlist, args.output)

if __name__ == "__main__":
    main()

import csv
import argparse
import os

def generate_wordlist():
    # =========================================================================
    #   CONFIGURATION SECTION - Edit these lists as needed
    # =========================================================================
    
    # 1. Prefixes (Letters/Names)
    prefixes = [
        'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 
        'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 
        'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz',
        'Admin'
    ]
    
    # 2. Number Sequences
    number_sequences = [
        "11111", "123123", "321321", "112233", "11223344", "1122334455", 
        "112233445566", "12345", "123456", "1234567", "12345678", "123456789",
        "135531", "13579", "221133", "22222", "223311", "24680", "332211",
        "332211332211", "33333", "44444", "54321", "55555", "654321", 
        "667788", "987654321", "102030"
    ]
    
    # 3. Single Symbols
    symbols = ['!', '@', '#']
    
    # 4. Symbol Pairs (2 Symbols)
    symbol_pairs = [
        '!!', '@@', '##', 
        '@#', '#@'        
    ]
    
    wordlist = set() 
    
    # Generate all combinations for each pattern
    for prefix in prefixes:
        for numbers in number_sequences:
            
            # Pattern 1: ?L?N (e.g., Aa12345)
            wordlist.add(prefix + numbers)
            
            # Pattern 2: ?L?S?N (e.g., Aa!12345)
            for symbol in symbols:
                wordlist.add(prefix + symbol + numbers)
            
            # Pattern 3: ?L?S?S?N (e.g., Aa!!12345 or Aa@#12345)
            for pair in symbol_pairs:
                wordlist.add(prefix + pair + numbers)
            
            # Pattern 4: ?L?N?S (e.g., Aa12345!)
            for symbol in symbols:
                wordlist.add(prefix + numbers + symbol)
            
            # Pattern 5: ?L?N?S?S (e.g., Aa12345!! or Aa12345@#)
            for pair in symbol_pairs:
                wordlist.add(prefix + numbers + pair)
    
    return sorted(wordlist)

def save_wordlist(wordlist, filename):
    """
    Saves the wordlist to a file. 
    Detects extension to decide between CSV or TXT format.
    """
    _, ext = os.path.splitext(filename)
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            # If extension is .csv, use csv writer. Otherwise (e.g. .txt), write plain lines.
            if ext.lower() == '.csv':
                writer = csv.writer(f)
                for word in wordlist:
                    writer.writerow([word]) 
                print(f"Mode: CSV (Comma Separated)")
            else:
                for word in wordlist:
                    f.write(word + '\n')
                print(f"Mode: Plain Text (Newline Separated)")
                
        print(f"Successfully saved to '{filename}'")
        print(f"Total entries: {len(wordlist)}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    # Initialize Argument Parser
    parser = argparse.ArgumentParser(description="Generate a custom wordlist.")
    
    # Add -o argument for output filename
    parser.add_argument('-o', '--output', type=str, required=True, 
                        help='Output filename (e.g., wordlist.csv or wordlist.txt)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # 1. Generate the list
    print("Generating wordlist...")
    wordlist = generate_wordlist()
    
    # 2. Save to the file specified in -o argument
    save_wordlist(wordlist, args.output)
    
    # 3. Show sample entries
    print("\nSample entries (first 10):")
    for i, word in enumerate(wordlist[:10]):
        print(f"{i+1}: {word}")

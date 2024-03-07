import re
import json
import sys

# Token types
KEYWORD = 'KEYWORD'
IDENTIFIER = 'IDENTIFIER'
OPERATOR = 'OPERATOR'
CONSTANT = 'CONSTANT'
SPECIAL_CHAR = 'SPECIAL_CHAR'
COMMENT = 'COMMENT'

# Error types
SYNTAX_ERROR = 'SYNTAX_ERROR'
RUNTIME_ERROR = 'RUNTIME_ERROR'

# Regular expressions for token matching
token_patterns = [
    (r'[:|,;]', SPECIAL_CHAR),
    (r'[-+*/%]|<<|>>|&|\||\^|==|!=|<=|>=|<|>', OPERATOR),
    (r'[A-Za-z_]\w*', IDENTIFIER),
    (r'[0-9]+', CONSTANT),
    (r'//.*', COMMENT),  # Match single-line comments starting with //
]

# SCL Keywords
SCL_KEYWORDS = ['IMPORT', 'USE', 'symbols', 'forward_refs', 'specifications', 'globals', 'implementations', 'FORWARD']

# SCL Grammar Rules
SCL_GRAMMAR = {
    'start': ['imports', 'symbols', 'forward_refs', 'specifications', 'globals', 'implementations'],
    'imports': ['import_file'],
    'import_file': ['IMPORT header_file_name', 'USE header_file_name'],
    'header_file_name': ['LANGB fname RANGB', 'QUOTES fname QUOTES'],
    'fname': ['IDENTIFIER', 'fname shlash IDENTIFIER'],
    'shlash': ['FSHASH', 'BSLASH'],
    # Add more grammar rules as needed
}

def scan_source_code(source_code):
    tokens = []
    lines = source_code.split('\n')
    
    for line_num, line in enumerate(lines, start=1):
        for token_pattern in token_patterns:
            pattern, token_type = token_pattern
            for match in re.finditer(pattern, line):
                value = match.group(0)
                if token_type != COMMENT:
                    tokens.append({'type': token_type, 'value': value, 'line': line_num})
                
    return tokens

def detect_syntax_errors(tokens):
    stack = ['start']
    expected_tokens = {rule: SCL_GRAMMAR[rule] for rule in SCL_GRAMMAR}

    for token in tokens:
        if token['type'] == 'COMMENT':
            continue
        while stack:
            current_rule = stack[-1]
            if token['value'] in expected_tokens[current_rule]:
                break
            else:
                print(f"Syntax Error: Unexpected token {token['value']} at line {token['line']}")
                if current_rule == 'start':
                    break
                else:
                    stack.pop()
        else:
            print(f"Syntax Error: Unexpected token {token['value']} at line {token['line']}")
            stack = []
            # Implement more detailed error handling if needed

    if stack and stack[-1] != 'start':
        print(f"Syntax Error: Incomplete syntax at the end of the file")

def detect_runtime_errors(tokens):
    # Example: Check if there are undefined variables
    variables = set()
    for token in tokens:
        if token['type'] == 'IDENTIFIER':
            variables.add(token['value'])
    
    # Check if there are variables used without being declared
    undeclared_variables = variables - set(SCL_KEYWORDS)
    if undeclared_variables:
        print(f"Runtime Error: Undeclared variables found: {', '.join(undeclared_variables)}")

def interpret_scl(tokens):
    # Basic SCL interpreter logic
    for token in tokens:
        if token['type'] == 'IDENTIFIER' and token['value'] == 'main':
            print("Interpreting main function...")
            # Add more interpretation logic for the 'main' function

def main():
    if len(sys.argv) != 2:
        print("Usage: python scl_scanner.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            source_code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    tokens = scan_source_code(source_code)

    if not tokens:
        print("No tokens found. Check your input file or the implemented token patterns.")
        sys.exit(1)

    # Detect and print syntax errors
    detect_syntax_errors(tokens)

    # Detect and print runtime errors
    detect_runtime_errors(tokens)

    # Interpret the SCL code
    interpret_scl(tokens)

    # Display tokens on the console
    print("\nTokens:")
    for token in tokens:
        print(token)

    # Write tokens to a JSON file
    output_file = 'tokens.json'
    with open(output_file, 'w') as json_file:
        json.dump(tokens, json_file, indent=2)

    print(f"\nTokens written to {output_file}")

if __name__ == "__main__":
    main()

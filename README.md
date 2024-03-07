# SCL Scanner and Interpreter

## Overview

This repository contains a simple Scanner and Interpreter for a subset of Symbolic C Language (SCL). The goal is to demonstrate a basic implementation of lexical analysis, syntax checking, and minimal interpretation.

## Contents

- `scl_scanner.py`: Python script for scanning SCL source code and generating tokens.
- `input.scl`:  SCL source code file.
- `tokens.json`: Output file containing scanned tokens.

## Usage

1. Ensure you have Python installed.
2. Run the scanner: `python scl_scanner.py input.scl`
3. View the scanned tokens on the console.
4. Check `tokens.json` for the token output in JSON format.

## Example SCL Code (input.scl)

```scl
IMPORT library scl:
symbols SYMBOL variable1 1
SYMBOL variable2 2
:

forward_refs FORWARD func_main PARAMETERS ALTERS INTEGER:
specifications
ENUM
STRUCT
DESCRIPTION:
globals
GLOBAL DECLARATIONS
CONSTANTS
DEFINE constants_file1 1
IDENTIFIER const_var1 1;
POINTER OF ARRAY OF TUNSIGNED 5;
VARIABLES
DEFINE variables_file1 1
IDENTIFIER var1 1;
POINTER OF INTEGER:
implementations
MAIN
DESCRIPTION:
PARAMETERS;
ALTERS variables_file1 1;
FUNCTION func_main PERSISTENT IS
DECLARE
CONSTANTS
DEFINE constants_file2 2
IDENTIFIER const_var2 2;
POINTER OF ARRAY OF TUNSIGNED 10;
VARIABLES
DEFINE variables_file2 2
IDENTIFIER var2 2;
POINTER OF INTEGER:
BEGIN;
ADD var1 TO var2 1 2;
SUBTRACT const_var2 FROM const_var1 2 1;
ENDFUN func_main
POSTCONDITION;
expr RELOP expr;
ENDMAIN

## Result

After running the scanner, you will see the scanned tokens and a tokens.json file containing the token details.

Feel free to explore and experiment with different SCL code examples!

## Contributions
Contributions are welcome. If you find any issues or improvements, please open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

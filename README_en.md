# Addison → Sage Converter (POC)
[🇩🇪 Deutsche Version](README.md)

⚠️ **Disclaimer**  
This is a **Proof of Concept** implementation based on the Sage import specification.  
The tool has **not been tested in a real production environment** with Sage.  
Use at your own risk.

## Overview
This repository contains a small Python tool that converts Addison payroll export files  
into a Sage-compatible import format. It was developed to replace an Excel/VBA macro workflow  
that required manual folder setup, file renaming, and path adjustments.

## Features
- Input: Addison export file (`.txt`, 11 columns, semicolon-separated)
- Output: Sage-compatible text file (`.txt`)
- Automatically extracts month and year
- Rearranges columns to match Sage import format
- GUI-based file selection (Tkinter) – no manual path editing
- Can be compiled into a portable `.exe` using PyInstaller

## Motivation
The original Excel/VBA macro was error-prone and unprofessional for B2B use:
- Hardcoded file paths in the code
- Manual renaming of input files
- Strict folder structures required
- Dependence on Excel and VBA knowledge

This Python version simplifies the process by providing:
- A standalone tool
- Flexible input/output paths
- Cleaner and more robust transformation logic

## Field Mapping (Addison → Sage)

The tool transforms an Addison export file with 11 columns into a Sage-compatible import file with 10 columns.  
Main transformation: the date column is split into **Month** and **Year**.

⚠️ Note: Addison’s official field specification was not available.  
The mapping below is based on observed test data and may not be complete.

| Addison column (Input)        | Meaning (observed/assumed) | Sage column (Output)    | Transformation / Comment                    |
|-------------------------------|----------------------------|-------------------------|---------------------------------------------|
| [0]                           | Company number             | [0]                     | 1:1 copied                                  |
| [1]                           | Personnel number           | [3]                     | 1:1 copied (shifted)                        |
| [2]                           | Wage type                  | [4]                     | 1:1 copied                                  |
| [3]                           | Unknown (possibly absence) | [5]                     | 1:1 copied (kept for structure)             |
| [4]                           | Unknown (possibly absence) | [6]                     | 1:1 copied (kept for structure)             |
| [5]                           | Unknown / unused           | –                       | dropped                                     |
| [6]                           | Encoded date (MMYYYY)      | [1] = Month, [2] = Year | split into separate fields                  |
| [7]                           | Amount (€)                 | [7]                     | 1:1 copied                                  |
| [8]                           | Percentage value           | [8]                     | 1:1 copied                                  |
| [9]                           | Unknown / reserved         | [9]                     | 1:1 copied (kept for structure)             |
| [10]                          | Surcharge hours            | [10]                    | 1:1 copied                                  |


## Status
- Proof of Concept (POC)
- Tested with dummy Addison export data only
- Not intended for production use

## Technologies
- Python
- Pandas
- Tkinter

## Usage
1. Run the tool (`python src/addison_to_sage.py` or compiled `.exe`).
2. Select the Addison export file via the GUI.
3. Choose an output path.
4. The converted Sage-compatible file will be saved automatically.

## Example Data
For demonstration purposes, an example file is included under `examples/dummy_addison_export.txt`.  
It contains fake data in the Addison export structure (11 columns, semicolon-separated).

## License
This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

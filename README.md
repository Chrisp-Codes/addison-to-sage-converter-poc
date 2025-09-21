# Addison → Sage Converter (POC)

⚠️ **Disclaimer**  
This is a **Proof of Concept** implementation based on the Sage import specification.  
The tool has **not been tested in a real production environment** with Sage.  
Use at your own risk.

## Overview
This repository contains a small Python tool to convert Addison payroll export files
into a Sage-compatible import format. It replaces an earlier Excel/VBA macro workflow.

## Features
- Input: Addison export file (`.txt`, 11 columns, semicolon-separated)
- Output: Sage-compatible text file
- Extracts month & year automatically
- Rearranges columns to Sage import order
- GUI for file selection (tkinter)
- Portable `.exe` possible (via PyInstaller)

## Status
- Proof of Concept (POC)
- Tested with dummy data only
- Not intended for production use

## Technologies
- Python
- Pandas
- Tkinter

## Example Data
A sample file (`examples/dummy_addison_export.txt`) is provided for testing.

## License
This project is licensed under the MIT License – see [LICENSE](LICENSE).

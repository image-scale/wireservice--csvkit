# Goal

## Project
csvkit — a python project.

## Description
A suite of command-line tools for converting to and working with CSV files. csvkit provides 14 CLI commands that can filter, search, sort, join, convert, query, and analyze tabular data from the terminal. Built on top of the agate library for CSV/data processing.

Core tools:
- csvcut: Filter and truncate CSV columns (like Unix cut for tabular data)
- csvformat: Convert CSV to custom output format (delimiters, quoting, etc.)
- csvgrep: Search CSV files by string, regex, or file match (like Unix grep for tabular data)
- csvclean: Report and fix common CSV errors (length mismatches, empty columns)
- csvstack: Stack rows from multiple CSV files vertically with optional grouping
- csvsort: Sort CSV files by columns (like Unix sort for tabular data)
- csvlook: Render CSV as a Markdown-compatible fixed-width table
- csvjson: Convert CSV to JSON or GeoJSON
- csvjoin: SQL-like join of multiple CSV files on specified columns
- csvstat: Print descriptive statistics for each column
- in2csv: Convert other formats (XLS, XLSX, JSON, GeoJSON, DBF, fixed-width) to CSV
- csvsql: Generate SQL statements for CSV files or execute them on a database
- sql2csv: Execute SQL queries against a database and output results as CSV
- csvpy: Load CSV into a Python interactive shell

## Scope
- ~20 production source files to implement
- ~20 test files to write
- Reproduce all core source code, tests, and configuration

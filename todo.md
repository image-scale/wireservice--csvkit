# Todo

## Plan
Build the CLI framework first as part of the csvcut feature (the simplest and most fundamental tool). Then implement each additional tool one at a time, adding infrastructure (exceptions, helpers, converters) alongside the features that need them. Format converters (in2csv) and database tools (csvsql, sql2csv) come last since they have the most external dependencies.

## Tasks
- [ ] Task 1: Implement csvcut — a CLI tool that filters and truncates CSV columns. Supports selecting columns by name/index, excluding columns, deleting empty rows, listing column names, line numbers, and reading from files (including gzip/bzip2) or stdin. This also establishes the shared CLI framework (argument parsing, common flags, file handling) and shared test infrastructure.
- [ ] Task 2: Implement csvformat — a CLI tool that converts CSV to a custom output format. Supports custom delimiters, tab output, ASCII separator output, custom quote chars, quoting styles, escape chars, and line terminators for the output.
- [ ] Task 3: Implement csvgrep — a CLI tool that searches CSV files by string match, regex, or file-based matching. Supports inverse matching, any-column matching, and column selection.
- [ ] Task 4: Implement csvclean — a CLI tool that reports and fixes common CSV errors. Supports length mismatch detection, empty column detection, header normalization, joining short rows, and filling short rows.
- [ ] Task 5: Implement csvstack — a CLI tool that stacks rows from multiple CSV files vertically. Supports grouping values (explicit or filename-based), group naming, and no-header-row mode.
- [ ] Task 6: Implement csvsort — a CLI tool that sorts CSV files by one or more columns. Supports reverse sorting, case-insensitive sorting, and no-inference mode.
- [ ] Task 7: Implement csvlook — a CLI tool that renders CSV as a Markdown-compatible fixed-width table. Supports max rows, max columns, max column width, max precision, and no-inference mode.
- [ ] Task 8: Implement csvjson — a CLI tool that converts CSV to JSON or GeoJSON. Supports keyed output, NDJSON streaming, GeoJSON with lat/lon/type/geometry/crs/bbox options.
- [ ] Task 9: Implement csvjoin — a CLI tool that performs SQL-like joins on CSV files. Supports inner, left, right, full outer, and sequential joins on specified columns.
- [ ] Task 10: Implement csvstat — a CLI tool that prints descriptive statistics for each column. Supports type, nulls, unique, min, max, sum, mean, median, stdev, length, precision, and frequency statistics, with CSV and JSON output modes.
- [ ] Task 11: Implement in2csv — a CLI tool that converts other formats (XLS, XLSX, JSON, GeoJSON, NDJSON, DBF, fixed-width) to CSV. Supports sheet names, schema files for fixed-width, and format detection.
- [ ] Task 12: Implement csvsql and sql2csv — CLI tools for database interaction. csvsql generates SQL CREATE TABLE statements or executes them on a database with insert/query support. sql2csv executes SQL queries against a database and outputs CSV results.

import re


def parse_log(log: str) -> dict[str, str]:
    """Parse test runner output into per-test results.

    Args:
        log: Full stdout+stderr output of `bash run_test.sh 2>&1`.

    Returns:
        Dict mapping test_id to status string ("PASSED", "FAILED", "SKIPPED", "ERROR").
    """
    results = {}

    # Strip ANSI escape codes
    log = re.sub(r'\x1b\[[0-9;]*m', '', log)

    # Match inline pytest output lines:
    # "tests/foo.py::TestClass::test_method PASSED     [ 50%]"
    # "tests/foo.py::TestClass::test_method SKIPPED (...) [ 50%]"
    # Also handles multi-line output where test name appears twice
    inline_pattern = re.compile(
        r'^(tests/\S+::\S+(?:\[.*?\])?)\s+(PASSED|FAILED|SKIPPED|ERROR)[^\n]*\[',
        re.MULTILINE
    )
    for m in inline_pattern.finditer(log):
        test_id = m.group(1)
        status = m.group(2)
        results.setdefault(test_id, status)

    # Match summary section lines:
    # "FAILED tests/foo.py::TestClass::test_method - AssertionError: ..."
    summary_pattern = re.compile(
        r'^(PASSED|FAILED|SKIPPED|ERROR)\s+(tests/\S+::\S+)',
        re.MULTILINE
    )
    for m in summary_pattern.finditer(log):
        status = m.group(1)
        test_id = m.group(2)
        # Summary results take precedence for FAILED/ERROR (final authoritative status)
        if status in ('FAILED', 'ERROR'):
            results[test_id] = status
        else:
            results.setdefault(test_id, status)

    # Handle collection errors: "ERROR tests/foo.py" (no "::")
    collection_error_pattern = re.compile(
        r'^ERROR\s+(tests/[^\s:]+\.py)\s*$',
        re.MULTILINE
    )
    for m in collection_error_pattern.finditer(log):
        test_id = m.group(1)
        results.setdefault(test_id, 'ERROR')

    return results


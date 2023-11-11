import pytest
from txt2html import process_line


@pytest.mark.parametrize(
    "input_line, expected_output",
    [
        ("This is a normal line.", "This is a normal line."),
        ("This should be *italic*.", "This should be <i>italic</i>."),
        ("**This should not be bold.**", "**This should not be bold.**"),
        (
            "*Multiple* *italics* *in* *one* *line.*",
            "<i>Multiple</i> <i>italics</i> <i>in</i> <i>one</i> <i>line.</i>",
        ),
        ("No italics in this line.", "No italics in this line."),
    ],
)
def test_process_line(input_line, expected_output):
    result = process_line(input_line)
    assert result == expected_output

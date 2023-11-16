import pytest
from txt2html import process_line, process_text_file, contains_italics
from unittest.mock import patch


@pytest.mark.parametrize(
    "input_line, expected_output",
    [
        ("This is a normal line.", "This is a normal line."),
        ("This should be *italic.*", "This should be <i>italic.</i>"),
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

    # test the .txt file
    @patch("builtins.print")
    def test_process_text_file(self, mock_print):
        process_text_file(
            "examples/test-folder/test2.txt", "examples/test-folder-output"
        )
        mock_print.assert_called_with(
            "HTML file 'examples/test-folder-output/test2.html' generated successfully."
        )

    # test the .md file
    @patch("builtins.print")
    def test_process_md_file(self, mock_print):
        process_text_file(
            "examples/test-folder/test4.md", "examples/test-folder-output"
        )
        mock_print.assert_called_with(
            "HTML file 'examples/test-folder-output/test4.html' generated successfully."
        )

    # test the non exist file
    @patch("builtins.print")
    def test_process_non_exist_text_file(self, mock_print):
        with self.assertRaises(FileNotFoundError):
            process_text_file(
                "examples/test-folder/invalid.txt", "examples/test-folder-output"
            )

        mock_print.assert_called_once_with(
            "Error: examples/test-folder/invalid.txt not found."
        )

    def test_contains_italics(self):
        result = contains_italics("*italic word*")
        self.assertTrue(result, "expect to detect italic word")

    def test_not_contains_italics(self):
        result = contains_italics("not italic word")
        self.assertFalse(result, "expect not to detect italic word")

    def test_contains_mixed_italics(self):
        result = contains_italics("This is *italic word*")
        self.assertTrue(result, "expect to detect italic word")

    def test_contains_single_letter(self):
        result = contains_italics("a")
        self.assertFalse(result, "expect not to detect italic word")

    def test_contains_empty_string(self):
        result = contains_italics("")
        self.assertFalse(result, "expect not to detect italic word")

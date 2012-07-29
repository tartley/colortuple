from unittest import TestCase

from mock import patch

from ..options import create_parser, VERSION


class Test_Options(TestCase):

    @patch('sys.stderr')
    def assert_get_parser_error(self, args, expected, mock_stderr):
        with self.assertRaises(SystemExit):
            create_parser().parse_args(args)
        self.assertIn(expected, mock_stderr.write.call_args[0][0])


    def test_get_parser_version(self):
        self.assert_get_parser_error(['--version'], VERSION)


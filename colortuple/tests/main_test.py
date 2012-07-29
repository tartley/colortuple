from unittest import TestCase

from mock import call, patch

from ..main import main


class MainTest(TestCase):

    @patch('colortuple.main.sys.argv', [1, 2, 3])
    @patch('colortuple.main.create_parser')
    def test_main(
        self, mock_get_parser
    ):

        main()

        self.assertEqual(mock_get_parser.call_args, call())
        self.assertEqual(
            mock_get_parser.return_value.parse_args.call_args,
            call([2, 3])
        )


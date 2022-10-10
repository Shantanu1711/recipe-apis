from unittest.mock import patch
from psycopg2 import OperationalError as psycopg2error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
class CommandTest(SimpleTestCase):
    """
    test commands
    """
    @patch('core.management.commands.wait_for_db.check')
    def wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready"""

        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def wait_for_db_delay(self, patched_check):
        """test waiting for operational error"""
        patched_check.side_effect = [psycopg2error] * 2 \
            [OperationalError]*3 + [True]

        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
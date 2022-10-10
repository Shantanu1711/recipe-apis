"""
django command to wait for db 
"""
import time 
from psycopg2 import OperationalError as psycopg2error
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    """Djando command to wait for database """

    def handle(self,*args,**options):
        """Endpoint for command"""
        self.stdout.write('waiting for database...')
        db_up = False
        
        while db_up == False :
            try:
                self.check(databases=['default']) 
                db_up = True
            except(psycopg2error,OperationalError):
                self.stdout.write('databse unavailable , waiting 1 second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DATBASE AVAILABLE'))            

        
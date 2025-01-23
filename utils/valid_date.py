from datetime import datetime

def valid_date(issue_date):
    try:
        datetime.strptime(issue_date, '%d-%m-%Y')
        return True
    except ValueError:
        return False
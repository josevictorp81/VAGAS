from datetime import datetime


async def convert_month_str_to_int(month: str) -> int:
    month_posted = datetime.strptime(month, '%b')
    return month_posted.month

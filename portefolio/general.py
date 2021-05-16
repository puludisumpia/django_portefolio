from datetime import datetime

def inject_site_name(request):
    return {"site_name": "mpia.com"}


def inject_year(request):
    return {"date": datetime.utcnow() }
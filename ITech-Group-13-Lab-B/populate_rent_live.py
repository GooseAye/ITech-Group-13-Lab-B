import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rentlive.settings')

import django
django.setup()
from rent_live.models import Category, LettingAgent, City, Rental_Property, User, Comment

def populate():

    letting_agents = [
        {'name': 'Dave Smith',
        'description': 'Landlord operating out of Glasgow',
        'phone': '0712345678',
        'email': 'DaveSmith@gmail.com',
        'category': 'landlord',
        'city': 'GLA'},
        {'name': 'John Davidson',
        'description': 'Letting Agent operating out of Edinburgh',
        'phone': '078889992',
        'email': 'JohnDavidsonh@gmail.com',
        'category': 'agent',
        'city': 'EDI'},
        {'name': 'Mary Fergusson',
        'description': 'Letting agent operating out of Glasgow',
        'phone': '0798765432',
        'email': 'MaryF@gmail.com',
        'category': 'landlord',
        'city': 'GLA'},
    ]

    categories = [
        {'name': 'landlord',
        'description': 'Private person looking to rent a small amount of privately owned properties'},
        {'name': 'agent',
        'description': 'Person working for a letting agency'},
        {'name': 'agency',
        'description': 'Company created to manage and let rentals'},
    ]

    cities = [
        {'name': 'Glasgow',
        'uniqueName': 'gla',
        'description': 'Scotlands largest city',
        'categories': {'landlord', 'agency', 'agent'}
        },
        {'name': 'Edinburgh',
        'uniqueName': 'edi',
        'description': 'Scotlands capital city',
        'categories': {'landlord', 'agency', 'agent'}
        },{'name': 'Dundee',
        'uniqueName': 'dnd',
        'description': 'A city',
        'categories': {'landlord', 'agency', 'agent'}
        },
    ]

    rentals = [
        {'name': '123 Fake St',
        'address': '123 Fake St, Glasgow, G11 1A1',
        'description': '1 bedroom flat in Southside',
        'city': 'gla',
        'lettingAgent': 'Mary Fergusson',
        'price': 400,
        'size': 2,
        'followers': 254,
        'state': True},
        {'name': '321 Fake Av',
        'address': '321 Fake Av, Edinburgh, EH12 1H1',
        'description': '1 bedroom flat in Morningside',
        'city': 'edi',
        'lettingAgent': 'John Davidson',
        'price': 200,
        'size': 4,
        'followers': 1243,
        'state': True},
        {'name': '445 Unreal St',
        'address': '445 Unreal St, Glasgow, G22 3J2',
        'description': '1 bedroom flat in West End',
        'city': 'gla',
        'lettingAgent': 'Dave Smith',
        'price': 800,
        'size': 6,
        'followers': 112,
        'state': True},
    ]
        
    for cat in categories:
        add_category(cat['name'], cat['description'])

    for l in letting_agents:
        add_agent(l['name'], l['description'], l['phone'], l['email'], l['city'])

    for c in cities:
        add_city(c['name'], c['uniqueName'], c['description'])

    for r in rentals:
        add_rental(r['name'], r['address'], r['description'], r['city'], r['lettingAgent'], r['price'], r['size'], r['followers'], r['state'])



def add_category(name, description):
    c = Category.objects.get_or_create(name=name)[0]
    c.description = description
    c.save()
    return c

def add_agent(name, description, phone, email, city):
    l = LettingAgent.objects.get_or_create(name=name)
    l[0].description = description
    l[0].phone = phone
    l[0].email = email
    #l.category = category
    l[0].city = city
    l[0].save()
    return l[0]

def add_city(name, uniqueName, description):
    c = City.objects.get_or_create(uniqueName=uniqueName)
    c[0].name = name
    c[0].description = description
    #c[0].categories = categories
    c[0].save()
    return c[0]

def add_rental(name, address, description, city, lettingAgent, price, size, followers, state):
    r = Rental_Property.objects.get_or_create(address=address)
    r[0].name = name
    r[0].description = description
    r[0].city = city
    r[0].lettingAgent = lettingAgent
    r[0].price = price
    r[0].size = size
    r[0].followers = followers
    r[0].state = state
    r[0].save()
    return r



if __name__ == '__main__':
    print("Starting the RentLive Population Script...")
    populate()
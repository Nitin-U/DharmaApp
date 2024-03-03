import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dharma_App.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from django.contrib.auth.models import User
from cart.models import Product
from login.models import UserData
from faker import Faker
from django.contrib.auth.hashers import make_password

### MODEL POPULATE HERE
fakegen = Faker()

def populate(value):
    for _ in range(value):  # You can adjust the number of users you want to create
            
            #USER MODEL FIELDS
            username = fakegen.unique.user_name()
            # email = fakegen.email()
            emails = ['abc@gmail.com', 'mno@gmail.com', 'xyz@gmail,com']
            email = random.choice(emails)
            raw_password = "testpassword123"
            password = make_password(raw_password)
            is_active = "1"

            #USER MODEL POPULATE
            user, created = User.objects.get_or_create(username=username, email=email, password=password, is_active=is_active) #Create a User instance

            #USERDATA MODEL FIELDS
            raw_phone = "9845112233"
            phone_number = raw_phone
            roles = ['Customer', 'Package Provider', 'Product Seller']
            role = random.choice(roles)

            #PRODUCT MODEL FIELDS
            product_name = fakegen.random_element(elements=('Pashupatinath Temple',
            'Swayambhunath Stupa (Monkey Temple)',
            'Boudhanath Stupa',
            'Lumbini (Birthplace of Lord Buddha)',
            'Muktinath Temple',
            'Dakshinkali Temple',
            'Janaki Mandir (Janakpur Temple)',
            'Manakamana Temple',
            'Gosaikunda Lake',
            'Tengboche Monastery',
            'Pathibhara Devi Temple',
            'Baraha Kshetra',
            'Galeshwor Temple',
            'Tansen',
            'Budhanilkantha Temple',
            'Gupteshwor Mahadev Cave',
            'Bhimeshwor Temple',
            'Changunarayan Temple',
            'Halesi Mahadev',
            'Tansen Durbar',
            'Baglung Kalika Temple',
            'Patale Chhango (Devil\'s Fall)',
            'Charikot Bhimsen Temple',
            'Swargadwari',
            'Chandeshwari Temple',
            'Bindhyabasini Temple',
            'Namobuddha',
            'Khaptad Baba Ashram',
            'Narayangadh Bhimsen Temple',
            'Mahabouddha Temple',
            'Bajrayogini Temple',
            'Chilancho Stupa',
            'Dhulikhel Narayanthan Temple',
            'Kirateshwar Mahadev Temple',
            'Ridi Bazaar',
            'Tansen Bhagwati Temple',
            'Sanga Bhagwati Temple',
            'Halesi Mahadev',
            'Indreshwor Temple',
            'Rani Mahal',
            'Shaligram',
            'Gokarneshwor Mahadev Temple',
            'Changu Narayan Temple',
            'Budhasingh Kalinga',
            'Namo Buddha Stupa',
            'Siddha Gufa',
            'Mai Pokhari',
            'Godavari Botanical Garden',
            'Dantakali Temple',
            'Ruru Kshetra',
            'Muktinath Temple',
            'Swayambhunath Stupa (Monkey Temple)'))
            product_type = fakegen.random_element(elements=('Package', 'Product'))
            product_category = fakegen.random_element(elements=('Category1', 'Category2', 'Category3', 'Category4', 'Category5'))
            product_description = fakegen.text(max_nb_chars=144)
            product_quantity = random.randint(1, 100)
            product_price = random.uniform(1.0, 1000.0)
            product_stock = random.randint(0, 1)
            product_location = fakegen.random_element(elements=('Kathmandu',
            'Kathmandu',
            'Kathmandu',
            '',
            'Mustang',
            'Kathmandu',
            'Janakpur',
            'Gorkha',
            'Langtang',
            'Everest Region',
            'Taplejung',
            'Sunsari',
            'Myagdi',
            'Palpa',
            'Kathmandu',
            'Pokhara',
            'Dolakha',
            'Bhaktapur',
            'Khotang',
            'Palpa',
            'Baglung',
            'Pokhara',
            'Dolakha',
            'Pyuthan',
            'Banepa',
            'Pokhara',
            'Kavre',
            'Khaptad',
            'Chitwan',
            'Patan',
            'Sankhu',
            'Bhaktapur',
            'Dhulikhel',
            'Chitwan',
            'Gulmi',
            'Palpa',
            'Kavre',
            'Khotang',
            'Panauti',
            'Palpa',
            'Muktinath',
            'Kathmandu',
            'Bhaktapur',
            'Jhapa',
            'Kavre',
            'Nuwakot',
            'Ilam',
            'Lalitpur',
            'Dharan',
            'Palpa',
            'Mustang',
            'Kathmandu'))
            seller = User.objects.order_by('?').first() #Retrieve or create a User instance to use as the seller. Randomly select a seller from existing users, you can adjust this based on your requirements.
            
            #USERDATA MODEL POPULATE
            UserData.objects.get_or_create(user=user, phone_number=phone_number, role=role)
            Product.objects.create(
            product_name=product_name,
            product_type=product_type,
            product_category=product_category,
            product_description=product_description,
            product_quantity=product_quantity,
            product_price=product_price,
            product_stock=product_stock,
            product_location=product_location,
            seller=seller)

            #PRODUCT MODEL POPULATE

def main():
      no = int(input("How Many Records Do We Wanna Populate:"))
      populate(no)

if __name__=="__main__":
      main()
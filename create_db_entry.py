
from app import User



def create_db_entry():
    db_entry = User(login='anton_2002',
         surname='Иванов',
         name='Иван',
         patronymic='Иваныч',
         email = 'something@gmail.com',
         contact1_name = 'Vk',
         contact1_value = 'vk.com/id2134893',
         contact2_name = 'tg',
         contact2_value = '@sample_text',
         about = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         growth_area = 'Программирование, Искусство',
         tags = 'Cool tag',
         education = 'Баклавр колбасных изделий в Томском тракторном институте',
         courses = 'Coursera "Programming for Everobody", Stepik "Программирование на python"',
         projects ='Generation digits from mnist dataser',
         # job_experience = db.Column(db.Text, nullable=True)
         hard_skills = 'Программирование, АиДС, математика',
         soft_skills = 'Коммуникабельность'
    )
    return db_entry

def none_db_entry():
     db_entry = User(login='none',
                     surname='Kozlova',
                     name='Anna',
                     email='vsevolod026@gmail.com',
                     contact1_name='Vk',
                     contact1_value='vk_link',
                     contact2_name='tg',
                     contact2_value='@sample_text',
                     growth_area='programming, datascience',
                     tags='Cool tag',
                     education='Баклавр колбасных изделий в Томском тракторном институте',
                     courses='Coursera DS, Stepik neuro application',
                     projects='Проект по разработке приколов\n Проект по питону',
                     # job_experience = db.Column(db.Text, nullable=True)
                     )
     return db_entry
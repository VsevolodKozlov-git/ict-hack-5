
from app import User


def create_db_entry():
    db_entry = User(login='anna228',
         surname='Kozlova',
         name='Anna',
         patronymic='Denisovna',
         email = 'vsevolod026@gmail.com',
         contact1_name = 'Vk',
         contact1_value = 'vk_link',
         contact2_name = 'tg',
         contact2_value = '@sample_text',
         contact3_name = 'whatsapp',
         contact3_value = '+7...',
         about = 'something about me and my life',
         growth_area = 'programming, datascience',
         tags = 'Cool tag',
         education = 'Баклавр колбасных изделий в Томском тракторном институте',
         courses = 'Coursera DS, Stepik neuro application',
         projects ='Проект по разработке приколов\n Проект по питону',
         # job_experience = db.Column(db.Text, nullable=True)
         hard_skills = 'Программирование',
         soft_skills = 'Отсутствуют'
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
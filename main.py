from PhoneNumber import get_phone_number
from Email import get_mail
from NameEmployee import get_name
from GenderEmployee import get_gender

filename = 'resume_for_test_2.pdf'
#filename = 'Мисоченко Ульяна.pdf'
#filename = 'Тарабрин Кирилл Викторович.pdf'

get_name(filename)
get_phone_number(filename)
get_mail(filename)
get_gender(filename)
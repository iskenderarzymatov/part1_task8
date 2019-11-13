isken = {'Usain':1, 'Me': 2, 'Aybek':3}
isken2 = {1: 'Usain', 2: 'Me', 3: 'Aybek'}

def choice_to_number(choice):
    return isken[choice]
    
def number_to_choice(number):
    return isken2[number]
   


def test_choice_to_number():
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Me') == 2
    assert choice_to_number('Aybek') == 3
def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Me'
    assert number_to_choice(3) == 'Aybek'
def test_all():
    try:
        test_choice_to_number()
        test_number_to_choice()
    except AssertionError:
        print("WRONG")
    else:
        print("SUCCESS")

test_all()
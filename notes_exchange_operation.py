def notes_operation(amount_into_list):
    num_of_notes = 0
    for amount in amount_into_list[:]:
        if amount % 100 == 0:
            print(f'{amount // 100} hundred naira notes')
            num_of_notes += amount // 100
            amount_into_list.remove(amount)
            print(amount_into_list)
            continue
        else:
            pass
    for amount in amount_into_list[:]:
        if amount % 50 == 0:
            print(f'{amount // 50} fifty naira notes')
            num_of_notes += amount // 50
            print(amount_into_list)
            break
        elif amount % 50 > 1:
            print(f'{amount // 50} fifty naira notes')
            num_of_notes += amount // 50
            amount_into_list.remove(amount)
            remender = amount % 50
            amount_into_list.insert(0, remender)
            print(amount_into_list)
            break
        else:
            pass
    for amount in amount_into_list[:]:
        if amount % 20 == 0:
            print(f'{amount // 20} twenty naira notes')
            num_of_notes += amount // 20
            amount_into_list.remove(amount)
            print(amount_into_list)
            break
        elif amount % 20 > 1:
            print(f'{amount // 20} twenty naira notes')
            num_of_notes += amount // 20
            amount_into_list.remove(amount)
            remender = amount % 20
            amount_into_list.insert(0, remender)
            print(amount_into_list)
            break
        else:
            pass
    for amount in amount_into_list[:]:
        if amount % 10 == 0:
            print(f'{amount // 10} ten naira notes')
            num_of_notes += amount // 10
            amount_into_list.remove(amount)
            print(amount_into_list)
            break
        elif amount % 10 > 0:
            print(f'{amount // 10} ten naira notes')
            num_of_notes += amount // 10
            amount_into_list.remove(amount)
            remender = amount % 10
            amount_into_list.insert(0, remender)
            print(amount_into_list)
            break
        else:
            pass
    for amount in amount_into_list[:]:
        if amount % 5 == 0:
            print(f'{amount // 5} five naira notes')
            num_of_notes += amount // 5
            amount_into_list.remove(amount)
            print(amount_into_list)
            break
        elif amount % 5 > 0:
            print(f'{amount // 5} five naira notes')
            num_of_notes += amount // 5
            amount_into_list.remove(amount)
            remender = amount % 5
            amount_into_list.insert(0, remender)
            print(amount_into_list)
            break
        else:
            pass

    print(num_of_notes)


amount = int(input('Enter number: '))
c = 1
amount_into_list = []
while amount != 0:
    z = amount % 10
    amount_into_list.append(z * c)
    amount = amount // 10
    c *= 10

amount_into_list.reverse()
print(amount_into_list)

notes_operation(amount_into_list)
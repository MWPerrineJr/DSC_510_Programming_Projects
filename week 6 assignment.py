#DSC 510
# Week 6
# Programming Assignment
# Author Michael Perrine
# 10/04/2024


def main():
    print('week 6')
if __name__ == '__main__':
    main()

# temperature stores the list of temps selected by user

temperature = []

# the loop will continue to ask for a temperature until they select to quit

while True:
    value = int(input('Enter a temperature: \n'))
    temperature.append(value)
    choice= input('Enter another temperature? (y/n): \n ')

    if choice.lower() == 'y':
        print('Thank you')
    elif choice.lower() == 'n':
         print('Thank you')
         break
    else:
        print('Wrong selection please try again')
        continue

temperature_count= len(temperature)
print(temperature)
print(max(temperature))
print(min(temperature))
print(f'The total number of tempertures are {temperature_count}')

main()













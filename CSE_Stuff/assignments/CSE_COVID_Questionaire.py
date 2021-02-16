print('Welcome to the COVID symptom analyzer! Please only answer with "yes" or "no" to recieve accurate results.\n')
symptoms = [' fever? ', 
    ' chills? ', 
    ' cough? ', 
    ' shortness of breath? ', 
    ' sore muscles? ', 
    ' runny nose? ', 
    ' sore throat? ', 
    ' headache? ',
    ' mausea / vomiting? ',
    ' adbominal pain? ',
    ' diarrhea? ']
x = list()
count_yes = 0
count_no = 0
for symptom in symptoms:
  answer = input('Do you have (a)' + symptom)
  x.append(answer)
  if answer == 'yes':
      answer_a = input('Is this normal for you, perhaps due to allergies? ')
      print('\ncontinuing... ')
      if answer_a == 'yes':
          count_yes += 1
      elif answer_a == 'no':
          count_no += 1   
print('Your responses are', x)
print('You answered yes to', count_yes + count_no, 'questions, and', count_no, 'of the symptoms are not normal for you.')
if count_no > 0:
    print('We recommend you stay home.')
elif count_no == 0:
    print('You are healthy, and you can go outside.')
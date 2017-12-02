import csv

answers={
    'привет': 'И тебе привет!',
    'как дела': 'Лучше всех',
    'пока': 'Увидимся'
    }

with open ('answers_list.csv','w',encoding='utf-8') as qa:
    writer = csv.writer(qa)
    #fields = ['question', 'answer']
    #writer = csv.DictWriter(qa, fields, delimiter=';')
    #writer.writeheader()
    writer = csv.writer(qa, delimiter=';')
    for r in answers:
        writer.writerow([str(r),str(answers[r])])

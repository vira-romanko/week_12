import csv
import matplotlib.pyplot as plt

categories = []
men = []
women = []
men_2014 = []
women_2014 = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
    	if line_count is 0:
    		categories.append(row)
    		line_count += 1
    	elif row[4] == "CAN":
    		men.append([int(row[0]), row[5], row[7]])

    	else:
    		women.append([int(row[0]), row[5], row[7]])
    print('total medals for men:', len(men))
    print("total medals for women:", len(women))

    print('processed', line_count, 'rows of data')

    


for medal in man:
	if medal[0] == 2014 and medal[3] =="Gold" or "Silver" or "Bronze":
		man_2014.append(medal)


for medal in women:
    if medal[0] == 2014 and medal[3] =="Gold" or "Silver" or "Bronze":
        women_2014.append(medal)


print('men won', len(men_2014), 'medals men won in 2014')
print('women won', len(women_2014), 'medals women won in 2014')
print('processed', line_count, 'rows of data')


labels = "Men", "Women"
sizes = [men_2014, women_2014]
colors = ['yellowgreen', 'lightgreen']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title(" Medal Number men vs women")
plt.xlabel("Medal Count 2014")
plt.show()


# filter 2014 based on gender

# pie chart man vs women
#how many medals for each as a precentage of the total		   		     		     		     		 
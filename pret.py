import matplotlib.pyplot as plt

# constants
P = 1500000
Ta = 6/100
Tm = Ta/12
Y = 30
Ym = Y*12

#summary
print("montant emprunte: ", P)
print("taux annuel(%): ", Ta*100)

#Numerator
Numerator = P*(1+Tm)**Ym

#Denominator
Denominator = 0
for i in range (Ym):
    Denominator += (1+Tm)**i
  
# remboursement mensuel sans assurance
rm = Numerator/Denominator
print ("remboursement mensuel: ", rm)

## Interets mensuels
#months = []
#Interets = []
#reste_a_rembourser = P
#month = 1
#while (reste_a_rembourser > 0):
#    months.append(month)
#    Interets.append(reste_a_rembourser*Tm)
#    reste_a_rembourser = reste_a_rembourser - rm + (reste_a_rembourser*Tm)
#    month += 1
#
## Create plot
#plt.plot(months, Interets, marker='o', color='blue', linestyle='--', label='Interets mensuels')
#
## Add labels and title
#plt.xlabel('Mois')
#plt.ylabel('Interets')
#plt.title('Interets')
#plt.legend()
#
## Show plot
#plt.show()


# Interets annuels
years = []
Interets = []
reste_a_rembourser = P
Interets_annee_en_cours = 0
Interets_year_1 = 0
month = 1
year = 1
while (reste_a_rembourser > 0):
    Interets_annee_en_cours += reste_a_rembourser*Tm
    reste_a_rembourser = reste_a_rembourser - rm + (reste_a_rembourser*Tm)
    if month%12==0:
        years.append(year)
        print ("Interets annee:", year, " : ",Interets_annee_en_cours)
        Interets.append(Interets_annee_en_cours)
        if year == 1:
            Interets_year_1 = Interets_annee_en_cours
        Interets_annee_en_cours = 0
        year += 1
    month+=1
    

# Tax deduction
W2_1 = 300000
W2_2 = 540000
W2 = W2_1 + W2_2
Taxable_income = W2 - 29200
print("Taxable_income: ",Taxable_income)
Federal_tax_brackets = [[10,0],[12,23850],[22,96950],[24,206700],[32,394600],[35,501050],[37,751600]]
State_tax_brackets = [[1,0],[2,20199],[4,47885],[6,75577],[8,104911],[9.3,132591] ,[10.3,677279],[11.3,812729],[12.3,1354557]]

print("Interets_year_1: ", Interets_year_1)
Federal_tax_discount_year_1 = (Taxable_income - 751600)*0.37 + (Interets_year_1 - (Taxable_income - 751600))*0.35
State_tax_discount_year_1 = Interets_year_1*0.103
Total_tax_discount_year_1 =  Federal_tax_discount_year_1 + State_tax_discount_year_1
print("Federal_tax_discount_year_1: ", Federal_tax_discount_year_1)
print("State_tax_discount_year_1: ", State_tax_discount_year_1)
print("Total_tax_discount_year_1: ", Total_tax_discount_year_1)

print("Total_tax_discount_year_1_per_month: ", Total_tax_discount_year_1/12)
print("Reboursement mensuel avec tax decution: ", rm - Total_tax_discount_year_1/12)

# Create plot
#print (Interets)
plt.plot(years, Interets, marker='o', color='blue', linestyle='--', label='Interets annuels')

# Add labels and title
plt.xlabel('years')
plt.ylabel('Interets annuels')
plt.title('Interets annuels')
plt.legend()

# Show plot
plt.show()


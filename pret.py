import matplotlib.pyplot as plt

# constants
_ONE_MILLION_ = 1000000
P = 1.7*_ONE_MILLION_
T = 5.25
Ta = T/100
Tm = Ta/12
Y = 30
Ym = Y*12

# income and tax brackets
W2_1 = 300000
W2_2 = 540000
W2 = W2_1 + W2_2
Non_itemized_federal_standard_deduction = 29200
Non_itemized_state_standard_deduction = 30000

Taxable_income = W2

print("Taxable_income: ",Taxable_income)
Federal_tax_brackets = [[10,0],[12,23850],[22,96950],[24,206700],[32,394600],[35,501050],[37,751600]]
State_tax_brackets = [[1,0],[2,20199],[4,47885],[6,75577],[8,104911],[9.3,132591] ,[10.3,677279],[11.3,812729],[12.3,1354557]]

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
print (" ------------ Remboursemnt mensuel  ------------ ")
remboursement_mensuel = Numerator/Denominator
print ("remboursement mensuel: ", remboursement_mensuel)

# Interets annuels
print (" ------------ Interets annuels ------------ ")
years = []
Interets = []
reste_a_rembourser = P
Interets_annee_en_cours = 0
Interets_year_1 = 0
month = 1
year = 1
while (reste_a_rembourser > 0):
    Interets_annee_en_cours += reste_a_rembourser*Tm
    reste_a_rembourser = reste_a_rembourser - remboursement_mensuel + (reste_a_rembourser*Tm)
    if month%12==0:
        years.append(year)
        print ("Interets annee:", year, " : ", int(Interets_annee_en_cours))
        Interets.append(Interets_annee_en_cours)
        if year == 1:
            Interets_year_1 = int(Interets_annee_en_cours)
        Interets_annee_en_cours = 0
        year += 1
    month+=1
    

# Tax deduction
print (" ------------ Tax deduction  ------------ ")
print("Interets_year_1: ", Interets_year_1)
    
# Find the brackets that correspond to the tax income
def find_what_deductible_to_what_bracket(w_d_t_w_b, tax_brackets, deduction):
    deductible_of_this_bracket=0
    total_deductible_for_all_brackets=0
    for i in range (len(tax_brackets)-1, -1,-1): # if len of list brackets is , i goes from 6 to 0
        if total_deductible_for_all_brackets == 0:
            # total_deductible_for_all_brackets == 0 means that we have not found yet the highest bracket
            # that corresponds to the taxable income
            if Taxable_income > tax_brackets[i][1]:
                if deduction < Taxable_income - tax_brackets[i][1]:
                    deductible_of_this_bracket = deduction
                    total_deductible_for_all_brackets = deduction
                    w_d_t_w_b.append([i,deduction])
                else:
                    deductible_of_this_bracket = Taxable_income - tax_brackets[i][1]
                    total_deductible_for_all_brackets = deductible_of_this_bracket
                    w_d_t_w_b.append([i,deductible_of_this_bracket])
        elif total_deductible_for_all_brackets<deduction:
            # if taxable income is in this bracket 
            # let see how much of interest of the year correspond to
            if tax_brackets[i+1][1]-tax_brackets[i][1] > deduction-total_deductible_for_all_brackets:
                deductible_of_this_bracket = deduction-total_deductible_for_all_brackets
                total_deductible_for_all_brackets = deduction
                w_d_t_w_b.append([i,deductible_of_this_bracket])
            else:
                deductible_of_this_bracket = tax_brackets[i+1][1]-tax_brackets[i][1]
                total_deductible_for_all_brackets += deductible_of_this_bracket
                w_d_t_w_b.append([i,deductible_of_this_bracket])

print(" --- Federal ---")
print("In case of itemization, here is what can be deducted from federal tax income")
what_deductible_to_what_bracket = []
find_what_deductible_to_what_bracket(what_deductible_to_what_bracket, Federal_tax_brackets, Interets_year_1)
print(what_deductible_to_what_bracket)
federal_saving = 0
for i in range(len(what_deductible_to_what_bracket)):
    tax_bracket_index = what_deductible_to_what_bracket[i][0]
    federal_saving += Federal_tax_brackets[tax_bracket_index][0]*what_deductible_to_what_bracket[i][1]/100
print("federal_saving: ", int(federal_saving))

print("But if in case of itemization, the default discount from tax income no longer apply")
what_deductible_to_what_bracket = []
find_what_deductible_to_what_bracket(what_deductible_to_what_bracket, Federal_tax_brackets, Non_itemized_federal_standard_deduction)
print(what_deductible_to_what_bracket)
federal_loosing = 0
for i in range(len(what_deductible_to_what_bracket)):
    tax_bracket_index = what_deductible_to_what_bracket[i][0]
    federal_loosing += Federal_tax_brackets[tax_bracket_index][0]*what_deductible_to_what_bracket[i][1]/100
print("federal_loosing: ", int(federal_loosing))


print(" --- State ---")
print("In case of itemization, here is what can be deducted from state tax income")
what_deductible_to_what_bracket = []
find_what_deductible_to_what_bracket(what_deductible_to_what_bracket, State_tax_brackets, Interets_year_1)
print(what_deductible_to_what_bracket)
state_saving = 0
for i in range(len(what_deductible_to_what_bracket)):
    tax_bracket_index = what_deductible_to_what_bracket[i][0]
    state_saving += State_tax_brackets[tax_bracket_index][0]*what_deductible_to_what_bracket[i][1]/100
print("state_saving: ", int(state_saving))

print("But if in case of itemization, the default discount from tax income no longer apply")
what_deductible_to_what_bracket = []
find_what_deductible_to_what_bracket(what_deductible_to_what_bracket, State_tax_brackets, Non_itemized_state_standard_deduction)
print(what_deductible_to_what_bracket)
state_loosing = 0
for i in range(len(what_deductible_to_what_bracket)):
    tax_bracket_index = what_deductible_to_what_bracket[i][0]
    state_loosing += State_tax_brackets[tax_bracket_index][0]*what_deductible_to_what_bracket[i][1]/100
print("state_loosing: ", int(state_loosing))

print(" --- TOTAL GAIN fist year ---")
total_gain = federal_saving + state_saving +  federal_loosing - state_loosing
print("remboursement mensuel sans deduction: ", remboursement_mensuel)
print("deduction mensuelle: ", int(total_gain/12))
print("remboursement mensuel avec deduction: ", remboursement_mensuel - int(total_gain/12))


print(" --- verify ---")
Federal_tax_discount_year_1 = (Taxable_income - 751600)*0.37 + (Interets_year_1 - (Taxable_income - 751600))*0.35
State_tax_discount_year_1 = Interets_year_1*0.103
Total_tax_discount_year_1 =  Federal_tax_discount_year_1 + State_tax_discount_year_1

print("Federal_tax_discount_year_1: ", Federal_tax_discount_year_1)
print("State_tax_discount_year_1: ", State_tax_discount_year_1)
print("Total_tax_discount_year_1: ", Total_tax_discount_year_1)

print("Total_tax_discount_year_1_per_month: ", Total_tax_discount_year_1/12)
print("Reboursement mensuel avec tax decution: ", remboursement_mensuel - Total_tax_discount_year_1/12)

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


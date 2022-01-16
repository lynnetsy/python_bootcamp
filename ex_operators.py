#CREA UN PROGRAMA QUE TE PREGUNTE CUANTOS AÑOS TIENES 
# Y QUE CON LAS OPERACIONES VISTAS ANTERIORMENTE NOS DIGA
#CUANTOS DIAS , SEMANAS Y MESES NOS QUEDAN PARA LLEGAR A 90 AÑOS
#RECUERDA QUE HAY 365 DIAS EN UN AÑO
#52 SEMANAS EN UN AÑO Y 12 MESES EN UN AÑO

current_age = int(input("What's your current age?\n"))

goal_years = 90
goal_90_months = 90 * 12
goal_90_weeks = 90 * 52
goal_90_days = 90 * 365

days_left = goal_90_days - (current_age * 365)
weeks_left = goal_90_weeks - (current_age * 52)
months_left = goal_90_months - (current_age * 12)
years_left = goal_years - current_age


message = f"You have {days_left} days,\n{weeks_left} weeks,\n{months_left} months,\n{years_left} years left."
print(message)
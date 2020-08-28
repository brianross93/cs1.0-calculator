# Calculation program allows user to plug in the wattage of their microwave to ensure 
# cooking times are accurate. 


#take the recommended wattage listed on ingredients from user
m_ingredient_wattage = int(input("What is the recommended wattage?"))
m_ingredient_time = int(input("How long does it say to cook it IN SECONDS?"))

#Get user input for microwave they currently have
m_user_wattage = int(input("How many watts is your microwave?"))

# Assign kilojoules for recommended ingredients by ENERGY = WATTAGE * SECONDS
m_kilojoules = m_ingredient_wattage * m_ingredient_time

# Print how many seconds the user needs to cook their food for SECONDS = ENERGY/WATTAGE
m_user_time = round(m_kilojoules/m_user_wattage)

print(f'Cook your meal for {m_user_time} seconds. ')
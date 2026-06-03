# PressureLab

# 1. Constantes:
massa_molar_acido_acetico = 60.052
massa_molar_bicarbonato = 84.007
massa_molar_gas_carbonico = 44.009
R = 0.08206

# 2. Mensagem inicial:
print()
print("Bem vindo ao PressureLab, aqui você poderá estimar a pressão do seu foguete!")
print("A equação da reação é: CH3COOH + NaHCO3 → CH3COONa + H2O + CO2")
print("A proporção é: 1 mol ácido = 1 mol bicarbonato")
print()

# 3. Entrada de dados
vinagre_ml = float(input("Volume de vinagre (mL): "))
acidez = float(input("Acidez (%): "))
temperatura_celsius = float(input("Temperatura (°C): "))
print()

bicarbonato_g = float(input("Massa de bicarbonato (g): "))
pureza = float(input("Pureza do bicarbonato (%): "))
print()

volume_garrafa = float(input("Volume da garrafa (L): "))
print()

# 4. Cálculo inicial:
massa_acido_acetico = vinagre_ml * (acidez / 100)
mols_acido_acetico = massa_acido_acetico / massa_molar_acido_acetico

massa_bicarbonato_puro = bicarbonato_g * (pureza / 100)
mols_bicarbonato = massa_bicarbonato_puro / massa_molar_bicarbonato

# 5. Cálculo do reagente limitante:
if mols_acido_acetico < mols_bicarbonato:
    mols_co2 = mols_acido_acetico
    reagente_limitante = "Ácido acético"
    reagente_excesso = "Bicarbonato"
    excesso = massa_bicarbonato_puro - (mols_co2 * massa_molar_bicarbonato)
else:
    mols_co2 = mols_bicarbonato
    reagente_limitante = "Bicarbonato"
    reagente_excesso = "Ácido acético"
    excesso = massa_acido_acetico - (mols_co2 * massa_molar_acido_acetico)

# 6. Produção de gás carbônico:
massa_co2 = mols_co2 * massa_molar_gas_carbonico

# 7. Lei dos gases ideais:
temperatura_kelvin = temperatura_celsius + 273.15
pressao_atm = (mols_co2 * R * temperatura_kelvin) / volume_garrafa
pressao_kpa = pressao_atm * 101.325
pressao_psi = pressao_atm * 14.6959

if pressao_psi <= 50:
    aviso = "Pressão baixa para sistemas de garrafa PET."
elif pressao_psi <= 100:
    aviso = "Pressão moderada. Utilize recipientes em boas condições."
elif pressao_psi <= 150:
    aviso = "Pressão alta. Recomenda-se cautela durante os testes."
else:
    aviso = "Pressão muito alta. Verifique cuidadosamente a resistência do sistema."

# 8. Resultados
print("Resultados:")
print()

print(f"Mols de ácido acético: {mols_acido_acetico:.3f} mol")
print(f"Mols de bicarbonato: {mols_bicarbonato:.3f} mol")
print()

print(f"Reagente limitante: {reagente_limitante}")
print(f"Reagente em excesso: {reagente_excesso}")
print(f"Massa de reagente em excesso: {excesso:.3f}")
print()

print(f"CO₂ produzido: {massa_co2:.3f} gramas")
print(f"CO₂ produzido: {mols_co2:.3f} mol")
print()

print("Pressão estimada:")
print(f"• ATM: {pressao_atm:.3f} atm")
print(f"• kPa: {pressao_kpa:.3f} kPa")
print(f"• psi: {pressao_psi:.3f} psi")
print()

print(f"Avaliação: {aviso}")
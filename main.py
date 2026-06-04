# PressureLab
import math

# 1. Constantes:
massa_molar_acido_acetico = 60.052
massa_molar_bicarbonato = 84.007

massa_molar_acetato = 82.034
massa_molar_gas_carbonico = 44.009
massa_molar_agua = 18.015

R = 0.08206
pressao_atmosferica = 101.3
densidade_agua = 1000

# 2. Mensagem inicial:
print()
print("Bem vindo ao PressureLab, aqui você poderá estimar a pressão do seu foguete!")
print("A equação da reação é: CH3COOH + NaHCO3 → CH3COONa + H2O + CO2")
print("A proporção é: 1 mol de reagente = 1 mol de produto")
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
diametro_tubeira = float(input("Diametro da tubeira (mm): "))
print()

# 4. Cálculo inicial:
massa_acido_acetico = vinagre_ml * (acidez / 100)
mols_acido_acetico = massa_acido_acetico / massa_molar_acido_acetico

massa_bicarbonato_puro = bicarbonato_g * (pureza / 100)
mols_bicarbonato = massa_bicarbonato_puro / massa_molar_bicarbonato

# 5. Cálculo do reagente limitante:
if mols_acido_acetico < mols_bicarbonato:
    reagente_limitante = "Ácido acético"
    reagente_excesso = "Bicarbonato"

    mols_acetato = mols_acido_acetico
    mols_co2 = mols_acido_acetico
    mols_h2o = mols_acido_acetico

    excesso = massa_bicarbonato_puro - (mols_acetato * massa_molar_bicarbonato)
    consumido = massa_bicarbonato_puro - excesso
else:
    reagente_limitante = "Bicarbonato"
    reagente_excesso = "Ácido acético"

    mols_acetato = mols_bicarbonato
    mols_co2 = mols_bicarbonato
    mols_h2o = mols_bicarbonato

    excesso = massa_acido_acetico - (mols_acetato * massa_molar_acido_acetico)
    consumido = massa_acido_acetico - excesso

# 6. Produção de acetato de sódio:
massa_acetato = mols_acetato * massa_molar_acetato

# 7. Produção de gás carbônico:
massa_co2 = mols_co2 * massa_molar_gas_carbonico

# 8. Produção de água:
massa_h2o = mols_h2o * massa_molar_agua

# 9. Lei dos gases ideais:
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

# 10. Diferença de pressão:
diferenca_pressao_kpa = pressao_kpa - pressao_atmosferica
delta_p = diferenca_pressao_kpa * 1000

# 11. Velocidade da água:
velocidade_agua = math.sqrt((2*delta_p)/densidade_agua)
velocidade_agua_kmh = velocidade_agua * 3.6

# 12. Área da tubeira:
area_tubeira_milimetros  = math.pi * ((diametro_tubeira / 2) ** 2)
area_tubeira_metros = area_tubeira_milimetros / 1000000

# 13. Vazão mássica:
vazao_massica = densidade_agua * area_tubeira_metros * velocidade_agua

# 14. Empuxo:
empuxo = vazao_massica * velocidade_agua
empuxo_kgf = empuxo / 9.807

# 15 . Resultados
print("Resultados Químicos:")
print()

print(f"Mols de ácido acético: {mols_acido_acetico:.3f} mol")
print(f"Mols de bicarbonato: {mols_bicarbonato:.3f} mol")
print()

print(f"Reagente limitante: {reagente_limitante}")
print(f"Reagente em excesso: {reagente_excesso}")
print()

print(f"Massa de {reagente_excesso} remanescente: {excesso:.3f}")
print(f"Massa de {reagente_excesso} consumida: {consumido:.3f}")
print()

print(f"Quantidade de acetato de sódio produzido:")
print(f"• g: {massa_acetato:.3f} gramas")
print(f"• mol: {mols_acetato:.3f} mols")
print()

print("Quantidade de CO₂ produzido:")
print(f"• g: {massa_co2:.3f} gramas")
print(f"• mol: {mols_co2:.3f} mols")
print()

print("Quantidade de H₂O produzido:")
print(f"• g: {massa_h2o:.3f} gramas")
print(f"• mol: {mols_h2o:.3f} mols")
print()

print("Resultados de Pressão:")
print()

print("Pressão estimada:")
print(f"• ATM: {pressao_atm:.3f} atm")
print(f"• kPa: {pressao_kpa:.3f} kPa")
print(f"• psi: {pressao_psi:.3f} psi")
print()

print(f"Avaliação: {aviso}")
print()

print("Diferença aproximada de pressão:")
print(f"• kPa: {diferenca_pressao_kpa:.3f} kPa")
print(f"• Pa: {delta_p:.3f} Pa")
print()

print("Resultados de Propulsão")
print()

print(f"Velocidade estimada da água:")
print(f"• m/s: {velocidade_agua:.3f} m/s")
print(f"• km/h: {velocidade_agua_kmh:.3f} km/h")
print()

print(f"Área aproximada da tubeira:")
print(f"• mm²: {area_tubeira_milimetros:.3f} mm²")
print(f"• m²: {area_tubeira_metros:.6f} m²")
print()

print(f"Vazão mássica: {vazao_massica:.3f} kg/s")
print()

print("Empuxo estimado:")
print(f"• N: {empuxo:.3f} N")
print(f"• kgf: {empuxo_kgf:.3f} kgf")
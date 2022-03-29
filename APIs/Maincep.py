from Acessocep import Acessocep

print("Digite o seu CEP: ")
cep = input()
obj_cep = Acessocep(cep)
cedro = obj_cep.acessar_url()
ddd, cidade, uf = obj_cep.acessar_url()
print(f"DDD: {ddd} \nCidade: {cidade} \nEstado: {uf}")
print("CEP: ", obj_cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

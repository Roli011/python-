koltes = [1200, 800, 1500, 700, 900, 1100, 400]


egyenleg = 5000
elmaradt = 0                        
elso_elmaradt = 0                  
napi_egyenlegek = []                 
for i in range(len(koltes)):
    if koltes[i] <= egyenleg:
        egyenleg = egyenleg - koltes[i]  
    else:
        elmaradt = elmaradt + 1           
        if elso_elmaradt == 0:
            elso_elmaradt = i + 1        
    napi_egyenlegek.append(str(egyenleg))

print(" " + " ".join(napi_egyenlegek))


if elmaradt > 0:
    print(f" {elmaradt} napon maradt el a vásárlás, először az {elso_elmaradt}. napon.")
else:
    print(" Minden nap sikerült vásárolni.")


if egyenleg >= 500:
    print(" Maradt tartalék.")
else:
    print(" Elfogyott a tartalék.")
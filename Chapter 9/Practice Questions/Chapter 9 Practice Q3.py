
for j in range(2,21):
    with open(f'tables{j}.txt','w') as f:
        for i in range(1,11):
            f.write(f"{j}X{i}={i*j}\n")
    
           


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from colorama import Fore, Back, Style, init

df = pd.read_csv("Pokemon.csv",
                index_col="Name")
                
def get_exact_name(user_input, dataframe):
    matches = dataframe[dataframe.index.str.lower() == user_input.lower()]
    if not matches.empty:
        return matches.index[0]
    return None
                
                
completer = WordCompleter(df.index, ignore_case=True)                
                

init(autoreset=True)



print("Welcome to pydex")


while True:
 name1 = prompt("First Pokemon: ", completer=completer).strip()
 pokemon1 = get_exact_name(name1,df)
 
 if pokemon1 is None:
    
  print(Fore.RED +"ERORR!!")
  print(f"{name1} did not found")
  print("pls check")
  
 else:
  break

while True:   
  name2 = prompt("Second Pokemon: ", completer=completer).strip()
  pokemon2 = get_exact_name(name2,df)
 
  if pokemon2 is None:
    
   print(Fore.RED +"ERORR!!")
   print(f"{name2} did not found")
   print("pls check")

  else:
   break
               
print(f"{pokemon1}:")
print(f"{df.loc[pokemon1].T.to_string()}")
print("")
print(f"{pokemon2}:")
print(f"{df.loc[pokemon2].T.to_string()}")

X =["HP",
   "Attack",
   "Defense",
   "Sp. Atk",
   "Sp. Def",
    "Speed"]
    
Y1 = np.array(df.loc[[pokemon1]].head(1)[X])[0]
Y2 = np.array(df.loc[[pokemon2]].head(1)[X])[0]

font=dict(fontsize="25",
          color="black",
          fontweight="heavy")
          
              

figure , axes = plt.subplots(2,1)     
    
axes[0].bar(X,Y1,color="Red")
axes[0].set_title(pokemon1,**font)
axes[0].set_ylim(0,260)  
axes[0].grid(axis="y")

     
axes[1].bar(X,Y2,color="Blue")    
axes[1].set_title(pokemon2,**font)
axes[1].set_ylim(0,260) 
axes[1].grid(axis="y")

plt.tight_layout()
plt.show()
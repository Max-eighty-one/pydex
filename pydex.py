import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from colorama import Fore, Back, Style, init


#------ turning on the libraries -----
df = pd.read_csv("Pokemon.csv",   # we use it to open our csv file
                index_col="Name") 
                                         
completer = WordCompleter(df.index, ignore_case=True) # we use it so we turning on the completer where we gonna use it for searching our pokemons                
                
init(autoreset=True) # we use it so we dont need to type Style.RESET_ALL every time
#--------------------------------------

#------------- ignoring messy cases in our inputs ------
def get_exact_name(user_input, dataframe):
    matches = dataframe[dataframe.index.str.lower() == user_input.lower()]
    if not matches.empty:
        return matches.index[0]
    return None
#--------------------------------------

#----- the main code and questions -------
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
#--------------------------------------   

#---------- the return ---------------               
print(f"{pokemon1}:")
print(f"{df.loc[pokemon1].T.to_string()}")
print("")
print(f"{pokemon2}:")
print(f"{df.loc[pokemon2].T.to_string()}")
#--------------------------------------

#--------- matplotlib -----------
stast =["HP",
   "Attack",
   "Defense",
   "Sp. Atk",
   "Sp. Def",
    "Speed"]
    
Poke1 = np.array(df.loc[[pokemon1]].head(1)[stast])[0]
Poke2 = np.array(df.loc[[pokemon2]].head(1)[stast])[0]


font=dict(fontsize="25",
          color="black",
          fontweight="heavy")
          
              
figure , axes = plt.subplots(2,1)   
  
  
print("bar or barh?")
while True:
 plt_choose=input("> ").lower().strip()

 if plt_choose == "bar":
    
  axes[0].bar(stast,Poke1,color="Red")
  axes[0].set_title(pokemon1,**font)
  axes[0].set_ylim(0,260)  
  axes[0].grid(axis="y")

     
  axes[1].bar(stast,Poke2,color="Blue")   
  axes[1].set_title(pokemon2,**font)
  axes[1].set_ylim(0,260) 
  axes[1].grid(axis="y")
  break
  
 elif  plt_choose == "barh":
        
  axes[0].barh(stast,Poke1,color="Red")
  axes[0].set_title(pokemon1,**font)
  axes[0].set_xlim(0,260)  
  axes[0].grid(axis="x")

     
  axes[1].barh(stast,Poke2,color="Blue")  
  axes[1].set_title(pokemon2,**font)
  axes[1].set_xlim(0,260) 
  axes[1].grid(axis="x")
  break
  
 else:
  print(Fore.RED +"ERORR!!")
  print("pls make sure only to type(barh or bar)")
    
plt.tight_layout()
plt.show()

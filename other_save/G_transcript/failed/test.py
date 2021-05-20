import sys
   
sys.stdout = open("save.txt", "w")

print('TEST')
    
sys.stdout.close()
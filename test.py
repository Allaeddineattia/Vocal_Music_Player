import os
os.system("find ./music -type f -iname \"*.mp3\" -printf \"%CY %Cj %CT  %p \n\" | sort -r -k1,1 -k2,2  -k3,3 | cut -d \  -f5-")
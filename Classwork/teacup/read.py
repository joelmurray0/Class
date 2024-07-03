image = [
     [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
     [0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0],
     [0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0],
     [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
     [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
     [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
     [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
]


def read_bytes(array):
     conversion_dict = {
          0: "0000000",
          1: "1111111"
     }
     
     with open("imageSave.txt", "w") as f:
          for i in array:
               for j in i:
                    f.write(conversion_dict[j] + " ")

def read_bytes_rle(array):
     conversion_dict = {
          0: "0000000",
          1: "1111111"
     }
     continued = True
     pos = [0,0]
     with open("imageSave.txt", "w") as f:
          while pos != [17,8]:
               count = 1
               while continued:
                    ppos = pos
                    if pos[0] == 17:
                         if pos[1] != 8:
                              pos[1] += 1
                              pos[0] = 0
                         else:
                              continued = False
                    else:
                         pos[0] += 1
                    print(pos)
                    if continued:
                         if array[pos[1]][pos[0]] == array[ppos[1]][ppos[0]]:
                              count += 1
                         else:
                              continued = False
               if count != 1:
                    f.write(f"{count} {conversion_dict[array[ppos[1]][ppos[0]]]} ")


#read_bytes(image)
read_bytes_rle(image)
print("done")
                    


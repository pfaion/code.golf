# # VERSION 1 (452/452)
# f = lambda i: f"{i} bottle{("","s")[i>1]} of beer"
# for i in range(99,1,-1):
#  print(f"{f(i)} on the wall, {f(i)}.")
#  print(f"Take one down and pass it around, {f(i-1)} on the wall.")
#  print()
# print("""1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.

# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.""")

# # VERSION 2 (351/351)
# f = lambda i: f"{("no more", i)[i>0]} bottle{("","s")[i!=1]} of beer"
# for i in range(99,0,-1):
#  print(f"{f(i)} on the wall, {f(i)}.")
#  print(f"Take one down and pass it around, {f(i-1)} on the wall.")
#  print()
# print("""No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.""")

# # VERSION 3 (257, 257)
# f=lambda i:f"{("no more", i)[i>0]} bottle{("","s")[i!=1]} of beer"
# w=" on the wall"
# for i in range(99,-1,-1):print(f"{f(i).capitalize()}{w}, {f(i)}.\n{("Go to the store and buy some more","Take one down and pass it around")[i>0]}, {f((99,i-1)[i>0])}{w}.\n")

# # VERSION 4 (249/249)
# f=lambda i:f"{("no more",i)[i>0]} bottle{("","s")[i!=1]} of beer"
# w=" on the wall"
# i=99
# while i>-1:print(f(i).capitalize()+w+f", {f(i)}.\n{("Go to the store and buy some more","Take one down and pass it around")[i>0]}, {f((99,i:=i-1)[i>-1])}{w}.\n")

# # VERSION 5 (151/151)
# # prep:
# code = R"""\
# f=lambda i:f"{("no more",i)[i>0]} bottle{("","s")[i!=1]} of beer"
# w=" on the wall"
# i=99
# while i>-1:print(f(i).capitalize()+w+f", {f(i)}.\n{("Go to the store and buy some more","Take one down and pass it around")[i>0]}, {f((99,i:=i-1)[i>-1])}{w}.\n")
# """
# print(code.encode().decode('u16'))
# code:
exec(bytes('ੜ㵦慬扭慤椠昺笢∨潮洠牯≥椬嬩㹩崰⁽潢瑴敬⡻∢∬≳嬩Ⅹㄽ絝漠⁦敢牥ਢ㵷•湯琠敨眠污≬椊㤽ਹ桷汩⁥㹩ㄭ瀺楲瑮昨椨⸩慣楰慴楬敺⤨眫昫Ⱒ笠⡦⥩⹽湜⡻䜢⁯潴琠敨猠潴敲愠摮戠祵猠浯⁥潭敲Ⱒ吢歡⁥湯⁥潤湷愠摮瀠獡⁳瑩愠潲湵≤嬩㹩崰ⱽ笠⡦㤨ⰹ㩩椽ㄭ嬩㹩ㄭ⥝筽絷尮≮਩','u16')[2:])

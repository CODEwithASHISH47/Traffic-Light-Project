#traffic light code

light = input("light : ")
if light == "red":
    print("stop")
elif light == "yellow":
    print("look around")
elif light == "green":
    print("go ahead")
elif light in ["brown","black","violet"]:
    print("the light is failed and broken")
else:
     print("get attention on yourself:")

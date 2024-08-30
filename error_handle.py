file = open("youtube_manager.txt", "w")

try: 
    file.write("Sabbir is a handsome boy")
finally:
    file.close()

with open("youtube_manager.txt", "w") as file:
    file.write("My name is omuk")
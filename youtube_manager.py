import json

# Name of the file
filename = "management.txt"

#To help for data reading from the file
def load_data():
    #Using try-catch incase there have any error
    try:
        with open(filename, "r") as file:
           test = json.load(file)
        #    print(test)
           return test
    except FileNotFoundError:
        return[]

#For helping to save the data which we will get from add_video function.
def helper_to_save_data(videos):
    #Dump use for writing in json file
    with open(filename, "w") as file:
        json.dump(videos, file)

#Showing the data to the user.
def list_all_videos(videos):
    print("\n")
    #enumerate use for making tupple so in that case we can indexing our json data
    for index, video in enumerate(videos, start=1):
       print(f"{index}. name: {video['name']}, duration: {video['time']}")
       
#Getting information from users and store it.
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video length: ")
    
    videos.append({"name": name, "time": time})
    helper_to_save_data(videos)

#Updating the video information 
def update_video(videos):
    #Getting all list so we can give choice to our user and through indexing we also can update the previous value
    list_all_videos(videos)
    index = int(input("Choose the video number you want to update: "))
    if 1<= index <= len(videos):
        name = input("Enter The New Name: ")
        time = input("Enter the New Time: ")
        videos[index-1] = {'name': name, 'time': time}
        #Saving new updated data
        helper_to_save_data(videos)
    else:
        print("Invaild Number")

#Deleting the data by indexing
def delete_vidoes(videos):
    list_all_videos(videos)
    index = int(input("Enter the index number you want to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        helper_to_save_data(videos)
    else:
        print("Invaild Number")

#The main will be the first function when app will run
def main():
    videos = load_data()

#For continuously running
    while True:
        print("\n YouTube Manager")
        print("1. List all youtube Videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter Your Choice: ")
        # print(videos)

#Instead of if/else using match for better uses. It's almost like Javascript switch case.
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_vidoes(videos)      
            case '5':
                break
            case _:
                print("Invaild choice")

#Checking and calling the main function        
if __name__ == "__main__":
    main()
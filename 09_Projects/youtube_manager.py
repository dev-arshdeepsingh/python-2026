import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data():
    with open("youtube.txt", 'w') as file:
        json.dump(videos,file)

def display_videos(videos):
    print("X" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video["name"]} Duration: {video["time"]}")
    print("X" * 70)

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter video Duraton: ")
    videos.append({'name': name,'time':time})
    save_data()
    print("Video Added!")

def update_video(videos):
    display_videos(videos)
    index = int(input("Enter video No. to update: "))
    name = input("Give New Video Name: ")
    time = input("Give new video duration: ")
    if index>0 and index<=len(videos):
        videos[index-1] = {'name': name, 'time': time}
        save_data()
        print("Video Updated!")
    else:
        print("Invalid Input!")


def delete_video(videos):
    display_videos(videos)
    index = int(input("Enter video No. to Delete: "))
    if index > 0 and index<= len(videos):
        del videos[index-1]
        save_data()
        print("Video Deleted!")
    else:
        print("Invalid Input!")



videos = load_data()

def main():
    #videos = []: We could use empty array too then use array methods like for loop to display, append() to add, remove() to delete etc but we will use new thing
    while True:
        print("\n YOUTUBE MANAGER / CHOOSE THE BELOW OPTIONS")
        print("1: View all Videos")
        print("2: Add New Video")
        print("3: Update any Video")
        print("4: Delete any Video")
        print("5: Exit")


        choice = input("Enter Your Choice: ")

        match choice:
            case "1":
                display_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                "Invalid Choice"


if __name__ == "__main__":
    main()
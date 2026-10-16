
import json

def load_data():
  try:
    with open('youtube.txt', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return[]

def save_data_helper(video):
  with open('youtube.txt', 'w') as file:
    json.dump(video, file)


def list_all_video(video):
 for index, video in enumerate(video, start=1):
   print(f"{index}.")
 def add_video(video):
  name=input ("enter video name") 
  time=input ("enter video time")
  video.append({'name':name ,'time':time}) 
  save_data_helper(video)
 def update_video(video):
   pass 
 def delete_video(video):
   pass 

def main(): 
    video=load_data()
    while True:
        print("/n youtube manager")
        print("/n list all youtube video")
        print("/n add a youtube video")
        print("/n update a youtube video ")
        print("/n delete a youtube video ")
        print("/n exit the app ")
        choice=input("enter ur choice")
        print(video)

    match choice:
            case '1': 
             list_all_video(video)
            case '2':
             add_video(video)
            case '3':
             update_video(video)
            case '4':
             delete_video(video)
            case '5':
             break
          

if __name__ == "__main__":
   main()
          
    
    
class A:    
        def __init__(self):
            self.name='masala chai'
            self.time='2 min'
        def display(self):
            print(f"video name is {self.name} and time is {self.time}")

            hi
            
import random


#identify music genre selections for the user
class HolySoundApp:
    def __init__(self):
        self.music_library = {
            "Christian Contemporary": ["Song1", "Song2", "Song3"],
            "Gospel": ["Song4", "Song5", "Song6"],
            "Christian Rap": ["Song7", "Song8", "Song9"],
            "Christian R&B": ["Song10", "Song11", "Song12"],
            "Christian Country": ["Song13", "Song14", "Song15"],
        }

    #show what happens when a user selects a certain genre of a song to play
    def play_random_song(self, genre=None):
        if genre:
            if genre in self.music_library:
                playlist = self.music_library[genre]
                if playlist:
                    song = random.choice(playlist)
                    print(f"Now playing: {song} ({genre})")
                else:
                    print(f"No songs available in the {genre} genre.")
            else:
                print(f"Invalid genre: {genre}")
        else:
            print("Please specify a genre to play.")
            

    #give the user the option to use the explore page and search for different songs
    def explore_music(self):
        print("Explore Page:")
        for genre, playlist in self.music_library.items():
            if playlist:
                print(f"{genre}: {', '.join(playlist)}")
            else:
                print(f"{genre}: No songs available")

if __name__ == "__main__":
    holy_sound_app = HolySoundApp()

    while True:
        print("\nA Holy Sound - Main Menu:")
        print("1. Play Random Song")
        print("2. Explore Music")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            genre = input("Enter the genre (Christian Contemporary/Gospel/Christian Rap/Christian R&B/Christian Country): ")
            holy_sound_app.play_random_song(genre)
        elif choice == "2":
            holy_sound_app.explore_music()
        elif choice == "3":
            print("Exiting A Holy Sound. Thank you for worshiping with us!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

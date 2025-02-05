import os

def create_m3u_files(music_folder):
    for root, dirs, files in os.walk(music_folder):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            m3u_file_path = os.path.join(dir_path, f"{dir_name}.m3u")
            with open(m3u_file_path, 'w') as m3u_file:
                for file_name in os.listdir(dir_path):
                    if file_name.endswith(('.mp3', '.wav', '.flac')):
                        file_path = os.path.join(dir_path, file_name)
                        m3u_file.write(f"{file_path}\n")
            print(f"Created {m3u_file_path}")

if __name__ == "__main__":
    user = os.getlogin()
    music_folder = f"C:\\Users\\{user}\\Music"
    create_m3u_files(music_folder)
#made with help of copilot uwu :3
#tested w le linkin park music owo

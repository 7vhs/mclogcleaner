#!/usr/bin/env python3
import os

#   Minecraft log cleaner by Toby

logname = input("Log file path: ")
term2locate = "[CHAT]"
skiplines = ["joined the game", "left the game", "completed the challenge", "made the advancement", "reached the goal"]
avoids = ["Vanishmod", "//", "{}"]
out_path = os.path.expanduser("~/Desktop/cleanedlog.txt")

try:
    with open(logname, 'r') as infile, open(out_path, 'w') as outfile:
        found_chat = False
        for line in infile:
            if term2locate in line:
                found_chat = True
                start_index = line.find(term2locate) + len(term2locate + " ")
                clean_line = line[start_index:]
                clean_line = clean_line.replace("<", "").replace(">", ":").replace("§r", "")
                if any (avoid in clean_line for avoid in avoids):
                    pass
                elif any (skipline in clean_line for skipline in skiplines):
                    outfile.write("\n" + clean_line + "\n")
                else:
                    outfile.write(clean_line)
        
        if not found_chat:
            print("This log doesn't have any chat messages in it!")
        else:
            print(f"Done! Cleaned log saved at '{out_path}'.")
except FileNotFoundError:
    print("Couldn't find this file!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
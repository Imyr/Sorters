import shutil
import time
import os
import re

# Made another anime sorter, this time regex based. This one works better IMO.
# I've tried to add examples and links to each regex, just to sort of make it easier to understand.
# Did a small (15720 sample size) test, and it didn't sort 0.37% (57) of the files. I guess it's okay.
# Unsorted files get pushed to (Dest. Folder/~Unsorted).

SOURCE_FOLDER = "H:/Anime/Airing/"
DESTINATION_FOLDER = "H:/Anime/Synced/"

# Matches {Group} {Title} ~~episode_number_and_other_junk~~  {Quality}
# https://regex101.com/r/Ri7a3n/2
REGEX_1 = r"\[(.+?)\][\.\s\_](.+?)[\.\s\_][v\_\.\-\~0-9\s]+?[Episode]*?[Volume]*?[END]*?[OVA]*?[OAD]*?[v\_\.\-\~0-9\s]*?[\[\(].*?([0-9]{3,4}x[0-9]{3,4}|[0-9]{3,4}[pi]).*?[\]\)]"

# Matches {Group} {Title} ~~episode_number_and_other_junk~~
# https://regex101.com/r/Pkgbu6/2
REGEX_2 = r"\[(.+?)\][\.\s\_](.+?)[\.\s\_][v\_\.\-\~0-9\s]+?[Episode]*?[Volume]*?[END]*?[OVA]*?[OAD]*?[v\_\.\-\~0-9\s]*?[\[\(].*?[\]\)]"

# Matches {Group} {Title} {Quality}
# https://regex101.com/r/qK47yd/2
REGEX_3 = r"\[(.+?)\][\.\s\_](.+?)[\.\s\_][\[\(].*?([0-9]{3,4}x[0-9]{3,4}|[0-9]{3,4}[pi]).*?[\]\)]"

# Matches {Group} {Title} ~~other_garbage_between_brackets~~
# https://regex101.com/r/f77fbz/2
REGEX_4 = r"\[(.+?)\][\.\s\_](.+?)[\.\s\_][\[\(].*?[\]\)]"

# Matches {Group} {Title} ~~other_garbage~~
# https://regex101.com/r/sUo6hF/2
REGEX_5 = r"^\[(.+?)\][\.\s\_](.+?)[\.\s\_][v\_\.\-\~0-9\s]*?$"

# Gunsmith Cats [BD.1080p] [Iznjie Biznjie], 
# Could make one more regex for this one, but nah.

def cleaner(string_):
    for f in '\/:*?"<>|':
        string_ = string_.replace(f, '')
    return(string_)

def Path(Title):
    for regexString in [REGEX_1, REGEX_2, REGEX_3, REGEX_4, REGEX_5]:
        Result = re.search(regexString, Title)
        if Result:
            groupName = Result.group(1)
            titleName = Result.group(2)

            titleName = titleName.replace('_', ' ').replace('.', ' ')
            try:
                Quality = Result.group(3)
            except IndexError:
                Quality = None
            
            if Quality:
                Quality = Result.group(3)
                if 'x' in Quality:
                    Quality = f"{Quality.split('x')[-1]}p"
                return(os.path.join(cleaner(groupName), cleaner(titleName), Quality))
            else:
                return(os.path.join(cleaner(groupName), cleaner(titleName)))
    return(None)

Filenames = os.listdir(SOURCE_FOLDER)
os.mkdir(os.path.join(DESTINATION_FOLDER, "~Unsorted"))
StartTime = time.time()

for i in range(len(Filenames)):
    print(f"Processing {Filenames[i]}")
    newPath = Path(Filenames[i])
    try:
        if newPath:
            print(f"Destination: {newPath}")
            if not os.path.exists(os.path.join(DESTINATION_FOLDER, newPath)):
                os.makedirs(os.path.join(DESTINATION_FOLDER, newPath))
            shutil.move(os.path.join(SOURCE_FOLDER, Filenames[i]), os.path.join(DESTINATION_FOLDER, newPath))
        else:
            print(f"Headed towards unsorted...")
            shutil.move(os.path.join(SOURCE_FOLDER, Filenames[i]), os.path.join(DESTINATION_FOLDER, "~Unsorted"))
    except Exception as e:
        print (f"{e} for {Filenames[i]}")
    print (f"{i + 1} of {len(Filenames)} processed!", end="\n\n")

EndTime = time.time()
print(f"Finished processing in: {EndTime - StartTime}")

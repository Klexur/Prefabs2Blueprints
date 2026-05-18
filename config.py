# Path to search for Prefab sbc files
# Use only forward slashes in the path
# Path is searched recursively so any subfolders with sbc files will be found
# Default value is the game's Prefabs folder
PREFABS_PATH = "C:/Program Files (x86)/Steam/steamapps/common/SpaceEngineers/Content/Data/Prefabs"

# Each blueprint will be put in a folder equal to the original filename
# Extra string to add to start of new blueprint names
PREFIX = "PREFAB_"

# Extra string to add to end of new blueprint names
SUFFIX = ""

# 'True' will delete the found Prefab sbc files after making the Blueprint
# 'False' will keep the found Prefab sbc files
DELETE_OLD_FILES = False

# Preview what will happen without making changes
DRY_RUN = True

# Prefabs2Blueprints
#   Converts a Space Engineers prefab to a blueprint
#   Big thanks to Keen Software House
#   P2B does not have any copyright, feel free to re-use and modify
# Please give credit to the original author Vgr

import config
import getpass
import shutil
import os

from pathlib import Path

blueprints_folder = f"C:/Users/{getpass.getuser()}/AppData/Roaming/SpaceEngineers/Blueprints/local/"
# zero-index list of exit messages (normal good exit is 0)
exit_msg = [
    "All prefabs converted successfully.",
    f'ERROR: "{config.PREFABS_PATH}" is not a folder.'
]

def main():
    warning_count = 0

    if not os.path.isdir(config.PREFABS_PATH):
        return 1

    if config.PREFABS_PATH:
        config.PREFABS_PATH = config.PREFABS_PATH.replace("/", "\\")
        if not config.PREFABS_PATH[-1:] == "\\":
            config.PREFABS_PATH += "\\"

    pycache_folder = config.PREFABS_PATH + "__pycache__"

    found_prefabs: list[str] = list()
    p = Path(config.PREFABS_PATH)
    # find all prefab files in folder recursively
    for file_path in p.rglob('**/*.sbc'):
        if file_path.is_file():
            found_prefabs.append(str(file_path))

    for prefab_file in found_prefabs:
        prefab_name = os.path.basename(prefab_file)
        prefab_folder = config.PREFIX + prefab_name[:-4] + config.SUFFIX # -4 is ".sbc"
        new_path = os.path.join(blueprints_folder, prefab_folder)
        new_file = os.path.join(new_path, "bp.sbc")

        # create new prefab folder
        if not os.path.exists(new_path):
            print(f'Creating folder "{new_path}"... ', end='')
            if config.DRY_RUN == False:
                os.mkdir(new_path)
            print('Done.') # end creating

        if not convertPrefabFile(prefab_file, new_file):
            warning_count += 1
            if os.path.exists(new_path):
                os.rmdir(new_path) # remove new prefab folder

    if os.path.exists(pycache_folder):
        shutil.rmtree(pycache_folder)
    if warning_count > 0:
        print(f'Finished with {warning_count} warning(s)')
    return 0

def convertPrefabFile(prefab_file: str, new_file: str) -> bool:
    warning_msg = ''
    try:
        print(f'Found "{prefab_file}"')
        print(f'Reading Prefab... ', end='')
        with open(prefab_file, 'r', encoding="utf-8") as file:
            file_content = file.read()
            print('Done.') # end reading
            print(f'Converting Prefab... ', end='')
            file_content = file_content.replace('Prefab', 'ShipBlueprint')
            invalidFields = ['<RespawnShip>false</RespawnShip>', '<RespawnShip>true</RespawnShip>']
            for invalid in invalidFields:
                file_content = file_content.replace(invalid, '') # remove the invalid tags
            if '<TypeId>ShipBlueprintDefinition</TypeId>' in file_content:
                file_content = file_content.replace('<TypeId>ShipBlueprintDefinition</TypeId>', '<TypeId>MyObjectBuilder_ShipBlueprintDefinition</TypeId>')
            if not('CubeGrids' in file_content):
                file_content = file_content.replace('<CubeGrid>', '<CubeGrids><CubeGrid>')
                file_content = file_content.replace('</CubeGrid>', '</CubeGrid></CubeGrids>')
            print('Done.') # end converting

        print(f'Saving Blueprint "{new_file}"... ', end='')
        if config.DRY_RUN == False:
            with open(new_file, 'w', encoding="utf-8") as file:
                file.write(file_content)
        print('Done.') # end saving

        if config.DELETE_OLD_FILES == True:
            print(f'Deleting Prefab... ', end='')
            if config.DRY_RUN == False:
                os.remove(prefab_file)
            print('Done.') # end deleting
        return True
    except UnicodeDecodeError:
        warning_msg = f'WARNING: Could not read "{prefab_file}"'
    except IndexError:
        warning_msg = f'WARNING: Could not convert "{prefab_file}"'
    except:
        warning_msg = f'WARNING: Unknown error "{prefab_file}"'

    print('Failed.') # end in-progress line
    print(warning_msg)
    if os.path.exists(new_file) and config.DRY_RUN == False:
        os.remove(new_file) # remove broken file
    return False

if __name__ == "__main__":
    print(exit_msg[main()])
    os.system("pause")

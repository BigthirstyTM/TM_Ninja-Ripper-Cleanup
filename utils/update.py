import bpy
import os
#import os.path
import shutil
import requests
import zipfile
import re
import io

from .. import bl_info
from ..utils import path
from ..utils import logs


URL_RELEASES = "https://api.github.com/repos/BigthirstyTM/TM_Ninja-Ripper-Cleanup/releases"


log = logs.get_logger(__name__)

class AddonUpdate():   
    current_addon_version:tuple = bl_info["version"]
    current_blender_version:tuple = bpy.app.version
    latest_addon_version:tuple = (0,0,0)
    latest_minimal_blender_version:tuple = (0,0,0)
    latest_is_prerelease:bool = False
    latest_filename:str = None
    latest_download_url:str = None
    
    new_addon_available:bool = False
    current_blender_supported:bool = False
    can_update: bool = False

    @classmethod
    def check_can_update(cls) :
        cls.new_addon_available = cls.latest_addon_version > cls.current_addon_version
        cls.current_blender_supported = cls.current_blender_version > cls.latest_minimal_blender_version

        log.debug(f'Addon current -> latest : {cls.current_addon_version} -> {cls.latest_addon_version}')
        log.debug(f'Blender current -> minimal : {cls.current_blender_version} -> {cls.latest_minimal_blender_version}')
        log.debug(f'{cls.latest_is_prerelease = }')
        log.debug(f'{cls.latest_filename = }')

        if cls.new_addon_available:
            log.info(f'Update available: v{cls.latest_addon_version} > {cls.current_addon_version}')
            if cls.current_blender_supported:
                cls.can_update = True
            else:
                cls.can_update = False
                log.error(f'Current blender {cls.current_blender_version} isn\'t supported ! Minimal is {cls.latest_minimal_blender_version}')
        else:
            cls.can_update = False
            log.info('No update available')


    @classmethod
    def check_for_new_release(cls):
        log.info('Checking for new release...')
        try:
            response = requests.get(URL_RELEASES)
            # Parse latest release
            latest = response.json()[0]
            latest_tag_name    = latest['tag_name']
            latest_is_prerelease = latest['prerelease']
            latest_asset = latest['assets'][0]
            latest_asset_name = latest_asset['name']
            latest_asset_download_url = latest_asset['browser_download_url']
            # Get latest addon version from github API
            # Tag name must respect the format : "v%d.%d.%d"        
            pattern = rf'^v(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)'
            match = re.search(pattern, latest_tag_name, flags=re.IGNORECASE)
            latest_addon_version = (int(match.group('major')), int(match.group('minor')), int(match.group('patch')))
            # Get latest addon blender version from the asset name
            # Asset file must always end with "%d.%d.zip"
            pattern = rf'(?P<major>\d+)\.(?P<minor>\d+)\.zip$'
            match = re.search(pattern, latest_asset_name, flags=re.IGNORECASE)
            latest_minimal_blender_version = (int(match.group('major')), int(match.group('minor')))
        except Exception as e:
            log.exception('Error during parse of release metadata')        
        else:
            # Update class attributes
            cls.latest_addon_version = latest_addon_version
            cls.latest_is_prerelease = latest_is_prerelease
            cls.latest_minimal_blender_version = latest_minimal_blender_version
            cls.latest_filename = latest_asset_name
            cls.latest_download_url = latest_asset_download_url        
        finally:
            cls.check_can_update()


    @classmethod
    def do_update(cls) -> None:
        if cls.can_update:
            log.info('Updating addon now...')
            url      = cls.latest_download_url
            addon_path = path.get_addon_dirname()
            extract_to:str = None

            if os.path.islink(addon_path):
                extract_to = path.dirname(os.readlink(addon_path))
            else:
                extract_to = path.dirname(addon_path)

            log.info(f'{addon_path = }')
            log.info(f'{extract_to = }')
            
            # try:
            #     r = requests.get(url)
            #     z = zipfile.ZipFile(io.BytesIO(r.content))

            #     shutil.rmtree(path.get_addon_dirname(), False)

            #     z.extractall(extract_to)
            #     log.info('Addon updated, blender must be restarted.')
            # except Exception as e:
            #     log.exception('Error during addon update')
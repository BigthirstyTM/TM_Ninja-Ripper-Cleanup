# TM Ninja Ripper Cleanup
Blender 3.6+ addon for Trackmania2020.

Join us on the [Blendermania discord](https://discord.gg/rP6x2838vY) to get help or share your ideas !

## Imported NR cleanup
- Clean the imported meshes from Ninja Ripper in one click...
  - Remove everything but the selected collection
  - Join all meshes inside that collection
  - Flip vertically and flip faces
  - Separate the result by materials
- Create a "cleaned route" collection with only selected meshes.

## Cleaning tools
**They all work on multiple selected objects or multiple objects in Edit Mode**

In Object Mode...
- Delete vertical faces
- Delete faces by material

In Edit Mode...
- Delete vertical faces (In the active selection)
- Delete not linked flat faces (Based on the active selection)

## Download
- [Latest release](https://github.com/BigthirstyTM/TM_Ninja-Ripper-Cleanup/releases/latest)

## Installation
1. Open blender 3.6+
2. `Edit` -> `Preferences` (top left corner)
3. Click on `Add-ons`
4. Click on `Install...`
6. Select the downloaded zip file
7. Enable the add-on `Trackmania: NR_Cleanup`

## How to
You will find the addon panel in the 3D viewport right sidebar.

You can use this addon at the very start of a blender map project.
1. Your project should be empty before importing the Ninja Ripper files
2. You can follow [this tutorial](https://www.youtube.com/watch?v=rm2u-aCrfL0&ab_channel=bmx22c) to import your map with Ninja Ripper, thanks to `bmx22c`

### Select Map Collection
1. Once it is imported, you have to find the collection that contains the textured meshes<br>
   - You can use the small button right to the collection input to collapse all collections in the outliner (or press `shift+A` when hovering in the outliner)
   - In the outliner too, you can `ctrl+left-click` on the visibility toggle of the collection to hide everything else
2. Select this collection in the addon panel, and click on the `Clean Map Collection` button
3. Depending on how you imported the NR files, you might want to disable `Flip vertically` and `Flip faces` in the popup window
4. Delete manually things that are not wanted and away from the route

### Create Route Collection
Now you have one object per material in the resulting collection.
1. Select the ones that are part of the route with `shift+left-click`
2. Click on the `Create Route Collection`
3. By default, it will hide and exclude the original collection, and unlink the objects in there so they only exist in the newly created collection. You can disable this in the popup window.
4. Now you can make use of the `Cleaning Tools` to help you with the finishing touches

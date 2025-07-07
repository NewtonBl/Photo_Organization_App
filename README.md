This project runs as a standalone .exe application built using CustomTkinter.

The application sorts files (photos in this case) based on the first 8 digit date representation. This is a standard naming format of most mobile phone photos.
The photos are sorted first into a directories by year. If a directory for the given year does not exist, one is created.
The photos are then sorted into subdirectories within the year directory based on month. Again, if the subdirectory does nto exist, one is created.

Photos that do not meet the recognized naming conventions (yyyymmdd_timestamp or Resized_yyyymmdd_timestamp) then they are sorted into a directory named "Unknown Date".

If a photo with the same name already exists in the subdirectory, the photo is instead moved into a directory titled "Potential Duplicates".

In the app, the used first clicks a button to open a file dialog window to choose the directory that the files exist in which they want to sort.
Once a directory is selected, the user simply clicks the sort button.
If sorting completes without issue, a message is displayed stating the the sorting was successfully completed.

See video for example of operation.

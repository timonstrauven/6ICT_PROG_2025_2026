# TODO: Overloop alle afbeeldingen (EN ENKEL AFBEELDINGEN) in folder.
for index, bestand in enumerate(folder_inhoud):
        if (".png" in bestand) or (".jpeg" in bestand): # We werken enkel met png- of jpg-bestanden.
       
        
         # TODO: Inladen afbeelding
         bestand_pad = f"{folder_pad}/{bestand}"
         naam, extensie = os.path.splitext(bestand)
         afbeelding = cv2.imread(bestand_pad)


# TODO: Roteer afbeelding + opslaan.
afbeelding_rot = cv2.rotate(afbeelding, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite(filename=f'YOLOdataset/verwerkt/{naam}rot_270.jpeg', img=afbeelding_rot)


# TODO: Spiegel afbeelding + opslaan.
afbeelding_spiegel = cv2.flip(afbeelding , 1)
cv2.imwrite(filename=f'YOLOdataset/verwerkt/{naam}_spiegel_hor.jpeg', img=afbeelding_spiegel)
# TODO: Filter afbeelding (liefst wazig maken) + opslaan.
afbeelding_blur = cv2.blur(afbeelding, (20, 20))
cv2.imwrite(filename=f'YOLOdataset/verwerkt/{naam}_blur.jpeg', img=afbeelding_blur)


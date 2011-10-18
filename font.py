import fontforge
import glob
import string

font = fontforge.font()
font.fontname = "panik"
font.fondname = "panik"
font.fullname = "panik"
font.familyname = "panik"

charstring = string.lowercase + string.uppercase + "01234567890"

counter = 0

for outlinefile in glob.glob ('./SoundImageFont/*.svg'):
	glyph = font.createChar (-1, charstring[counter])
	glyph.importOutlines(outlinefile)
	counter += 1 

	if counter > len(charstring):
		break
font.save ("panik.sfd")
font.generate ("panik.ttf") 

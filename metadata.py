from PIL import Image, ExifTags
from fractions import Fraction

# three values: degrees, minutes, seconds
DegMinSec = tuple[Fraction, Fraction, Fraction]

def location(path: str):
	with Image.open(path) as img:
		exif = img.getexif()
		gpsInfo = exif.get_ifd(ExifTags.IFD.GPSInfo)

		latitudeDirection = gpsInfo[ExifTags.GPS.GPSLatitudeRef] # N or S
		latitudeValues: DegMinSec = gpsInfo[ExifTags.GPS.GPSLatitude] # see DegMinSec
		longitudeDirection = gpsInfo[ExifTags.GPS.GPSLongitudeRef] # W or E
		longitudeValues: DegMinSec = gpsInfo[ExifTags.GPS.GPSLongitude] # see DegMinSec

		printCordinateResults("Latitude", latitudeDirection, latitudeValues)
		printCordinateResults("Longitude", longitudeDirection, longitudeValues)


def degMinSecToMagnitude(values: DegMinSec) -> float:
	return round(values[0] + values[1]/60.0 + values[2]/3600.0, 4)

def formatDegMinSec(values: DegMinSec) -> str:
	deg = int(values[0])
	minute = int(values[1])
	sec = float(round(values[2], 2))
	return f'{deg}° {minute}′ {sec}″'


def printCordinateResults(name: str, direction: str, values: DegMinSec):
	degMinSec = formatDegMinSec(values)
	magnitude = degMinSecToMagnitude(values)
	print(f'{name}: {degMinSec}{direction} ({magnitude}°{direction})')
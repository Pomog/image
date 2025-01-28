import argparse
import steg
import metadata

parser = argparse.ArgumentParser()
parser.add_argument("-map", action="store_true",
					help="print the location from metadata")
parser.add_argument("-steg", action="store_true",
					help="print the message hidden file in the image")
parser.add_argument("image",
					help="the target image")
args = parser.parse_args()

if not args.map and not args.steg:
	print("no flags given\n")
	parser.print_help()
	exit(1)

imgPath = args.image

if args.steg:
	print(steg.findPGPKey(imgPath))

# looks a little nicer /shrug
if args.map and args.steg:
	print("")

if args.map:
	metadata.location(imgPath)


# the PGP key is hidden right at the end of the file in ascii, presumably where jpeg will no longer read at
def findPGPKey(path: str) -> str:
	with open(path, "rb") as img:
		fileContents = img.read()
		
		startArmour = b'-----BEGIN PGP PUBLIC KEY BLOCK-----'
		endArmour = b'-----END PGP PUBLIC KEY BLOCK-----'

		start_index = fileContents.find(startArmour)
		end_index = fileContents.find(endArmour)
		if (start_index == -1 or end_index == -1):
			raise Exception("did not find start or end armour in file")
		
		# want to read the full text, so to the end of the end armour, cant do it above because we need to check whether we found it at all
		end_index += len(endArmour)

		# read key
		result = fileContents[start_index:end_index]
		return result.decode()

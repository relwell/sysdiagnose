import struct

data = -9129941306809768153
data = int(data)

logger.info("Big endian -> Little endian")
ba = (data).to_bytes(64, byteorder='big', signed=True)

# print hex
logger.info("Hex view:")
logger.info(ba)
logger.info("")

# convert back to int
ls = int.from_bytes(ba, byteorder="little", signed=True)
logger.info("Little Endian / Signed: %d" % ls)

lu = int.from_bytes(ba, byteorder="little", signed=False)
logger.info("Little Endian / Unsigned: %d" % lu)

bs = int.from_bytes(ba, byteorder="big", signed=True)
logger.info("Little Endian / Signed: %d" % bs)

bu = int.from_bytes(ba, byteorder="big", signed=False)
logger.info("Little Endian / Unsigned: %d" % bu)

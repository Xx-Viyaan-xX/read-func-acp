reading = open("condingal.txt", "r")
print(reading.readline())
reading.close()

writer = open("condingal.txt", "w")
writer.write("\nlodha, 12\n")
writer.close()

writer = open("condingal.txt", "a")
writer.write("\nishaan, 12\n")
writer.close()
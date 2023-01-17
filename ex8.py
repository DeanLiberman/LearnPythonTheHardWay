formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
     "I had this thing.",
     "That you could type up right.",
     "But it didn't sing.",
     # Hm. What happened to the song in Cross Realms? Of course Sabarene's songs are still preserved, but what happened to the more mythological geeky songs? Oh yeah more importantly, I need to figure out why "But it didn't sing" is rendered in double quotation marks rather than single quotation marks.
     "So I said goodnight."
     
     )

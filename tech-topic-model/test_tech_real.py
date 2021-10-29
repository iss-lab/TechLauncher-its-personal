import spacy
nlp = spacy.load("versions_and_results/v1/training/model-best")

test_r1 = nlp("A Linux 4.5-rc1 Kernel With AMDGPU PowerPlay Enabled For Ubuntu Systems")
print(test_r1.cats['RELEVANT'])
if test_r1.cats['RELEVANT'] > 0.95:
   print("r1 is relevant")
else:
   print("r1 is irrelevant")

test_r2=nlp("Microsoft Blocks Linux Game Port From Happening")
print(test_r2.cats['RELEVANT'])
if test_r2.cats['RELEVANT'] > 0.95:
   print("r2 is relevant")
else:
   print("r2 is irrelevant")

test_r3=nlp("More Details On The Do-It-Yourself ARM64 Laptop")
print(test_r3.cats['RELEVANT'])
if test_r3.cats['RELEVANT'] > 0.95:
   print("r3 is relevant")
else:
   print("r3 is irrelevant")

test_r4=nlp("Intel Is Very Close With Tessellation Shaders For Mesa")
print(test_r4.cats['RELEVANT'])
if test_r4.cats['RELEVANT'] > 0.95:
   print("r4 is relevant")
else:
   print("r4 is irrelevant")

test_r5=nlp("QEMU 2.5 Released With The VirtIO GPU 3D Support")
print(test_r5.cats['RELEVANT'])
if test_r5.cats['RELEVANT'] > 0.95:
   print("r5 is relevant")
else:
   print("r5 is irrelevant")

test_r6=nlp("FreeBSD-Powered Firewall Distro OPNsense 16.1 Released")
print(test_r6.cats['RELEVANT'])
if test_r6.cats['RELEVANT'] > 0.95:
   print("r6 is relevant")
else:
   print("r6 is irrelevant")

test_r7=nlp("Parallel Query Support Coming To PostgreSQL 9.6")
print(test_r7.cats['RELEVANT'])
if test_r7.cats['RELEVANT'] > 0.95:
   print("r7 is relevant")
else:
   print("r7 is irrelevant")

test_r8=nlp("OpenBSD Sucks? Thoughts From One Of Their Developers")
print(test_r8.cats['RELEVANT'])
if test_r8.cats['RELEVANT'] > 0.95:
   print("r8 is relevant")
else:
   print("r8 is irrelevant")

test_r9=nlp("Primary Selection Support Still Being Worked On For Wayland")
print(test_r9.cats['RELEVANT'])
if test_r9.cats['RELEVANT'] > 0.95:
   print("r9 is relevant")
else:
   print("r9 is irrelevant")

test_r10=nlp("Mining Monero On The CPU & Ethereum On The GPU")
print(test_r10.cats['RELEVANT'])
if test_r10.cats['RELEVANT'] > 0.95:
   print("r10 is relevant")
else:
   print("r10 is irrelevant")



test_r1 = nlp("The Blockers For GTK4: Constraint-Based Layout, Finished OpenGL Renderer & More")
print(test_r1.cats['RELEVANT'])
if test_r1.cats['RELEVANT'] > 0.95:
   print("r1 is relevant")
else:
   print("r1 is irrelevant")

test_r2=nlp("The First Alpha Of Debian 10 Buster Installer")
print(test_r2.cats['RELEVANT'])
if test_r2.cats['RELEVANT'] > 0.95:
   print("r2 is relevant")
else:
   print("r2 is irrelevant")

test_r3=nlp("Better Half-Tiling Support Lands For Mutter 3.26.1 & GTK3")
print(test_r3.cats['RELEVANT'])
if test_r3.cats['RELEVANT'] > 0.95:
   print("r3 is relevant")
else:
   print("r3 is irrelevant")

test_r4=nlp("Calamares 3.2 Linux Installer Working On Wayland Support")
print(test_r4.cats['RELEVANT'])
if test_r4.cats['RELEVANT'] > 0.95:
   print("r4 is relevant")
else:
   print("r4 is irrelevant")

test_r5=nlp("A Binary Snapshot Of Qt 5.10 To Begin Testing This Next Toolkit Update")
print(test_r5.cats['RELEVANT'])
if test_r5.cats['RELEVANT'] > 0.95:
   print("r5 is relevant")
else:
   print("r5 is irrelevant")

test_r6=nlp("Firefox 55 Is Ready To Shine With Performance Improvements")
print(test_r6.cats['RELEVANT'])
if test_r6.cats['RELEVANT'] > 0.95:
   print("r6 is relevant")
else:
   print("r6 is irrelevant")

test_r7=nlp("Fedora 27 Enters Its Beta Freeze")
print(test_r7.cats['RELEVANT'])
if test_r7.cats['RELEVANT'] > 0.95:
   print("r7 is relevant")
else:
   print("r7 is irrelevant")

test_r8=nlp("RISC-V Linux Port Pursuing Mainlining In The Kernel")
print(test_r8.cats['RELEVANT'])
if test_r8.cats['RELEVANT'] > 0.95:
   print("r8 is relevant")
else:
   print("r8 is irrelevant")

test_r9=nlp("DRM Graphics Driver Comes For Dove/Cubox")
print(test_r9.cats['RELEVANT'])
if test_r9.cats['RELEVANT'] > 0.95:
   print("r9 is relevant")
else:
   print("r9 is irrelevant")

test_r10=nlp("Allwinner A80 Octa-Core Hardware Coming Next Month")
print(test_r10.cats['RELEVANT'])
if test_r10.cats['RELEVANT'] > 0.95:
   print("r10 is relevant")
else:
   print("r10 is irrelevant")











test_i1=nlp("15 Popular Travel Destinations You Should Avoid In The Summer")
print(test_i1.cats['RELEVANT'])
if test_i1.cats['RELEVANT'] > 0.95:
   print("i1 is relevant")
else:
   print("i1 is irrelevant")

test_i2=nlp("'Before You Call The Cops' On Him, Watch His Powerful Monologue On Racism")
print(test_i2.cats['RELEVANT'])
if test_i2.cats['RELEVANT'] > 0.95:
   print("i2 is relevant")
else:
   print("i2 is irrelevant")

test_i3=nlp("Hospice Overdosed Patients To 'Hasten Their Deaths")
print(test_i3.cats['RELEVANT'])
if test_i3.cats['RELEVANT'] > 0.95:
   print("i3 is relevant")
else:
   print("i3 is irrelevant")

test_i4=nlp("Fearless Body Image: Lessons From The Mermaid Parade (PHOTOS, VIDEO)")
print(test_i4.cats['RELEVANT'])
if test_i4.cats['RELEVANT'] > 0.95:
   print("i4 is relevant")
else:
   print("i4 is irrelevant")

test_i5=nlp("It Is Possible to Fix Your Credit in Two Months")
print(test_i5.cats['RELEVANT'])
if test_i5.cats['RELEVANT'] > 0.95:
   print("i5 is relevant")
else:
   print("i5 is irrelevant")

test_i6=nlp("Freeze Fresh Food: 6 Secrets To Make Healthy Picks Last Longer")
print(test_i6.cats['RELEVANT'])
if test_i6.cats['RELEVANT'] > 0.95:
   print("i6 is relevant")
else:
   print("i6 is irrelevant")

test_i7=nlp("Craft Of The Day: Get Festive  With This Fourth of July Decoration")
print(test_i7.cats['RELEVANT'])
if test_i7.cats['RELEVANT'] > 0.95:
   print("i7 is relevant")
else:
   print("i7 is irrelevant")

test_i8=nlp("The 9 Most Brilliant Pieces Of Comedy Hiding On YouTube")
print(test_i8.cats['RELEVANT'])
if test_i8.cats['RELEVANT'] > 0.95:
   print("i8 is relevant")
else:
   print("i8 is irrelevant")

test_i9=nlp("Andrew Garfield And Emma Stone Tackle 'Spider-Man'")
print(test_i9.cats['RELEVANT'])
if test_i9.cats['RELEVANT'] > 0.95:
   print("i9 is relevant")
else:
   print("i9 is irrelevant")

test_i10=nlp("Celebrity Divorce: Who Is Your Celebrity Divorce Role Model?")
print(test_i10.cats['RELEVANT'])
if test_i10.cats['RELEVANT'] > 0.95:
   print("i10 is relevant")
else:
   print("i10 is irrelevant")





test_i1=nlp("Zach Huston, Victim of Brutal Ohio School Bullying, Tells His Story")
print(test_i1.cats['RELEVANT'])
if test_i1.cats['RELEVANT'] > 0.95:
   print("i1 is relevant")
else:
   print("i1 is irrelevant")

test_i2=nlp("Super Bowl 2012: Organic Beers For The Big Game")
print(test_i2.cats['RELEVANT'])
if test_i2.cats['RELEVANT'] > 0.95:
   print("i2 is relevant")
else:
   print("i2 is irrelevant")

test_i3=nlp("Duncan Niederauer, NYSE CEO: 'Mega-Mergers' Unlikely In Near Future")
print(test_i3.cats['RELEVANT'])
if test_i3.cats['RELEVANT'] > 0.95:
   print("i3 is relevant")
else:
   print("i3 is irrelevant")

test_i4=nlp("The Joy of Reading Can Take You So Many Places: A Chat With Gayle King")
print(test_i4.cats['RELEVANT'])
if test_i4.cats['RELEVANT'] > 0.95:
   print("i4 is relevant")
else:
   print("i4 is irrelevant")

test_i5=nlp("The Art Of Not Making' Explores The Intentions And Effects Of The New Artist/Artisan Relationship")
print(test_i5.cats['RELEVANT'])
if test_i5.cats['RELEVANT'] > 0.95:
   print("i5 is relevant")
else:
   print("i5 is irrelevant")

test_i6=nlp("Sperry and Milly Team Up: These Aren't Your Dad's Boat-Shoes")
print(test_i6.cats['RELEVANT'])
if test_i6.cats['RELEVANT'] > 0.95:
   print("i6 is relevant")
else:
   print("i6 is irrelevant")

test_i7=nlp("Mysterious Illness at Le Roy School: Understanding Conversion Disorders")
print(test_i7.cats['RELEVANT'])
if test_i7.cats['RELEVANT'] > 0.95:
   print("i7 is relevant")
else:
   print("i7 is irrelevant")

test_i8=nlp("Madonna Looks Stylish As She Preps For Her Super Bowl Sunday Performance")
print(test_i8.cats['RELEVANT'])
if test_i8.cats['RELEVANT'] > 0.95:
   print("i8 is relevant")
else:
   print("i8 is irrelevant")

test_i9=nlp("Toxic Sugar: Should We Regulate It Like Alcohol?'")
print(test_i9.cats['RELEVANT'])
if test_i9.cats['RELEVANT'] > 0.95:
   print("i9 is relevant")
else:
   print("i9 is irrelevant")

test_i10=nlp("Depression in the Workplace: Don't Ask, Don't Tell?")
print(test_i10.cats['RELEVANT'])
if test_i10.cats['RELEVANT'] > 0.95:
   print("i10 is relevant")
else:
   print("i10 is irrelevant")


   

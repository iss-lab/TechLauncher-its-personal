import spacy
nlp = spacy.load("versions_and_results/v5/training/model-best")

test_r1 = nlp("Kevin Durant, Thunder send Lakers to sixth loss in row")
print(test_r1.cats['RELEVANT'])
if test_r1.cats['RELEVANT'] > 0.95:
   print("r1 is relevant")
else:
   print("r1 is irrelevant")

test_r2=nlp("Australia's Tomic wins first ATP title at Sydney")
print(test_r2.cats['RELEVANT'])
if test_r2.cats['RELEVANT'] > 0.95:
   print("r2 is relevant")
else:
   print("r2 is irrelevant")

test_r3=nlp("Tennis Channel Court Report 01.12.12")
print(test_r3.cats['RELEVANT'])
if test_r3.cats['RELEVANT'] > 0.95:
   print("r3 is relevant")
else:
   print("r3 is irrelevant")

test_r4=nlp("J.J. Redick's big three helps Magic shock host Clippers")
print(test_r4.cats['RELEVANT'])
if test_r4.cats['RELEVANT'] > 0.95:
   print("r4 is relevant")
else:
   print("r4 is irrelevant")

test_r5=nlp("The good and bad of Twitter and college athletes")
print(test_r5.cats['RELEVANT'])
if test_r5.cats['RELEVANT'] > 0.95:
   print("r5 is relevant")
else:
   print("r5 is irrelevant")

test_r6=nlp("Tokyo opens 2020 Olympic bid campaign in London")
print(test_r6.cats['RELEVANT'])
if test_r6.cats['RELEVANT'] > 0.95:
   print("r6 is relevant")
else:
   print("r6 is irrelevant")

test_r7=nlp("Tina Maze wins super-G; Lindsey Vonn is fourth")
print(test_r7.cats['RELEVANT'])
if test_r7.cats['RELEVANT'] > 0.95:
   print("r7 is relevant")
else:
   print("r7 is irrelevant")

test_r8=nlp("Mediation will address U.S. speedskaters")
print(test_r8.cats['RELEVANT'])
if test_r8.cats['RELEVANT'] > 0.95:
   print("r8 is relevant")
else:
   print("r8 is irrelevant")

test_r9=nlp("USA's Madison Keys still growing into her big game")
print(test_r9.cats['RELEVANT'])
if test_r9.cats['RELEVANT'] > 0.95:
   print("r9 is relevant")
else:
   print("r9 is irrelevant")

test_r10=nlp("Suns finally get 2,000th win with upset of Bulls")
print(test_r10.cats['RELEVANT'])
if test_r10.cats['RELEVANT'] > 0.95:
   print("r10 is relevant")
else:
   print("r10 is irrelevant")



print("----------------------------------------")


test_r1 = nlp("Stephen Curry tops Damian Lillard as Warriors beat Blazers")
print(test_r1.cats['RELEVANT'])
if test_r1.cats['RELEVANT'] > 0.95:
   print("r1 is relevant")
else:
   print("r1 is irrelevant")

test_r2=nlp("Ivan Lendl still a physical specimen at 52")
print(test_r2.cats['RELEVANT'])
if test_r2.cats['RELEVANT'] > 0.95:
   print("r2 is relevant")
else:
   print("r2 is irrelevant")

test_r3=nlp("John Wall's return powers Wizards to upset of Hawks")
print(test_r3.cats['RELEVANT'])
if test_r3.cats['RELEVANT'] > 0.95:
   print("r3 is relevant")
else:
   print("r3 is irrelevant")

test_r4=nlp("David West posts triple-double as hot Pacers top Bobcats")
print(test_r4.cats['RELEVANT'])
if test_r4.cats['RELEVANT'] > 0.95:
   print("r4 is relevant")
else:
   print("r4 is irrelevant")

test_r5=nlp("Begay joins NBC, Golf Channel as reporter")
print(test_r5.cats['RELEVANT'])
if test_r5.cats['RELEVANT'] > 0.95:
   print("r5 is relevant")
else:
   print("r5 is irrelevant")

test_r6=nlp("Joking aside, No. 1 Djokovic hopes to make history")
print(test_r6.cats['RELEVANT'])
if test_r6.cats['RELEVANT'] > 0.95:
   print("r6 is relevant")
else:
   print("r6 is irrelevant")

test_r7=nlp("Troubled Tomic talks about his ups and downs")
print(test_r7.cats['RELEVANT'])
if test_r7.cats['RELEVANT'] > 0.95:
   print("r7 is relevant")
else:
   print("r7 is irrelevant")

test_r8=nlp("Oosthuizen shoots 66 to win Volvo Champions\n")
print(test_r8.cats['RELEVANT'])
if test_r8.cats['RELEVANT'] > 0.95:
   print("r8 is relevant")
else:
   print("r8 is irrelevant")

test_r9=nlp("Kazakhstan quickly lands on tennis map")
print(test_r9.cats['RELEVANT'])
if test_r9.cats['RELEVANT'] > 0.95:
   print("r9 is relevant")
else:
   print("r9 is irrelevant")

test_r10=nlp("Marcel Hirscher wins slalom, adds to World Cup lead")
print(test_r10.cats['RELEVANT'])
if test_r10.cats['RELEVANT'] > 0.95:
   print("r10 is relevant")
else:
   print("r10 is irrelevant")



print("----------------------------------------")






test_i1=nlp("Trump's Crackdown On Immigrant Parents Puts More Kids In An Already Strained System")
print(test_i1.cats['RELEVANT'])
if test_i1.cats['RELEVANT'] > 0.95:
   print("i1 is relevant")
else:
   print("i1 is irrelevant")

test_i2=nlp("Ryan Zinke Looks To Reel Back Some Critics With 'Grand Pivot' To Conservation")
print(test_i2.cats['RELEVANT'])
if test_i2.cats['RELEVANT'] > 0.95:
   print("i2 is relevant")
else:
   print("i2 is irrelevant")

test_i3=nlp("In Historic Victory, Barbados Elects First Female Prime Minister")
print(test_i3.cats['RELEVANT'])
if test_i3.cats['RELEVANT'] > 0.95:
   print("i3 is relevant")
else:
   print("i3 is irrelevant")

test_i4=nlp("2 People Injured In Indiana School Shooting")
print(test_i4.cats['RELEVANT'])
if test_i4.cats['RELEVANT'] > 0.95:
   print("i4 is relevant")
else:
   print("i4 is irrelevant")

test_i5=nlp("The 20 Funniest Tweets From Women This Week")
print(test_i5.cats['RELEVANT'])
if test_i5.cats['RELEVANT'] > 0.95:
   print("i5 is relevant")
else:
   print("i5 is irrelevant")

test_i6=nlp("Fish Market Buys Freedom For Fred The 70-Pound Octopus")
print(test_i6.cats['RELEVANT'])
if test_i6.cats['RELEVANT'] > 0.95:
   print("i6 is relevant")
else:
   print("i6 is irrelevant")

test_i7=nlp("North Korea Demolishes Tunnels At Nuclear Test Site, Reports Say")
print(test_i7.cats['RELEVANT'])
if test_i7.cats['RELEVANT'] > 0.95:
   print("i7 is relevant")
else:
   print("i7 is irrelevant")

test_i8=nlp("'Late Night' Writer's Breathless Royal Wedding Recap Is The Only One You Need")
print(test_i8.cats['RELEVANT'])
if test_i8.cats['RELEVANT'] > 0.95:
   print("i8 is relevant")
else:
   print("i8 is irrelevant")

test_i9=nlp("Guatemala Syphilis Study Lawsuit: Dismissal Despite United States Experiments On Natives In 1940s")
print(test_i9.cats['RELEVANT'])
if test_i9.cats['RELEVANT'] > 0.95:
   print("i9 is relevant")
else:
   print("i9 is irrelevant")

test_i10=nlp("Rescue Cat Has Hilarious Wide-Eyed Expression After Scan Confirms She Is Pregnant")
print(test_i10.cats['RELEVANT'])
if test_i10.cats['RELEVANT'] > 0.95:
   print("i10 is relevant")
else:
   print("i10 is irrelevant")



   print("----------------------------------------")






test_i1=nlp("European Cold Snap Freezes Venice, Berlin and Other Destinations")
print(test_i1.cats['RELEVANT'])
if test_i1.cats['RELEVANT'] > 0.95:
   print("i1 is relevant")
else:
   print("i1 is irrelevant")

test_i2=nlp("5 Parenting Strategies That Work")
print(test_i2.cats['RELEVANT'])
if test_i2.cats['RELEVANT'] > 0.95:
   print("i2 is relevant")
else:
   print("i2 is irrelevant")

test_i3=nlp("James Franco Directs New Ads For Seven For All Mankind")
print(test_i3.cats['RELEVANT'])
if test_i3.cats['RELEVANT'] > 0.95:
   print("i3 is relevant")
else:
   print("i3 is irrelevant")

test_i4=nlp("Marlon Brando Couch Lawsuit: Furniture Company Sued For Using Actor's Name")
print(test_i4.cats['RELEVANT'])
if test_i4.cats['RELEVANT'] > 0.95:
   print("i4 is relevant")
else:
   print("i4 is irrelevant")

test_i5=nlp("The Six Personal Traits That Help Women Successfully Survive Divorce")
print(test_i5.cats['RELEVANT'])
if test_i5.cats['RELEVANT'] > 0.95:
   print("i5 is relevant")
else:
   print("i5 is irrelevant")

test_i6=nlp("Mortgage Deal Reached In 2008 Shows Pitfalls To Avoid In Current Settlement")
print(test_i6.cats['RELEVANT'])
if test_i6.cats['RELEVANT'] > 0.95:
   print("i6 is relevant")
else:
   print("i6 is irrelevant")

test_i7=nlp("Green Tea Could Help Functioning In Old Age: Study")
print(test_i7.cats['RELEVANT'])
if test_i7.cats['RELEVANT'] > 0.95:
   print("i7 is relevant")
else:
   print("i7 is irrelevant")

test_i8=nlp("'Mouse in the House: What a Rodent Problem Can Reveal")
print(test_i8.cats['RELEVANT'])
if test_i8.cats['RELEVANT'] > 0.95:
   print("i8 is relevant")
else:
   print("i8 is irrelevant")

test_i9=nlp("Louis Vuitton's Merry-Go-Round Strap Mule: Object Of My Affection")
print(test_i9.cats['RELEVANT'])
if test_i9.cats['RELEVANT'] > 0.95:
   print("i9 is relevant")
else:
   print("i9 is irrelevant")

test_i10=nlp("Heart Disease: 17 Celebrities With Heart Problems")
print(test_i10.cats['RELEVANT'])
if test_i10.cats['RELEVANT'] > 0.95:
   print("i10 is relevant")
else:
   print("i10 is irrelevant")



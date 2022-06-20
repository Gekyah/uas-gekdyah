maks = 5
limit=maks;
for bintang in range (0,maks):
    for pola in range (0, limit+1):
        print("   ",end="")

    for bentuk in range (0,bintang+1):
        print(" * ",end="")
    limit-=1
    print("")
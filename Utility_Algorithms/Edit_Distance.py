def edit_distance(str1, str2):
    # dynamic programming
    len1, len2 = len(str1), len(str2)
    dp = [[0 for x in range(len2 + 1)] for y in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                dp[i][j] = j
                
            elif j == 0:
                dp[i][j] = i 
            
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            

            else:
                dp[i][j] = 1 + min(dp[i][j-1],       # Insert
                                   dp[i-1][j],       # Remove
                                   dp[i-1][j-1])     # Replace
    
    return dp[len1][len2]

#test:
str1 = "sunday"
str2 = "saturday"
print("Edit distance:", edit_distance(str1, str2))

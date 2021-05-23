#Following example requires at minimum the number of citations of each publication of one or more authors

#Create the H-index column
df['H-index'] = ""
#Create the list for citations
citation_list = []
#Create list for h-index scores
h_index = []
#Loop through each row in the dataframe
for i, row in enumerate(df.itertuples(), 0):
    #Split the Cites column of each row by semicolon and save it as a list
    citation_list = df['Cites'][i].split(";")
    #Convert the list data from str to int (optional)
    citation_list = list(map(int, citation_list))
    #Calculate the h-index
    h_index = sum(x >= i + 1 for i, x in enumerate(sorted(  list(citation_list), reverse=True)))
    #Append the calculated h-index to the h-index column
    df['H-index'][i] = h_index
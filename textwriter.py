class TextWriter:

    def writeMoviesToFile(self,file_name,movies):
        with open(file_name,'w') as movies_file:
            for movie in movies:
                movies_file.writelines(f"{movie['Rank']} || {movie['Title']} || {movie['Year']} || {movie['Rating']} \n")

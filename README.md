# PyMovieI
PyMovieI is a Python package which has a PyMovieInfo library for fetching  movie informations and poster
it works on web scarping and it fetches the data from Wikipedia.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyMovieI.

```bash
pip install PyMovieI
```

## Usage

```python
from PyMovieI import PyMovieInfo

MovieObj=PyMovieInfo('Movie_Name') # Create Objects of  'PyMovieInfo'

```


## getPoster() 
getPoster(name=None,path="") Method 'downloads' Movie Poster and you can rename it  as name argumnet passed in method and save it to specific location by providing location as argument in path. 

## Examples :

```python
from PyMovieI import PyMovieInfo

MovieObj=PyMovieInfo('Venom') # Create Objects of  'PyMovieInfo'
MovieObj.getPoster() #it will download poster in current location and save with the name available on wikipedida(from where data has been fecthed) 
MovieObj.getPoster("My Movie") # it will download poster as My_Movie.jpg or My_Movie.png 
MovieObj.getPoster(path="D:\\posters\\") # it will download poster in D drive posters directory

```


## movie_info 
movie_info is attribute of PyMovieInfo class's Object it returns dictionary having  movie information in it as title, starring, directed_by, budget, etc.
## Examples:
```python
from PyMovieI import PyMovieInfo

MovieObj=PyMovieInfo('Venom') # Create Objects of  
MovieObj.movie_info # Returns dictionary having 
{'Title': ['Venom'], 'Directed by': ['Ruben Fleischer'],
 'Produced by': ['Avi Arad', 'Matt Tolmach', 'Amy Pascal'], 
 'Screenplay by': ['Jeff Pinkner', 'Scott Rosenberg', 'Kelly Marcel'],
 'Story by': ['Jeff Pinkner', 'Scott Rosenberg'], 
 'Based on': ['Todd McFarlane', 'David Michelinie'], 'Starring': ['Tom Hardy', 'Michelle Williams', 
 'Riz Ahmed', 'Scott Haze', 'Reid Scott'], 'Music by': ['Ludwig Göransson'], 
 'Cinematography': ['Matthew Libatique'], 'Edited by': ['Maryann Brandon', 'Alan Baumgarten'],
 'Production company': ['Columbia Pictures', 'Marvel Entertainment', 'Tencent Pictures', 'Arad Productions', 'Matt Tolmach Productions', 'Pascal Pictures'],
 'Distributed by': ['Sony Pictures Releasing'], 
 'Release date': [datetime.datetime(2018, 10, 1, 0, 0)], 'Running time': [112], 'Country': ['United States'], 
 'Language': ['English'],
 'Budget': [{'ammount': 100000000.0, 'currency': '$'}], 
 'Box office': [{'ammount': 856100000.0, 'currency': '$'}]}
```
## title
title is an attribute of PyMovieInfo class's Object it returns list of movie title.

## Examples:

```python
from PyMovieI import PyMovieInfo

MovieObj=PyMovieInfo('Venom') # Create Objects of  'PyMovieInfo'
print(MovieObj.title[0]) # will print movie title(output:"Venom")

```

## running_time
running_time is attribute of PyMovieInfo class's object it returns list having movie's running time in minutes.

## Examples:

```python
from PyMovieI import PyMovieInfo

MovieObj=PyMovieInfo('Venom') # Creates Object of  'PyMovieInfo'
print(MovieObj.running_time[0]) # will print movie running time in minutes(output:"112")

```
## starring
starring is attribute of PyMovieInfo class's Object it returns list of movie cast

## Examples:

```python
from PyMovieI import PyMovieInfo

MovieObj=PyMovieInfo('Venom') # Creates Object of  'PyMovieInfo'
print(MovieObj.starring) # will print movie starring cast's names(output:['Tom Hardy', 'Michelle Williams', 'Riz Ahmed', 'Scott Haze', 'Reid Scott'])

```

## directed_by
directed_by is an attribute of PyMovieInfo class's object it returns list having director names

## Examples:

```python
from PyMovieI import PyMovieInfo

MovieObj=PyMovieInfo('Venom') # Create Objects of  'PyMovieInfo'
print(MovieObj.directed_by) # will print movie directer's names(output:['Ruben Fleischer'])

```

## release_date
release_date is an attribute of PyMovieInfo class's object it returns list having release dates(object).

## Examples:

```python
from PyMovieI import PyMovieInfo

MovieObj=PyMovieInfo('Venom') # Create Objects of  'PyMovieInfo'
print(MovieObj.release_date) # will print (output:[datetime.datetime(2018, 10, 1, 0, 0)])

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what would you like to change in package PyMovieI.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
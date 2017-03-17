# entertainment_center

`entertainment_center` helps you to save your favorite movies and their relevant details including title, year of production, poster, and official movie trailer. `entertainment_center` uses a Python module called `fresh_tomatoes.py` to generate a webpage that displays your saved favorite movies.

If you want to know more about `fresh_tomatoes` Python module, see [fresh_tomatoes](https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py).

# Documentation

The information related to supported python version, how to get started, and license is included in this documentation.

- [Supported Python versions](#supported-python-versions)
- [Quick start](#quick-start)
  - [Usage from Windows Command line](#usage-from-windows-command-line)
     - [Command line example](#command-line-example)
  - [Add your favorite movies](#add-your-favorite-movies)
- [What is included](#what-is-included)
- [License](#license)


## Supported Python versions

The entertainment_center basically supports Python 2.x.

## Quick start

### Usage from Windows Command line

To view the default favorite movies website in your browser:

1. Download the [project's files](https://github.com/ahmadnagib/entertainment_center) and put them together in one folder. 
2. Make sure that Python 2.x is added to your Windows environment variables.
3. Open the command line and navigate to the folder's path.
4. Run the command:
```
python entertainment_center.py
```
or
```
py entertainment_center.py
```
or
```
entertainment_center.py
```
5. The default favorite movies web site should be opened in your default web browser.

#### Command Line example

```
folder_path\entertainment_center-master>py entertainment_center.py
```

### Add your favorite movies

To add your customized favorite movies instead of my default favorite movies:
1. Open `entertainment_center.py` file with any text editor.
2. Replace the instances found in the file with the instance of your own. They should look like:
```
your_favorite_movie = media.Movie("Movie Title", "Production Year",
                                  "Poster Image URL","Movie Trailer URL")
```
3. Replace the intances names in the `movies_list` with the names of the newly added instances in the order that you want the movies to be shown in the website.

## What is included

Within the download you will find the following files:

```
entertainment_center-master/
├── entertainment_center.py
├── media.py
├── fresh_tomatoes.py
├── README.md
├── LICENSE
```

## License

entertainment_center.py is Copyright © 2017 Ahmad Nagib. It is free software, and may be redistributed under the terms specified in the [LICENSE](/LICENSE) file.

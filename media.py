class Movie():
    """
    This class is created as a way to store movie-related information
    including movie title, year of production, poster image URL,
    and movie trailer URL.
    """

    def __init__(self, title, year, poster_image_url, trailer_youtube_url):
        """
        This function creates a movie instance that holds the passed details.

        Args:
        title: The title of the movie.
        year: The year of production of the movie.
        poster_image_url: The link to the  movie's official poster.
        trailer_youtube_url: The link to the movie's youtube trailer.
        """

        self.title = title
        self.year = year
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

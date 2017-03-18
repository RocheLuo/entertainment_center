import media
import fresh_tomatoes


# Create Movie instances to store favorite movies information
forrest_gump = media.Movie("Forrest Gump", "1994",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

you_ve_got_mail = media.Movie("You've Got Mail", "1998",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BZTcxNzgzZjMtYzZiZC00MmE1LTg3MzQtZDAxMTYyZWE4MDNhL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=bjP4s7UUnK8")

the_aviator = media.Movie("The Aviator", "2004",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BZTYzMjA2M2EtYmY1OC00ZWMxLThlY2YtZGI3MTQzOWM4YjE3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=FebPJlmgldE")

catch_me_if_u_can = media.Movie("Catch Me If You Can", "2002",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY5MzYzNjc5NV5BMl5BanBnXkFtZTYwNTUyNTc2._V1_.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=71rDQ7z4eFg")

inception = media.Movie("Inception", "2010",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=hstBN0Qkqhc")

captain_phillips = media.Movie("Captain Phillips", "2013",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQzNzExMDg3Ml5BMl5BanBnXkFtZTgwODU1NzEzMDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                               "http://www.youtube.com/watch?v=GEyM01dAxp8")

the_terminal = media.Movie("The Terminal", "2004",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM1MTIwNTMxOF5BMl5BanBnXkFtZTcwNjIxMjQyMw@@._V1_SY1000_CR0,0,737,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=GZjC9dAvWuU")

talented_mr_ripley = media.Movie("The Talented Mr. Ripley", "1999",
                                 "https://images-na.ssl-images-amazon.com/images/M/MV5BODA3NDhiZjYtYTk2NS00ZWYwLTljYTQtMjU0NzcyMGEzNTU2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,672,1000_AL_.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=Ylc5ToQoLg0")

this_boys_life = media.Movie("This Boy's Life", "1993",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BODA5ZTBjNjktZTc0OS00Yjc5LWJiNzUtYmRhYjVkYTI4MWExL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=P28qmkCrNSM")


# Group movies instances in a list to pass them to open_movies_page() function
movies_list = [you_ve_got_mail, the_aviator, catch_me_if_u_can, inception,
               forrest_gump, captain_phillips, the_terminal,
               talented_mr_ripley, this_boys_life]


# Generate an HTML file producing a website showcasing my favorite movies
fresh_tomatoes.open_movies_page(movies_list)

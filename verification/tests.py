TESTS = {
    "Basic": [
        {
            "input": (('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                       'German-coffee', 'beer-white', 'cat-water',
                       'horse-2', 'milk-3', '4-Rothmans',
                       'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                       'bird-Brit', '4-green', 'Winfield-beer',
                       'Dane-blue', '5-dog', 'blue-horse',
                       'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                      'fish-color'),
            "answer": 'green',
        },
        {
            "input": (('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                       'German-coffee', 'beer-white', 'cat-water',
                       'horse-2', 'milk-3', '4-Rothmans',
                       'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                       'bird-Brit', '4-green', 'Winfield-beer',
                       'Dane-blue', '5-dog', 'blue-horse',
                       'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                      'tea-number'),
            "answer": '2',
        },
        {
            "input": (('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                       'German-coffee', 'beer-white', 'cat-water',
                       'horse-2', 'milk-3', '4-Rothmans',
                       'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                       'bird-Brit', '4-green', 'Winfield-beer',
                       'Dane-blue', '5-dog', 'blue-horse',
                       'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                      'Norwegian-beverage'),
            "answer": 'water',
        },

    ],

    "Extra": [
        {
            "input": (['Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                       'German-coffee', 'beer-white', 'cat-water',
                       'horse-2', 'milk-3', '4-Rothmans',
                       'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                       'bird-Brit', '4-green', 'Winfield-beer',
                       'Dane-blue', '5-dog', 'blue-horse',
                       'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'], 'horse-cigarettes'),
            "answer": 'Marlboro',
        },
        {
            "input": (['Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                       'German-coffee', 'beer-white', 'cat-water',
                       'horse-2', 'milk-3', '4-Rothmans',
                       'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                       'bird-Brit', '4-green', 'Winfield-beer',
                       'Dane-blue', '5-dog', 'blue-horse',
                       'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'], 'green-number'),
            "answer": '4',
        },
        {
            "input": (['Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                       'German-coffee', 'beer-white', 'cat-water',
                       'horse-2', 'milk-3', '4-Rothmans',
                       'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                       'bird-Brit', '4-green', 'Winfield-beer',
                       'Dane-blue', '5-dog', 'blue-horse',
                       'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'], 'milk-color'),
            "answer": 'red',
        },
        {
            "input": (['Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                       'German-coffee', 'beer-white', 'cat-water',
                       'horse-2', 'milk-3', '4-Rothmans',
                       'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                       'bird-Brit', '4-green', 'Winfield-beer',
                       'Dane-blue', '5-dog', 'blue-horse',
                       'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'], 'Winfield-nationality'),
            "answer": 'Swede',
        },
        {
            "input": (['Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                       'German-coffee', 'beer-white', 'cat-water',
                       'horse-2', 'milk-3', '4-Rothmans',
                       'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                       'bird-Brit', '4-green', 'Winfield-beer',
                       'Dane-blue', '5-dog', 'blue-horse',
                       'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'], 'yellow-pet'),
            "answer": 'cat',
        },
    ]}

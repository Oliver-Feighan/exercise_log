import datetime



class CalisthenicsData(object):
    """
    the data object that contains the data to be input into the
    calisthenics table.
    >>> import datetime
    >>> calisthenic_data = \
     CalisthenicsData({ \
      "logdate" : datetime.datetime.now().date() \
    , "pushups" : 75 \
    , "pullups" : 18 \
    , "squats" : 90  \
    , "comments" : "comment comment" \
    , "rating" : "8.5" \
    })
    >>> calisthenic_data.date
    datetime.date(2020, 6, 21)
    >>> calisthenic_data.pushups
    75
    >>> calisthenic_data.pullups
    18
    >>> calisthenic_data.squats
    90
    >>> calisthenic_data.comments
    'comment comment'
    >>> calisthenic_data.rating
    '8.5'
    >>> calisthenic_data.make_data_dict()
    {'logdate': datetime.date(2020, 6, 21), 'pushups': 75, 'pullups': 18, 'squats': 90, 'comments': 'comment comment', 'rating': '8.5'}

    """
    def __init__(self, params):
        self.date     = params.get("logdate")
        self.pushups  = params.get("pushups")
        self.pullups  = params.get("pullups")
        self.squats   = params.get("squats")
        self.comments = params.get("comments")
        self.rating   = params.get("rating")


    def make_data_tuple(self) -> tuple:
        data_tuple = (
        self.date,
        self.pushups,
        self.pullups,
        self.squats,
        self.comments,
        self.rating,
        )

        return data_tuple
